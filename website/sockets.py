from flask_socketio import join_room, leave_room, send
from flask import session
from . import db, socketio
from .models import Messages, Room
from flask_login import current_user
from datetime import datetime

@socketio.on("connect")
def connect():
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    room_obj = Room.query.filter_by(name=room).first()
    if not room_obj:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    #rooms[room]["members"]+= 1
    print(f"{name} joined room {room}")


@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    #if room in rooms:
        #rooms[room]["members"] -= 1
        #if rooms[room]["members"] <= 0:
        #    del rooms[room]
    

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")


@socketio.on("new-message")
def message(data):
    room = session.get("room")
    room_obj = Room.query.filter_by(name=room).first()
    if not room_obj:
        return
    
    content = {
        "name":  session.get("name"),
        "message": data["data"]
        #Date & time of sent message should be here and parsed.
    }

    date = datetime.now()


    #messages are now saved in the personal Messages Model
    new_message = Messages(data=data["data"], user_id=current_user.id, room_id=room_obj.name,date=date)
    db.session.add(new_message)
    db.session.commit()

    send(content, to=room)
    print(f"{session.get('name')} said: {data['data']}")
