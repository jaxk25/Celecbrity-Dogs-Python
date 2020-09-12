#!/usr/bin/env python2
# Celebrity Dogs game
# Written in Python 2.7

# Define global variables
all_cards = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad'] # Define the characters assigned to each card
p_cat = '' # The player's category
c_cat = '' # The computer's category
p_cat_val = '' # The value of the player's category
c_cat_val = '' # The value of the computer's category
winner="" # The winner of the round

# Import modules
import random # Used for random intergers
import time # Used for timed pauses

def clear(): # Function to clear screen
      for i in range(0,100): # Repeat 100 times
            print("\n") # Print newlines characters to clear screen of any text

def menu(): # Function to show the main menu
      menu_choice = raw_input("Play Game\nHelp\nQuit\n>>> ") # Ask for user input
      menu_choice = menu_choice.lower() # Set characters in menu_choice to all lower case
      if menu_choice == 'play game': # If the user selected the play game option,
            game() # Call the game function
      elif menu_choice == 'help': # Display help information
            print("\nWelcome to Celebrity Dogs!\nThis game was made for the 2019 AQA Computer Science exam task.\nPlease type Play Game to play the game, Help to view this again or Quit to exit.\nAll areas where you need to type are case insensitive.\nWhen playing the game, you will be given instuctions at each section to help you.\nIf you have any queries, please contact jaxk.programmer@gmail.com.\nTo download again or to find the source code on GitHub, go to https://www.jaxk.ga/celeb-dogs.\nThank you for playing Celebrity Dogs!\n") # Output help information to the screen
            menu() # Call menu function to restart the menu
      elif menu_choice == 'quit': # If the player wants to quit:
            print("\nThank you for playing") # Display message to user
            raw_input("Press RETURN to exit")# When the user presses RETURN, end program
            clear() # Call function to clear the screen
            quit() # Use python built-in function to quit
      else: # If the user does not enter a valid option,
            print("\nError\n") # If neither result is entered, return an error
            menu() # Call the menu function to restart the menu

