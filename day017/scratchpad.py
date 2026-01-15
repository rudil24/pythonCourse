class User:
    def __init__(self, user_id, username):        
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): #when I follow another user, invoke this method
        user.followers += 1 #i follow them so they gain a follower
        self.following += 1 #i'm following them so i increment my following count

user_1 = User("001", "alice")
user_2 = User("002", "bob")

print(user_1.followers)  # Output: 0

user_1.follow(user_2)    #make user_1 follow user_2
print(user_1.followers)  # Output: 0
print(user_1.following)  # Output: 1
print(user_2.followers)  # Output: 1
print(user_2.following)  # Output: 0