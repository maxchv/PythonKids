# http://www.codeskulptor.org/#user15_ZoYz8vHeMS_82.py
# Mini-project #6 - Blackjack

import simpleguitk as simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []        

    def __str__(self):
        # return a string representation of a hand
        r = "Hands contains"
        for card in self.cards:
            r+=" "+str(card)
        return r

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)        

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        aces  = 0
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
            if rank is 'A':
                aces += 1        
        for ace in range(aces):
            if value + 10 < 21:
                value += 10       
        
        return value	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i=1
        for card in self.cards:
            card.draw(canvas, (pos[0]*i, pos[1]))
            i+=1
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for s in SUITS:
            for r in RANKS:            
                self.cards.append(Card(s, r))        

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.cards)	# use random.shuffle() to shuffle the deck

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        r='Deck contains'
        for card in self.cards:
            r+=" "+str(card)
        return r
    
    
#define event handlers for buttons
def deal():
    global outcome, deck, player, dealer, in_play, score
    
    # your code goes here        
    deck = Deck()
    player = Hand()
    dealer = Hand()

    outcome = ""
    deck.shuffle()    
    
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    if in_play:
        score -= 1
    in_play = True

def hit():         
    global in_play, outcome, deck, player, score
    # if the hand is in play, hit the player
    if in_play:        
        player.add_card(deck.deal_card())
        
        # if busted, assign a message to outcome, update in_play and score    
        if player.get_value() > 21:
            outcome = "You went bust and lose."
            in_play = False
            score -= 1
        
        if player.get_value() == 21:            
            stand()
       
def stand():
    global outcome, in_play, deck, player, dealer, score
    
    if in_play:
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card()) 
        # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21 or dealer.get_value() < player.get_value():
            outcome = "You win."
            score += 1
        #elif dealer.get_value() == player.get_value():
        #    outcome = "Dead heat."
        else:
            outcome = "You lose."
            score -= 1
    in_play = False

# draw handler    
def draw(canvas):
    global outcome, in_play, deck, player, dealer
    # test to make sure that card.draw works, replace with your code below
        
    canvas.draw_text("Blackjack", (230, 50), 45, "Aqua")
    if score < 0:
        canvas.draw_text("Score "+str(score), (425, 125), 40, "Red")
    else:
        canvas.draw_text("Score "+str(score), (425, 125), 40, "Black")
           
    if in_play:
        canvas.draw_text("Dealer ("+str(VALUES[dealer.cards[1].get_rank()])+")", (100, 220), 30, "Black")
    else:
        canvas.draw_text("Dealer ("+str(dealer.get_value())+")", (100, 220), 30, "Black")
    canvas.draw_text(outcome, (300, 220), 30, "Black")
    x_card = CARD_SIZE[0]+3
    dealer.draw(canvas, (x_card, 250))
    
    canvas.draw_text("Player ("+str(player.get_value())+")", (100, 420), 30, "Black")
    player.draw(canvas, (x_card, 450))
    
    if in_play:
        canvas.draw_text("Hit or Stand?", (300, 420), 30, "Black")
    else:
        canvas.draw_text("New deal?", (300, 420), 30, "Black")
    
    if in_play: # hole card
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                         [x_card + CARD_BACK_CENTER[0], 250 + CARD_BACK_CENTER[1]], 
                         CARD_BACK_SIZE)
    
deal()

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric
