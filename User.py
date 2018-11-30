class User:

    def __init__(self, u):
        self.id = u
        self.friends = []

    def addFriend(self, f):
    	self.friends.append(f)

    def __str__(self):
    	return "User " + str(self.id) + " has friends: " + str(self.friends)