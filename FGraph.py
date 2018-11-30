class FGraph:

	def __init__(self, data):
		self.data = data

	def findFriends(self, user):
		return user.friends

	def findFriendsFriends(self, user):
		allSecondFriends = []
		friends = self.findFriends(user)
		for friend in friends:
			for user in self.data:
				if user.id == friend:
					allSecondFriends = allSecondFriends + self.findFriends(user)
					allSecondFriends = list(set(allSecondFriends))
					break

		allSecondFriends = [x for x in allSecondFriends if x not in friends]
		return allSecondFriends

	def findCommonFriends(self, test):
		friends = self.findFriends(test)
		secondFriends = self.findFriendsFriends(test)
		commonFriends = []

		for second in secondFriends:
			for user in self.data:
				if user.id == second:
					common = len(set(friends) & set(user.friends))
					commonFriends.append([user.id, common])
					break
			
		commonFriends.sort(key=lambda x: x[1], reverse=True)
		i = 1

		print("Recommendations for user " + test.id)
		while i < 5:
			print(commonFriends[i][0] + ", because they have " + str(commonFriends[i][1]) + " friends in common!")
			i += 1

	def findRealFriends(self, test):

		#Friends of test
		friends = self.findFriends(test)

		#Second friends of test
		secondFriends = self.findFriendsFriends(test)
		commonFriends = []

		#For each secondFriend find common friends
		for second in secondFriends:
			commons = []
			suggestion = 0
			for user in self.data:
				if user.id == second:
					commons = set(friends) & set(user.friends)
					break

			for common in commons:
				for user in self.data:
					if user.id == second:
						suggestion += 1/len(user.friends)

			commonFriends.append([second, suggestion])

		commonFriends.sort(key=lambda x: x[1], reverse=True)
		print("Recommendations for user " + test.id)

		i = 1

		while i < 5:
			print(str(commonFriends[i][0]) + ", because their friendship ratio is " + str(commonFriends[i][1]))
			i += 1