def game(): # Function for the main game
      # Define variables
      p_cat = '' # Variable to store which category the player picked
      c_cat = '' # Variable to store which category the computer picked
      p_cat_val = '' # Variable to store the value of the player's card for the selected category
      c_cat_val = '' # Variable to store the value of the computer's card for the selected category
      winner='' # Variable to store the winner of the round
      winner = random.choice(['player','player','computer']) # Pick a random player to start the game. Ratio for chance of being picked -> player:computer=2:1
      possible_cards = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28] # Define number of cards that can be used
      while True: # While the player has not picked a valid number of cards, repeat
            try:
                  cards_tbp = int(raw_input("\nHow many cards would you like to be played?\nThis includes you and the computer.\nThe number must be above 4, but below 30, and only an even number.\n>>> ")) # Ask for user input and convert it into an integer
                  print("\nYou have selected to play " +str(cards_tbp) +" cards.\n") # Print how many cards were selected
                  break # If successful, break out of while loop
            except ValueError: # If the number is not valid (e.g float or string, not int),
                  print("\nThat is not a valid number!") # Give an error
      selection = raw_input("Is this ok?\n>>>[Y/N] ")# Confirm amount of cards is correct
      selection = selection.lower() # Set selection variable to all lower case
      if selection == 'y': # If the user selected yes,
            print("\nOk.\n") # Continue program
      elif selection == 'n': # If the user selected no,
            print("\nOk.\n Returning to selection.\n") # Restart selection
            game() # Call game function to allow user to reselect amount of cards
      else: # If the user inputted a value that can not be handled,
            print("\nError\n") # Output an error
            game() # Call game function to allow user to reselect amount of cards
      if cards_tbp in possible_cards: # If player's selection is valid and in possible_cards,
            f=open("dogs.txt", "r") # Open dogs.txt in read mode
            if f.mode == 'r': # If opened correctly in read mode,
                  contents = f.read() # Set contents value to what is in the dogs.txt file
                  a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad = contents.split(";") # Split contents into separate variables at every ','
                  a_exercise,a_intelligence,a_friendliness,a_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  b_exercise,b_intelligence,b_friendliness,b_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  c_exercise,c_intelligence,c_friendliness,c_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  d_exercise,d_intelligence,d_friendliness,d_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  e_exercise,e_intelligence,e_friendliness,e_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  f_exercise,f_intelligence,f_friendliness,f_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  g_exercise,g_intelligence,g_friendliness,g_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  h_exercise,h_intelligence,h_friendliness,h_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  i_exercise,i_intelligence,i_friendliness,i_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  j_exercise,j_intelligence,j_friendliness,j_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  k_exercise,k_intelligence,k_friendliness,k_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  l_exercise,l_intelligence,l_friendliness,l_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  m_exercise,m_intelligence,m_friendliness,m_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  n_exercise,n_intelligence,n_friendliness,n_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  o_exercise,o_intelligence,o_friendliness,o_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  p_exercise,p_intelligence,p_friendliness,p_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  q_exercise,q_intelligence,q_friendliness,q_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  r_exercise,r_intelligence,r_friendliness,r_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  s_exercise,s_intelligence,s_friendliness,s_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  t_exercise,t_intelligence,t_friendliness,t_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  u_exercise,u_intelligence,u_friendliness,u_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  v_exercise,v_intelligence,v_friendliness,v_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  w_exercise,w_intelligence,w_friendliness,w_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  x_exercise,x_intelligence,x_friendliness,x_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  y_exercise,y_intelligence,y_friendliness,y_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  z_exercise,z_intelligence,z_friendliness,z_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  aa_exercise,aa_intelligence,aa_friendliness,aa_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  ab_exercise,ab_intelligence,ab_friendliness,ab_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  ac_exercise,ac_intelligence,ac_friendliness,ac_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  ad_exercise,ad_intelligence,ad_friendliness,ad_drool = random.randint(1,5),random.randint(1,100),random.randint(1,10),random.randint(1,10) # Randomly select variables for each card, one variable for exercise, intelligence, friendliness and drool
                  if cards_tbp <= 5: # If not enough cards were selected
                        print("Error! Cards selected is too low or not even. Returning to card selection...\n") # Give an error
                        game() # Call the game function to restart card selection
                  elif cards_tbp >= 29: # If too many cards were selected
                        print("Error! Cards selected is too high or not even. Returning to card selection...\n") # Give an error
                        game() # Call the game function to restart card selection
                  elif cards_tbp == 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20 or 22 or 24 or 26 or 28: # If a valid number of cards were selected,
                        allocated_cards = [] # Set allocated_cards to empty list
                        player_cards = [] # Set the player's cards to empty list
                        computer_cards = [] # Set the computer's cards to empty list
                        while len(player_cards) != (cards_tbp/2): # While the player has less than half of all cards played this game,
                              random_card = random.choice(all_cards) # Pick a random card
                              if random_card not in allocated_cards: # If the random card is not already being used,
                                    player_cards.append(random_card) # Give selected card to player
                                    allocated_cards.append(random_card) # Add to allocated cards list
                        print("Your cards are:") # Tell the player what cards they have
                        for cards in range(len(player_cards)-1): # Repeat for the amount of cards that the player has
                              if player_cards[cards] == 'a': # Tell the player the name of the cards they have
                                    print("\n\tAnnie the Afgan Hound")
                              elif player_cards[cards] == 'b': # Tell the player the name of the cards they have
                                    print("\n\tBertie the Boxer")
                              elif player_cards[cards] == 'c': # Tell the player the name of the cards they have
                                    print("\n\tBetty the Borzoi")
                              elif player_cards[cards] == 'd': # Tell the player the name of the cards they have
                                    print("\n\tCharlie the Chihuahua")
                              elif player_cards[cards] == 'e': # Tell the player the name of the cards they have
                                    print("\n\tChaz the Cockerspaniel")
                              elif player_cards[cards] == 'f': # Tell the player the name of the cards they have
                                    print("\n\tDonald the Dalmation")
                              elif player_cards[cards] == 'g': # Tell the player the name of the cards they have
                                    print("\n\tAlfie the Affenpinscher")
                              elif player_cards[cards] == 'h': # Tell the player the name of the cards they have
                                    print("\n\tAlbert the Alaskan Klee Kai")
                              elif player_cards[cards] == 'i': # Tell the player the name of the cards they have
                                    print("\n\tBernie the Black and Tan Coonhound")
                              elif player_cards[cards] == 'j': # Tell the player the name of the cards they have
                                    print("\n\tChloe the Chinese Shar-Pei")
                              elif player_cards[cards] == 'k': # Tell the player the name of the cards they have
                                    print("\n\tElizabeth the English Toy Spaniel")
                              elif player_cards[cards] == 'l': # Tell the player the name of the cards they have
                                    print("\n\tJake the Japanese Chin")
                              elif player_cards[cards] == 'm': # Tell the player the name of the cards they have
                                    print("\n\tKaty the Korean Jindo Dog")
                              elif player_cards[cards] == 'n': # Tell the player the name of the cards they have
                                    print("\n\tKaapro the Kooikerhondje")
                              elif player_cards[cards] == 'o': # Tell the player the name of the cards they have
                                    print("\n\tKa the Komondor")
                              elif player_cards[cards] == 'p': # Tell the player the name of the cards they have
                                    print("\n\tMatt the Mutt")
                              elif player_cards[cards] == 'q': # Tell the player the name of the cards they have
                                    print("\n\tNancy the Norfolk Terrier")
                              elif player_cards[cards] == 'r': # Tell the player the name of the cards they have
                                    print("\n\tNoelle the Norwich Terrier")
                              elif player_cards[cards] == 's': # Tell the player the name of the cards they have
                                    print("\n\tNatasha the Nova Scotia Tolling Retriever")
                              elif player_cards[cards] == 't': # Tell the player the name of the cards they have
                                    print("\n\tStacy the Staffordshire Bull Terrier")
                              elif player_cards[cards] == 'u': # Tell the player the name of the cards they have
                                    print("\n\tBrenda the Bull Dog")
                              elif player_cards[cards] == 'v': # Tell the player the name of the cards they have
                                    print("\n\tDarcy the Dogo Argentino")
                              elif player_cards[cards] == 'w': # Tell the player the name of the cards they have
                                    print("\n\tGlenda the German Shorthaired Pointer")
                              elif player_cards[cards] == 'x': # Tell the player the name of the cards they have
                                    print("\n\tHerbet the Havanese")
                              elif player_cards[cards] == 'y': # Tell the player the name of the cards they have
                                    print("\n\tPeter the Pekingese")
                              elif player_cards[cards] == 'z': # Tell the player the name of the cards they have
                                    print("\n\tPerkie the Plott")
                              elif player_cards[cards] == 'aa': # Tell the player the name of the cards they have
                                    print("\n\tPoppy the Puli")
                              elif player_cards[cards] == 'ab': # Tell the player the name of the cards they have
                                    print("\n\tXenophon the Xoloitzcuintli")
                              elif player_cards[cards] == 'ac': # Tell the player the name of the cards they have
                                    print("\n\tYork the Yorkipoo")
                              elif player_cards[cards] == 'ad': # Tell the player the name of the cards they have
                                    print("\n\tSan the Samoyed")
                              else: # If unknown card is in the player's deck,
                                    print("Error! Retruning to card selection") # Give an error
                                    game() # Call game function to allow player to restart game
                        print("\n") # Print newline
                        while len(computer_cards) != (cards_tbp/2): # While the computer has less than half the amount of cards being played this game,
                              random_card = random.choice(all_cards) # Pick a random card
                              if random_card not in allocated_cards: # If the random card is not already being used, do
                                    computer_cards.append(random_card) # Give the selected card to computer
                                    allocated_cards.append(random_card) # Add card to allocated cards list
                        while len(player_cards) != 0: # While the player still has cards,
                              print("\nYour card is:")# Tell the player what their card is.
                              if player_cards[len(player_cards)-1] == 'a': # If card is 'a'
                                    p_card_selected = 'a' # Set as active player card
                                    print("\nAnnie the Afgan Hound") # Print name
                                    print("Intelligence =\t" +str(a_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(a_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(a_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(a_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'b': # If card is 'b'
                                    p_card_selected = 'b' # Set as active player card
                                    print("\nBertie the Boxer") # Print name
                                    print("Intelligence =\t" +str(b_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(b_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(b_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(b_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'c': # If card is 'c'
                                    p_card_selected = 'c' # Set as active player card
                                    print("\nBetty the Borzoi") # Print name
                                    print("Intelligence =\t" +str(c_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(c_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(c_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(c_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'd': # If card is 'd'
                                    p_card_selected = 'd' # Set as active player card
                                    print("\nCharlie the Chihuahua") # Print name
                                    print("Intelligence =\t" +str(d_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(d_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(d_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(d_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'e': # If card is 'e'
                                    p_card_selected = 'e' # Set as active player card
                                    print("\nChaz the Cockerspaniel") # Print name
                                    print("Intelligence =\t" +str(e_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(e_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(e_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(e_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'f': # If card is 'f'
                                    p_card_selected = 'f' # Set as active player card
                                    print("\nDonald the Dalmation") # Print name
                                    print("Intelligence =\t" +str(f_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(f_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(f_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(f_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'g': # If card is 'g'
                                    p_card_selected = 'g' # Set as active player card
                                    print("\nAlfie the Affenpinscher") # Print name
                                    print("Intelligence =\t" +str(g_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(g_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(g_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(g_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'h': # If card is 'h'
                                    p_card_selected = 'h' # Set as active player card
                                    print("\nAlbert the Alaskan Klee Kai") # Print name
                                    print("Intelligence =\t" +str(h_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(h_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(h_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(h_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'i': # If card is 'i'
                                    p_card_selected = 'i' # Set as active player card
                                    print("\nBernie the Black and Tan Coonhound") # Print name
                                    print("Intelligence =\t" +str(i_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(i_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(i_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(i_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'j': # If card is 'j'
                                    p_card_selected = 'j' # Set as active player card
                                    print("\nChloe the Chinese Shar-Pei") # Print name
                                    print("Intelligence =\t" +str(j_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(j_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(j_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(j_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'k': # If card is 'k'
                                    p_card_selected = 'k' # Set as active player card
                                    print("\nElizabeth the English Toy Spaniel") # Print name
                                    print("Intelligence =\t" +str(k_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(k_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(k_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(k_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'l': # If card is 'l'
                                    p_card_selected = 'l' # Set as active player card
                                    print("\nJake the Japanese Chin") # Print name
                                    print("Intelligence =\t" +str(l_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(l_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(l_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(l_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'm': # If card is 'm'
                                    p_card_selected = 'm' # Set as active player card
                                    print("\nKaty the Korean Jindo Dog") # Print name
                                    print("Intelligence =\t" +str(m_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(m_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(m_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(m_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'n': # If card is 'n'
                                    p_card_selected = 'n' # Set as active player card
                                    print("\nKaapro the Kooikerhondje") # Print name
                                    print("Intelligence =\t" +str(n_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(n_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(n_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(n_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'o': # If card is 'o'
                                    p_card_selected = 'o' # Set as active player card
                                    print("\nKa the Komondor") # Print name
                                    print("Intelligence =\t" +str(o_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(o_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(o_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(o_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'p': # If card is 'p'
                                    p_card_selected = 'p' # Set as active player card
                                    print("\nMatt the Mutt") # Print name
                                    print("Intelligence =\t" +str(p_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(p_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(p_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(p_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'q': # If card is 'q'
                                    p_card_selected = 'q' # Set as active player card
                                    print("\nNancy the Norfolk Terrier") # Print name
                                    print("Intelligence =\t" +str(q_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(q_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(q_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(q_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'r': # If card is 'r'
                                    p_card_selected = 'r' # Set as active player card
                                    print("\nNoelle the Norwich Terrier") # Print name
                                    print("Intelligence =\t" +str(r_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(r_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(r_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(r_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 's': # If card is 's'
                                    p_card_selected = 's' # Set as active player card
                                    print("\nNatasha the Nova Scotia Tolling Retriever") # Print name
                                    print("Intelligence =\t" +str(s_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(s_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(s_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(s_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 't': # If card is 't'
                                    p_card_selected = 't' # Set as active player card
                                    print("\nStacy the Staffordshire Bull Terrier") # Print name
                                    print("Intelligence =\t" +str(t_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(t_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(t_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(t_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'u': # If card is 'u'
                                    p_card_selected = 'u' # Set as active player card
                                    print("\nBrenda the Bull Dog") # Print name
                                    print("Intelligence =\t" +str(u_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(u_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(u_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(u_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'v': # If card is 'v'
                                    p_card_selected = 'v' # Set as active player card
                                    print("\nDarcy the Dogo Argentino") # Print name
                                    print("Intelligence =\t" +str(v_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(v_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(v_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(v_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'w': # If card is 'w'
                                    p_card_selected = 'w' # Set as active player card
                                    print("\nGlenda the German Shorthaired Pointer") # Print name
                                    print("Intelligence =\t" +str(w_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(w_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(w_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(w_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'x': # If card is 'x'
                                    p_card_selected = 'x' # Set as active player card
                                    print("\nHerbet the Havanese") # Print name
                                    print("Intelligence =\t" +str(x_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(x_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(x_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(x_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'y': # If card is 'y'
                                    p_card_selected = 'y' # Set as active player card
                                    print("\nPeter the Pekingese") # Print name
                                    print("Intelligence =\t" +str(y_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(y_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(y_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(y_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'z': # If card is 'z'
                                    p_card_selected = 'z' # Set as active player card
                                    print("\nPerkie the Plott") # Print name
                                    print("Intelligence =\t" +str(z_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(z_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(z_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(z_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'aa': # If card is 'aa'
                                    p_card_selected = 'aa' # Set as active player card
                                    print("\nPoppy the Puli") # Print name
                                    print("Intelligence =\t" +str(aa_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(aa_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(aa_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(aa_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'ab': # If card is 'ab'
                                    p_card_selected = 'ab' # Set as active player card
                                    print("\nXenophon the Xoloitzcuintli") # Print name
                                    print("Intelligence =\t" +str(ab_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(ab_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(ab_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(ab_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'ac': # If card is 'ac'
                                    p_card_selected = 'ac' # Set as active player card
                                    print("\nYork the Yorkipoo") # Print name
                                    print("Intelligence =\t" +str(ac_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(ac_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(ac_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(ac_drool)) # Print drool
                              elif player_cards[len(player_cards)-1] == 'ad': # If card is 'ad'
                                    p_card_selected = 'ad' # Set as active player card
                                    print("\nSan the Samoyed") # Print name
                                    print("Intelligence =\t" +str(ad_intelligence)) # Print intelligence
                                    print("Exercise =\t" +str(ad_exercise)) # Print exercise
                                    print("Friendliness =\t" +str(ad_friendliness)) # Print friendliness
                                    print("Drool =\t" +str(ad_drool)) # Print drool
                              print("") # Print an empty line
                              p_cat = '' #set the player's category selection to nothing
                              print("The " +winner +" has been randomly selected to pick first.")
                              if winner == "player": #if the player won the last round, or if this is the first round, give the player choice over the category
                                    while p_cat != 'intelligence' or 'exercise' or 'friendliness' or 'drool': #while the player hasn't picked a valid category, loop
                                          p_cat = raw_input("\nWhat category would you like to use?\n>>> ") #Ask what category the player would like to use
                                          p_cat = p_cat.lower() #set p_cat to all lower-case
                                          if p_cat == 'intelligence': # if p_cat is 'intelligence', do
                                                print("Ok")
                                                c_cat = 'Intelligence' #set both player's categories to intelligence
                                                break #break out of the loop
                                          elif p_cat == 'exercise': #if p_cat is 'exercise', do
                                                print("Ok")
                                                c_cat = 'Excercise' #set both player's categories to exercise
                                                break #break out of the loop
                                          elif p_cat == 'friendliness': #if p_cat is 'friendliness', do
                                                print("Ok")
                                                c_cat = 'Friendliness' #set both player's categories to friendliness
                                                break #break out of the loop
                                          elif p_cat == 'drool': #if p_cat is 'drool', do
                                                print("Ok")
                                                c_cat = 'Drool' #set both player's categories to drool
                                                break #break out of the loop
                                          elif p_cat == 'overide': #if overide is given, quit this game
                                                print("Ok")
                                                game() #return to card selection
                                          else: #if p_cat is none, do, and repeat loop
                                                print("")#error
                              elif winner == "computer": #if the computer won the last round, give the computer choice over the category
                                    all_categories = ['Intelligence', 'Exercise', 'Friendliness', 'Drool'] #define the categories that the computer could pick
                                    c_cat = random.choice(all_categories) #pick a random category
                                    if c_cat == 'Intelligence': #set both player's categories to intelligence
                                          print("\nThe computer chose intelligence.\n")
                                          p_cat = 'intelligence'
                                    elif c_cat == 'Exercise': #set both player's categories to exercise
                                          print("\nThe computer chose exercise.\n")
                                          p_cat = 'exercise'
                                    elif c_cat == 'Friendliness': #set both player's categories to friendliness
                                          print("\nThe computer chose friendliness.\n")
                                          p_cat = 'friendliness'
                                    elif c_cat == 'Drool': #set both player's categories to drool
                                          print("\nThe computer chose drool.\n")
                                          p_cat = 'drool'
                                    else:
                                          print("Error")
                              else:
                                    print("Error")
                              if True: #always do:
                                    if p_cat == 'intelligence':#set p_cat_val to the correct value for the selected category
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_intelligence
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_intelligence
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_intelligence
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_intelligence
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_intelligence
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_intelligence
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_intelligence
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_intelligence
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_intelligence
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_intelligence
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_intelligence
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_intelligence
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_intelligence
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_intelligence
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_intelligence
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_intelligence
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_intelligence
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_intelligence
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_intelligence
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_intelligence
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_intelligence
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_intelligence
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_intelligence
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_intelligence
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_intelligence
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_intelligence
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_intelligence
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_intelligence
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_intelligence
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_intelligence
                                          else:
                                                print("Error")
                                    elif p_cat == 'exercise':
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_exercise
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_exercise
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_exercise
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_exercise
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_exercise
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_exercise
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_exercise
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_exercise
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_exercise
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_exercise
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_exercise
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_exercise
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_exercise
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_exercise
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_exercise
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_exercise
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_exercise
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_exercise
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_exercise
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_exercise
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_exercise
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_exercise
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_exercise
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_exercise
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_exercise
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_exercise
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_exercise
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_exercise
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_exercise
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_exercise
                                          else:
                                                print("")#error
                                    elif p_cat == 'friendliness':
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_friendliness
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_friendliness
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_friendliness
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_friendliness
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_friendliness
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_friendliness
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_friendliness
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_friendliness
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_friendliness
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_friendliness
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_friendliness
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_friendliness
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_friendliness
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_friendliness
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_friendliness
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_friendliness
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_friendliness
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_friendliness
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_friendliness
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_friendliness
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_friendliness
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_friendliness
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_friendliness
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_friendliness
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_friendliness
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_friendliness
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_friendliness
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_friendliness
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_friendliness
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_friendliness
                                          else:
                                                print("Error")
                                    elif p_cat == 'drool':
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_drool
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_drool
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_drool
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_drool
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_drool
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_drool
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_drool
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_drool
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_drool
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_drool
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_drool
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_drool
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_drool
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_drool
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_drool
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_drool
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_drool
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_drool
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_drool
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_drool
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_drool
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_drool
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_drool
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_drool
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_drool
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_drool
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_drool
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_drool
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_drool
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_drool
                                          else:
                                                print("Error")
                                    else:
                                          print("Error!")
                                    if c_cat == "Intelligence":
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_intelligence
                                          else:
                                                print("Error")
                                    elif c_cat == 'Exercise':
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_exercise
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_exercise
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_exercise
                                          else:
                                                print("")
                                    elif c_cat == 'Friendliness':
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_friendliness
                                          else:
                                                print("Error")
                                    elif c_cat == 'Drool':
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_drool
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_drool
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_drool
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_drool
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_drool
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_drool
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_drool
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_drool
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_drool
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_drool
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_drool
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_drool
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_drool
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_drool
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_drool
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_drool
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_drool
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_drool
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_drool
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_drool
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_drool
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_drool
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_drool
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_drool
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_drool
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_drool
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_drool
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_drool
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_drool
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_drool
                                          else:
                                                print("Error")
                                    else:
                                          print("Error!")
                              if p_cat == 'intelligence': #if p_cat is intelligence, do
                                    if p_cat_val > c_cat_val: #if the value of p_cat_val is bigger than the computer's, do
                                          print("You had a higher score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round  
                                    else:
                                          print("The computer had a higher score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          winner="computer" #decide who the winner is so they have control over the category next round
                              elif p_cat == 'exercise':
                                    if p_cat_val > c_cat_val:
                                          print("You had a higher score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round
                                    else:
                                          print("The computer had a higher score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          winner="computer" #decide who the winner is so they have control over the category next round
                              elif p_cat == 'friendliness':
                                    if p_cat_val > c_cat_val:
                                          print("You had a higher score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round    
                                    else:
                                          print("The computer had a higher score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          winner="computer" #decide who the winner is so they have control over the category next round
                              elif p_cat == 'drool':
                                    if p_cat_val < c_cat_val:
                                          print("You had a lower score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          player_cards.append(card_tbm) #give the card to the other player
                                          winner="player" #decide who the winner is so they have control over the category next round
                                    else:
                                          print("The computer had a lower score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1] #select the card that needs to be moved
                                          player_cards.pop(len(player_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          card_tbm = computer_cards[len(computer_cards)-1] #select the card that needs to be moved
                                          computer_cards.pop(len(computer_cards)-1) #remove the card
                                          computer_cards.append(card_tbm) #give the card to the other player
                                          winner="computer" #decide who the winner is so they have control over the category next round          
                              else:
                                    print("Fatal Error!") #error
                              if len(player_cards) == cards_tbp or len(computer_cards) == int('0'): #if the player has all cards or the computer has no cards, do
                                    player_cards = [] #remove all of the player's cards
                                    computer_cards = [] #remove all of the computer's cards
                                    clear() #clear the screen
                                    print("Well done, you won!")
                                    print("\nThank you for playing")
                                    raw_input("Press RETURN to return to the menu")#when RETURN pressed, do
                                    clear() #clear the screen
                                    menu() #return to the menu
                              elif len(player_cards) == int('0') or len(computer_cards) == cards_tbp: #if the player has no cards or the computer has all the cards, do
                                    player_cards = [] #remove all of the player's cards
                                    computer_cards = [] #remove all of the computer's cards
                                    clear() #clear the screen
                                    print("Bad luck, you lost.")
                                    print("\nThank you for playing")
                                    raw_input("Press RETURN to return to the menu")#when RETURN pressed, do
                                    clear() #clear the sreen
                                    menu() #return to the menu
                              else: #carry on with the game loop
                                    print("") #Do literally nothing
                              time.sleep(1.5) #give 1.5 seconds in case the computer won the last round so they player can read the screen
                  else:
                        print("Unknown Error! Retrurning to card selection.")
                        game()#return to card selection
      else:
              print("Error with selected number of cards. Returning to card selection.")
              game()#return to card selection

clear()#make blank screen
menu()#start the menu function
