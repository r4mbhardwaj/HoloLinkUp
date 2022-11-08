class Room(RunnerView):
    template_name = "src/room.html"
    def get_response(username):
        # do something
        return "Hello World"

RUNNER_STORE_VALUES_LIST = [
    {
        "name": "Room",
        "variable": Room,
    }
]