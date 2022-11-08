class Room(RunnerView):
    template_name = "src/room.html"
    def get_response(username, peer_id):
        # do something
        if peer_id and username:
            object = save_to_database(data={
                "username": username,
                "peer_id": peer_id
            }, type="json")
            print(object)
            message =  "saved to database successfully"
        else:
            message = "No data"
        print(message)
        return message

class OnlineUsers(RunnerView):
    template_name = "src/online_users.html"
    def get_response():
        # do something
        users = get_data_from_database(fields = {'data__icontains': ''})
        print(users)
        usrs = [user.get_data() for user in users]
        return usrs

RUNNER_STORE_VALUES_LIST = [
    {
        "name": "Room",
        "variable": Room,
    },
    {
        "name": "Online Users",
        "variable": OnlineUsers,
    }
]