# Pick a random friend from the list
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]  
random_friend = random.choice(friends)
print(f"Randomly selected friend: {random_friend}")
#2nd option using randint
random_index = random.randint(0, len(friends) - 1)
random_friend_2 = friends[random_index]
print(f"Randomly selected friend using randint: {random_friend_2}")
