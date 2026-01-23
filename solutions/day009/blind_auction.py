# from replit import clear # i don't have replit, so i'll clear the screen another way

from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  #could also use the max() function with a lambda to achieve the same result:
  # winner = max(bidding_record, key=lambda bidder: bidding_record[bidder])
  # print(f"The winner is {winner} with a bid of ${bidding_record[winner]}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    print("\033[2J\033[1;1H") # this will clear the screen in a non-replit environment
    # clear() # use this line if you are using replit