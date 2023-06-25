#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo1
print(logo1)

print("Welcome to the secret auction program.")

def find_highest_bidder(bidder_record):
  highest_amount = 0
  for bidder in bidder_record:
    bidding_amount = bidder_record[bidder]
    if bidding_amount > highest_amount:
      highest_amount = bidding_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest_amount}")

bidders = {}
should_continue = True
while should_continue:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  bidders[name] = bid
  response = input("Are there any other bidders? Type   yes or no: ").lower()
  if response == 'no':
    should_continue = False
    find_highest_bidder(bidders)
  else:
    should_continue = True
    #clear()
    
  
  
  
  
'''

bidders_list =[]
should_continue = True

while should_continue:
  bidders = {}
  name = input("What is your name? ")
  bidders['name'] = name
  bid = int(input("What is your bid? "))
  bidders['bid'] = bid
  bidders_list.append(bidders)
  response = input("Are there any other bidders? Type   yes or no: ").lower()
  
  if response == 'no':
    should_continue = False
    clear()
    
  else:
    should_continue = True
    clear()
    
  
  



bids = []

for bidders in bidders_list:
  for k,v in bidders.items():
    if k == 'bid':
      bids.append(v)
    


def find_max(bids):
  return max(bids)
max_bid = find_max(bids)

for bidders in bidders_list:
  for k,v in bidders.items():
    if k =='bid':
      if v == max_bid:
        print(f" The winner is {bidders['name']} with a bid of {bidders['bid']}")


'''

  
  