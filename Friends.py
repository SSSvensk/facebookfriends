import sys
from User import User
from FGraph import FGraph

users = []

#Opening and reading the .txt-file containing the links between users

with open("friends.txt") as infile:
    u = 0
    friends = []
    user = User(0)
    for line in infile:
        parts = line.split("\t")

        #To detect if it's the first user in the list or if the user in the first column is different
        #ASSUMPTION: Each user is grouped in text-file only once. So it is assumed that the user-id in first column won't appear after it has changed.
        if u == 0 or parts[0] != u:
   	        u = parts[0]
   	        user = User(u)
   	        users.append(user)

        user.addFriend(parts[1])
   	
fgraph = FGraph(users)

#Id's of users tested
testuser = ['20341', '33722', '35571', '25017']

#Problem 1

for test in testuser:
	for user in users:
		if user.id == test:
		fgraph.findCommonFriends(user)
		break

#Problem 2

for test in testuser:
  for user in users:
	  if user.id == test:
		  fgraph.findRealFriends(user)
		  break
