class Room(RunnerView):
    template_name = "src/room.html"

    def get_response(room_name, password="demo"):
        if room_name and password:
            # remove the room if it exists
            # create room
            try:
                object = get_object_from_database(fields={
                    "data__room_name": room_name,
                })
                message = "Room already exists"
            except Exception as e:
                print(e)
                # if exception was because get returned more than one object
                # then delete all objects with that room name
                if "get() returned more than one" in str(e):
                    # delete the room if multiple rooms exist
                    delete_data_from_database(fields={
                        "data__room_name": room_name,
                    })
                # create room
                object = save_to_database(name="room", data={
                    "room_name": room_name,
                    "password": password
                })
                message = "saved to database successfully"
            found = True
        else:
            found = False
            message = "please fill all fields"
        print(message)
        return {"message": message, "room_name": room_name, "found": found}


class Peer(RunnerView):
    # template_name = "src/peer.html"

    def get_response(room_name, username, peer_id, password="demo"):
        # check if room and password is correct
        if room_name and password:
            try:
                object = get_object_from_database(fields={
                    "name": "room",
                    "data__room_name": room_name,
                    "data__password": password
                })
            except Exception as e:
                print(e)
                # if exception was because get returned more than one object
                # then delete all objects with that room name
                if "get() returned more than one" in str(e):
                    # delete the room if multiple rooms exist
                    delete_data_from_database(fields={
                        "data__room_name": room_name,
                    })
                    # create room
                    object = save_to_database(name="room", data={
                        "room_name": room_name,
                        "password": password
                    })
                # if exception was because get returned no object
                # then return error message
                elif "get() returned no" in str(e):
                    return {"message": "room does not exist"}
                else:
                    return {"message": "password is incorrect"}
            # search for peer in database
            try:
                object, created = get_or_create_data_in_database(fields={
                    "name": "peer",
                    "data__room_name": room_name,
                    "data__username": username,
                })
                data_dict = {
                    "room_name": room_name,
                    "username": username,
                    "peer_id": peer_id,
                }
                object.data = data_dict
                object.save()
                message = "saved to database successfully"
            except Exception as e:
                print(e)
                message = "error saving to database"
        else:
            message = "please fill all fields"
        print(message)
        return message


class OnlineUsers(RunnerView):
    template_name = "src/online_users.html"

    def get_response(room_name):
        # do something
        users = search_database(
            fields={'name': 'peer', 'data__room_name': room_name})
        print(users)
        return users


RUNNER_STORE_VALUES_LIST = [
    {
        "name": "Room",
        "variable": Room,
    },
    {
        "name": "Online_Users",
        "variable": OnlineUsers,
    },
    {
        "name": "Peer",
        "variable": Peer,
    },
]
