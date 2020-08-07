#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    place = {}

    for ticket in tickets:
        if ticket.source not in place:
            place[ticket.source] = ticket.destination
    for (key, value) in place.items():
        if key == "NONE":
            route.append(value)
    while route[-1] != "NONE":
        route.append(place[route[-1]])
    print(route[0:-1])
    return route

# the source is starting aiport
# destination next airport

#
