from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
from flask import render_template
from bson.objectid import ObjectId
import datetime


app = Flask(__name__)

mongo_client = MongoClient(
    "mongodb+srv://tushar:VjD6w6cWZbvdSsy@cluster0.gfnrw.mongodb.net/db?retryWrites=true&w=majority"
)
db = mongo_client.db
user = db.user
ticket = db.ticket
ticket.create_index('timings',expireAfterSeconds=60*60*8)


@app.route("/api/book", methods=["POST"])
def book():
    input = request.get_json()
    name = input.get("name")
    phone = input.get("phone")
    timings = input.get("timings")
    if name and phone and timings:
        d = datetime.datetime.strptime(timings, "%d-%m-%Y-%H:%M:%S")
        d = d - datetime.timedelta(hours=5, minutes=30)
        if ticket.find({"timings": d}).count() != 20:
            user_id = user.insert_one({"name": name, "phone": phone})
            user_id = user_id.inserted_id
            ticket.insert_one({"user": user_id, "timings": d})
            return {"res": "Done"}
        else:
            return {"res": "Slots filled"}
    else:
        return {"res": "Not Valid I/P"}


@app.route("/api/update", methods=["POST"])
def update():
    input = request.get_json()
    t_id = input.get("ticket")
    new_time = input.get("time")
    if t_id and new_time:
        d = datetime.datetime.strptime(new_time, "%d-%m-%Y-%H:%M:%S")
        d = d - datetime.timedelta(hours=5, minutes=30)
        if ticket.find({"timings": d}).count() != 20:
            ticket.update({"_id": t_id}, {"timings": d})
            return {"res": "updated"}
        else:
            return {"res": "Slots filled"}
    else:
        return {"res": "Not Valid I/P"}


@app.route("/api/tickets", methods=["POST"])
def show():
    input = request.get_json()
    timings = input.get("time")
    if timings:
        d = datetime.datetime.strptime(timings, "%d-%m-%Y-%H:%M:%S")
        d = d - datetime.timedelta(hours=5, minutes=30)
        res = list(ticket.find({"timings": d}))
        response = []
        for r in res:
            obj = {"user": str(r["user"]), "ticket": str(r["_id"])}
            response.append(obj)
        return {"res": response}
    else:
        return {"res": "Not Valid I/P"}


@app.route("/api/delete", methods=["POST"])
def delete():
    input = request.get_json()
    t_id = input.get("ticket")
    if t_id:
        ticket.delete_one({"_id": ObjectId(t_id)})
        return {"res": "Deleted"}
    return {"res": "Not Valid I/P"}


@app.route("/api/user", methods=["POST"])
def details():
    input = request.get_json()
    t_id = input.get("ticket")
    if t_id:
        user_id = ticket.find_one({"_id": ObjectId(t_id)})["user"]
        details = user.find_one({"_id": ObjectId(user_id)})
        details["_id"] = str(details["_id"])
        return {"res": details}
    else:
        return {"res": "Not Valid I/P"}


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
