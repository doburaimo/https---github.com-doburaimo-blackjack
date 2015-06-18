"""
Name:    DANIEL BURAIMO
File:    blackjack.py
Purpose: A game of Blackjack
Run:     python blackjack.py
Input:   Number Of Players and option--Hit or Stand
Output:  Blackjack Winner
"""


from random import randint
from sys import exit
#----------------------------------------------------------------------
def print_card(card):
   """Print a single card"""
   print '(', card[0], ',', card[1], ')',

#----------------------------------------------------------------------
def create_deck():
   """Create a deck of cards
      ranks is a list of the ranks
      suits is a list of the suits"""
   ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
   suits = ['C', 'D', 'H', 'S']
   deck = []
   for suit in suits:
      for rank in ranks:
         card = (rank, suit)
         deck.append(card)
   return deck

#----------------------------------------------------------------------
def shuffle_deck(deck):
   """Shuffle the deck by swapping pairs of cards"""
   for i in range(51):     # i ranges from 0 to 50
      j = randint(i+1,51)  # j ranges from i+1 to 51
      deck[i], deck[j] = deck[j], deck[i]

#----------------------------------------------------------------------
def print_deck(deck):
   """Print a deck of cards"""
   for card in deck:
      print_card(card)
      print

#----------------------------------------------------------------------
def print_hand(hand):
   """Print the cards in a hand"""
   for card in hand:
      print_card(card)
   print

#----------------------------------------------------------------------
def deal_card(deck):
   """Deal one card from the deck"""
   if len(deck) == 0:
      print "Trying to deal from empty deck!"
      print "Bye"
      exit()
   card = deck[0]
   del deck[0]
   return card

#----------------------------------------------------------------------
def eval_blackjack_hand(hand, rank_vals):
   """Return a list whose elements are the possible values of the
      blackjack hand, hand.
      rank_vals is a dictionary with values of the various ranks,
      An ace is stored as 1"""
   val = 0
   ace_count = 0
   for card in hand:
      rank = card[0]
      card_val = rank_vals[rank]
      if card_val > 1:
         val = val + card_val
      else:
         val = val + 1
         ace_count = ace_count+1
   val_list = [val]
   for i in range(ace_count):
      val_list.append(val + (i+1)*10) 
   return val_list
#--------------------------------------------------------------------------
def deal_hands(players,deck):
   hands = []
   for player in range(players):
      hands.append([])
   for i in range(players):
      hands[i] = [ deck[i], deck[players +i]]
   for card in range(2*players):
      deal_card(deck)
   return hands
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def print_hands(hands,bool): 
   if bool == True:
      print
      print "(""Player",players, "is the Dealer"")"
      print "          ","USING THE SHUFFLED DECK"
      for i in range(players):
         print "Player",i+1,"has a hand"," """, hands[i]
   else:
      print
      print "(""Player",players, "is the Dealer"")"
      print "          ","USING THE SHUFFLED DECK"
      for i in range(players - 1):
        print "Player",i+1,"has a hand"," """, hands[i]
      print "Player", players, "has a hand"," ",[hands[players-1][0], "HOLE CARD"]
   
#------------------------------------------------------------------------------------------------
def total_values(players, deck,hands):
   supalist = []
   for i in range(players):
         hand = hands[i]
         val_list = eval_blackjack_hand(hand, rank_vals)
         supalist.append(val_list)
   return supalist

#----------------------------------------------------------------------------------------------------
def values(players, deck, hands):
   valueslist = []
   for i in range(players):
      hand = hands[i]   
      val_list = eval_blackjack_hand(hand, rank_vals)
      t = len(val_list) - 1
      val = val_list[t]
      while t > 0 and val > 21:
         t = t - 1
         val = val_list[t]
      valueslist.append(val)
   return valueslist

