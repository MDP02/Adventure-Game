import time
import random

foes = ["dragon", "pirate", "ghost", "fairie", "zombie"]

def valid_input(prompt, options):
  while True:
    response = input(prompt).lower()
    for option in options:
      if option in response:
        return response
        break
    else:
      print_pause("Please choose 1 or 2")
  return response

def print_pause(message_to_print):
  print(message_to_print)
  time.sleep(1)

def get_random_foe():
  foe = random.choice(foes)
  return foe

foe = get_random_foe()

def intro():
  print_pause('You find yourself standing in an open field, filled with grass and yellow wildflowers.')
  print_pause('Rumor has it that a ' + foe + ' is somewhere around here, and has been terrifying the nearby village.')
  print_pause('In front of you is a house.')
  print_pause('To your right is a dark cave.')
  print_pause('In your hand you hold your trusty (not very effective) dagger.\n')
  print_pause('Enter 1 to knock on the door of the house.')
  print_pause('Enter 2 to peer into the cave.')

def house_path(items):
  print_pause("You approach the door of the house.")
  if "Sword of Ogoroth" in items:
    print_pause("You are about to knock when the door opens and out steps a " + foe + ".")
    print_pause("Eep! This is the " + foe + "'s house!")
    print_pause("The " + foe + " attacks you!")
    newtoys_path(items)
  else:
    print_pause("You are about to knock when the door opens and out steps a " + foe + ".")
    print_pause("Eep! This is the " + foe + "'s house!")
    print_pause("The " + foe + " attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    daggers_path(items)

def cave_path(items):
  print_pause("You peer cautiously into the cave.")
  if "Sword of Ogoroth" in items:
    print_pause("You've been here before, and gotten all the good stuff.")
    print_pause("It just an empty cave now.")
    print_pause("You walk back out to the field.")
    pick_path(items)
  else:
   print_pause('It turns out to be only a very small cave.')
   print_pause('Your eyes catches a glint of metal behind a rock.')
   print_pause('You have found the magical Sword of Ogoroth!')
   print_pause('You discard your silly old dagger and take the sword with you.')
   print_pause('You walk back out to the field.\n')
   items.append("Sword of Ogoroth")
   pick_path(items)

def daggers_path(items):
  response = input('Would you like to [1] fight or [2] run away?\n')
  if '1' in response:
    print_pause('You do your best...')
    print_pause('but your dagger is no match for the ' + foe + '.')
    print_pause('You have been defeated.')
  elif '2' in response:
    print("Time to smell the flower and... Back to the field!\n")
    pick_path(items)
  else:
    daggers_path(items)

def newtoys_path(items):
  response = input('Would you like to [1] fight or [2] run away?\n')
  if '1' in response:
    print_pause("As the " + foe + " moves to attack, you unsheath your new sword.") 
    print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
    print_pause("But the " + foe + " takes one look at your shiny new toy and runs away!")
    print_pause("You have rid the town of the " + foe + ". You are victorious!")
  elif '2' in response:
    print("Doubting the shiny sword already? Back to the field!\n")
    pick_path(items)
  else:
    newtoys_path(items)

def pick_path(items):
  print_pause("What would you like to do?")
  response = input("(Please choose 1 or 2.)\n")
  if response == '1':
    house_path(items)
  elif response == '2':
    cave_path(items)
  else:
    pick_path(items)

def again():
  response = input("Would you like to play again? (y/n)\n")
  if response == 'n':
    print_pause("Thank you for playing! See you next time.")
  elif response == 'y':
    play_game()
  else:
    again()

def play_game():
  items = []
  intro()
  pick_path(items)
  again()

play_game()