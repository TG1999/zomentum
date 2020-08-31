To install modules 

`pip3 install -r requirements.txt`

To run server:

`cd ./server`

`python3 __init__.py`

Routes:

To book tickets-

'/api/book'

Example JSON input - 

{"timings":"01-10-2020-20:00:00","name":"Test","phone":"991"}

To update ticket timings-

'/api/update'

Example JSON input - 

{"ticket":"5f4bbefeaf914233364e20ed","time":"01-10-2020-22:00:00"}

To get tickets for a time-

'/api/tickets'

Example JSON input - 

{"time":"01-10-2020-21:00:00"}

To delete ticket-

'/api/delete'

{"ticket":"5f4bcd0febfd336f3d776cc1"}

To show user details-

'/api/user'

{"ticket":"5f4bf57d843435223eedb5c1"}

Every document has a TTL of 8 hours with respect to show time 

This line ensures automatic deletion of tickets after 8 hours 

```ticket.create_index('timings',expireAfterSeconds=60*60*8)```