#--------------------------------------------------------------------------
def eval_game(valueslist,players,hands):
   print_hands(hands, True)
   print
   print
   bla = []
   t = 0
   while t < players:
      for i in valueslist:
         print "Player",t+1,"has a hand total of ",i 
         t = t+ 1
   for q in valueslist:
      if q < 22 and max(valueslist):
         bla.append(q)
   q = max(bla)
   print 
   for i in range(players):
     if len(hands[i]) == 2:
        while valueslist[i] == 21:
            for (t,y) in hands[i]:
               if len(hands[i]) == 2:
                  if t == 'A' or '10' or 'K' or 'Q' or 'J':
                        print "Player",i+1,"has the first NATURAL"
                        print "If No one else has a NATURAL"
                        print "Player" ,i+1, "wins"
                     
                  break
               break
            exit()
         
   print "The Player with a hand Total of-",q,"-IS THE BLACKJACK WINNER" 
   print "                         ""NOTE"
   print "          ""if 2 or more players have a hand of -",q
   print "The Player with a Natural Blackjack wins or the Game ends as a Draw"  
               
#------------------------------------------------------------------------
def play_dealer_hand(hands,deck,rank_vals):
   print_hands(hands, True)
   values(players, deck, hands)
   total_values(players, deck,hands)
   valueslist = values(players, deck, hands)
   supalist = total_values(players, deck,hands)
   hand = hands[players-1]
   val_list = eval_blackjack_hand(hand, rank_vals)
   for i in hands[players-1]:
          if i[0] == 'A' and valueslist[players-1] >16:
             eval_blackjack_hand(hand, rank_vals)  
          else:
                break
   valueslist = values(players, deck, hands)
   while  valueslist[players-1] < 17:
      new_card = deal_card(deck)
      hands[players-1].append(new_card) 
      valueslist = values(players, deck, hands)
      for i in hands[players-1]:
          if i[0] == 'A' and valueslist[players-1] >16:
             eval_blackjack_hand(hand, rank_vals) 
   if valueslist[players-1] > 16:
      eval_game(valueslist, players,hands) 
   eval_game(valueslist, players,hands) 
  
#----------------------------------------------------------------------    
def query():
   hands = deal_hands(players,deck)
   print_hands(hands, False)
   for player in range(players - 1):
      play_hand(player, hands, deck, rank_vals)
      
   if all_busted(hands,rank_vals)== True:
      print "ALL PLAYERS WENT BUST. THE DEALER AUTOMATICALLY WINS"
      exit()
   else:
      play_dealer_hand(hands,deck,rank_vals)
#-----------------------------------------------------------------------
def play_hand(player, hands, deck, rank_vals):
      busted = False
      hand = hands[player]
      print
      print "Player" ,player + 1," "
      cmd = raw_input("Hit(h) or Stand(s)\n")
      while cmd == "h" and not busted:
         new_card = deal_card(deck)
         hands[player].append(new_card) 
         busted = is_busted(hand, rank_vals)
         print_hands(hands, False)
         total_values(players, deck,hands)
         values(players, deck, hands)
         print
         print "Player",player+1,"has a possible total of"
         print total_values(players, deck,hands)[player]
         print 
         values(players, deck, hands)
         if not busted:
            print "Player" , player + 1
            cmd = raw_input("Hit(h) or Stand(s)\n")
         else:
            print 
            print "Sorry,""Player",player + 1, "you've busted"
#-------------------------------------------------------------------      
      
def is_busted(hand, rank_vals):
   vals = eval_blackjack_hand(hand, rank_vals)
   min_val = min(vals)
   if min_val > 21:
      return True
   else:
      return False
#------------------------------------------------------------------
def all_busted(hands,rank_vals):
   valz = values(players, deck, hands)[0:players-1]   
   min_vals = min(valz)
   if min_vals > 21:
      return True
   else:
      return False
    
#----------------------------------------------------------------------
if __name__ == "__main__":
   rank_vals = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
         '10':10, 'J':10, 'Q':10, 'K':10}
   players = int(raw_input("Input the amount of players\n"))
   deck = create_deck()
   shuffle_deck(deck)
   query()
   