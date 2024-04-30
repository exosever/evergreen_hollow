#Text based RPG project by Joshua Harrison aka SeverX

import re
import random
import os

#Function to clear console
def clear():
  os.system("clear")
  os.system("cls")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Evergreen Hollow, your journey is just beginning.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("If you see a >>>, press 'ENTER' to continue.")
print("If you see a [-], this requires an input.")
print()
input("Press 'ENTER' to remember..... >>>")
print()
clear()

#Variable to run the character creation continuously until player chooses to continue
creation=True
restart=True
while restart:
  #Name Choice, beginning of Character Creation
  while creation:
    input("You wake up in a haze, unsure of where you are. The first question that comes to your mind is.... >>>")
    while True:
      char_name=input("What is your name? [-] ")
      if len(char_name) > 12:
        print()
        print ("That doesn't seem right... I think it was shorter...")
        print ("~~~~12 Character Maximum~~~")
      else:
        print()
        clear()
        break

  #Class list
    class_list = ["Fighter","Wizard","Thief","Barbarian"]
    class_list_l=[class_l.lower() for class_l in class_list]

    input(f"That's right.... {char_name}, but why are you here? What is your profession? >>>")
    print("Choose 1: " + ", ".join(class_list))

  #Class choice

    while True:
      char_class=input("I am a [-] ").lower()
      char_class=re.sub(r'[^a-zA-Z]', '', char_class)
      if class_list_l.count(char_class) != 1:
        print()
        print("~~~~You have chosen an incorrect profession, please try again.~~~~")
        print()
      else:
        print()
        input("Of course! You're a " + char_class + "!" " >>>")
        clear()
        break

  #Make char_class formatted correctly after submission
    char_class = char_class.capitalize()

  #Race list
    race_list = ["Orc", "Elf", "Human", "Dwarf"]
    race_list_l = [race.lower() for race in race_list]

  #Race choice
    print()
    input("You look around and see a mirror, what do you see in the reflection? >>>")
    print("Choose 1: " + ", ".join(race_list))

    while True:
      char_race=input("I see a(n)... [-] ").lower()
      char_race=re.sub(r'[^a-zA-Z]','', char_race)
      if race_list_l.count(char_race) != 1:
        print()
        print("~~~~You have chosen an incorrect race, please try again.~~~~")
        print()
      else:
        print()
        input("Looking back at you in the mirror.... you see a(n) " + char_race.capitalize() + ". " + ">>>")
        clear()
        break

  #Momento list
    momento_list= ["Necklace", "Knife", "Handkerchief", "Opal"]
    momento_list_l = [momento.lower() for momento in momento_list]

  #Momento choice
    print()
    input("You look away from the mirror, and as your eyes adjust to the dim light, you see a table... >>>")
    input("On that table you see a necklace... >>>")
    input("A knife... >>>")
    input("An embroidered handkerchief... >>>")
    input("And an opal... >>>")
    print()
    print("You reach out to grab one... which do you pick? ")
    print("Choose 1: " + ", ".join(momento_list))

    while True:
      char_momento=input("I grab the... [-] ").lower()
      char_momento=re.sub(r'[^a-zA-Z]','', char_momento)
      if momento_list_l.count(char_momento) != 1:
        print()
        print("~~~~You have chosen an incorrect momento, please try again.~~~~")
        print()
      else:
        print()
        input("Quickly, you grab the " + char_momento + " and turn towards the door. >>>")
        clear()
        break
    char_momento = char_momento.capitalize()

  #Equipment list
    equipment_list=["Bow", "Dagger", "Sword and Shield", "Longsword", "Battle Axe", "Flail", "Staff", "Grimoire"]

  #Equipment choice
    input("As you hurry towards the door, you see weapons lying on each side of it... >>>")
    input("You take a moment to inspect them... >>>")
    clear()

    while True:
      if char_class == class_list[2]:
        print(f"On the left, you see a {equipment_list[0]}")
        print(f"On the right, you see a {equipment_list[1]}")
        char_weapon=input("Do you grab the weapon to your /left/, or to your /right/? [-] ").lower()
        if char_weapon == "left":
          char_weapon = equipment_list[0]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        elif char_weapon == "right":
          char_weapon = equipment_list[1]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        else:
          print("~~~Please respond left or right~~~")

      elif char_class == class_list[0]:
        print(f"On the left, you see a {equipment_list[2]}")
        print(f"On the right, you see a {equipment_list[3]}")
        char_weapon=input("Do you grab the weapon to your /left/, or to your /right/? [-] ").lower()
        if char_weapon == "left":
          char_weapon = equipment_list[2]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        elif char_weapon == "right":
          char_weapon = equipment_list[3]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        else:
          print("~~~Please respond left or right~~~")

      elif char_class == class_list[3]:
        print(f"On the left you see a large {equipment_list[4]}")
        print(f"On the right, you see a {equipment_list[5]}")
        char_weapon=input("Do you grab the weapon to your /left/, or to your /right/? [-] ").lower()
        if char_weapon == "left":
          char_weapon = equipment_list[4]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        elif char_weapon == "right":
          char_weapon = equipment_list[5]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        else:
          print("~~~Please respond left or right~~~")

      elif char_class == class_list[1]:
        print(f"On the left, you see a magical {equipment_list[6]}")
        print(f"On the right, you see a {equipment_list[7]}")
        char_weapon=input("Do you grab the weapon to your /left/, or to your /right/? [-] ").lower()
        if char_weapon == "left":
          char_weapon = equipment_list[6]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        elif char_weapon == "right":
          char_weapon = equipment_list[7]
          input(f"You grab the {char_weapon}, and it feels natural in yours hands... >>>")
          clear()
          break
        else:
          print("~~~Please respond left or right~~~")

  #Final check, continue with this character, or restart?
    print()
    input(f"With your {char_weapon} in hand, you walk into the doorway... >>>")
    input("You glance back and take one last look at the room you awoke from... >>>")
    print()
    print(f"Your name is {char_name}, a(n) {char_race} {char_class}. Is this truly who you remember?")
    while True:
      user_input = input("Enter (Y/N) [-] ").lower()
      if user_input == "n":
        print()
        print("You try to remember again...")
        print()
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break
      elif user_input == "y":
        input("You take a step outside... >>>")
        creation = False
        clear()
        break
      else:
        print("~~~Please respond Y or N~~~")
        print()

  #Set up inventory
  char_inv=[char_momento, char_weapon]
  def inventory():
    print("Your inventory contains: " + ', '.join(char_inv))

  #Variable to remove momento from inventory
  momento_remove=char_inv.index(char_momento)

  #Stat values
  hp_lower = 10
  hp_upper = 10

  #For Fighter
  stamina_lower = 50
  stamina_upper = 50

  #For Wizard
  mana_lower = 20
  mana_upper = 20

  #For Thief
  wits_lower = 30
  wits_upper = 30

  #For Barbarian
  rage_lower = 40
  rage_upper = 40

  #Introduce HUD :## format is for static string length.

  if char_class == class_list[0]:
    def hud():
      print(" " + "_" * 78)
      print("<" + " " * 10 + "Name: " + f"{char_name:13}" + "Class: " + f"{char_class.capitalize():16}" + "Weapon: " + f"{char_weapon:18}" ">")
      print(f"|" + " " * 10 + "HP: " + f"{hp_lower:2}" + "/" + f"{hp_upper:2}" + " " * 10 + "Stamina: " + f"{stamina_lower:2}" + "/" + f"{stamina_upper:2}" + " " * 35 + "|")
      print("<" + "=" * 78 + ">")

  elif char_class == class_list[1]:
    def hud():
      print("," + "~" * 78 + ",")
      print("*" + " " * 10 + "Name: " + f"{char_name:13}" + "Class: " + f"{char_class.capitalize():16}" + "Weapon: " + f"{char_weapon:18}" "*")
      print("|" + " " * 10 + "HP: " + f"{hp_lower:2}" + "/" + f"{hp_upper:2}" + " " * 10 + "Mana: " + f"{mana_lower:2}" + "/" + f"{mana_upper:2}" + " " * 38 + "|")
      print("*" + "-^" * 39 + "*")
    
  elif char_class == class_list[2]:
    def hud():
      print(" " + "." * 78)
      print(":" + " " * 10 + "Name: " + f"{char_name:13}" + "Class: " + f"{char_class.capitalize():16}" + "Weapon: " + f"{char_weapon:18}" ":")
      print(":" + " " * 10 + "HP: " + f"{hp_lower:2}" + "/" + f"{hp_upper:2}" + " " * 10 + "Wits: " + f"{wits_lower:2}" + "/" + f"{wits_upper:2}" + " " * 38 + ":")
      print("'" + "-" * 78 + "'")

  elif char_class == class_list[3]:
    def hud():
      print(" " * 2 + "_-" * 37 + "_")
      print(" " + "/" + " " * 9 + "Name: " + f"{char_name:13}" + "Class: " + f"{char_class.capitalize():16}" + "Weapon: " + f"{char_weapon:16}" "\\")
      print("/" + " " * 10 + "HP: " + f"{hp_lower:2}" + "/" + f"{hp_upper:2}" + " " * 10 + "Rage: " + f"{rage_lower:2}" + "/" + f"{rage_upper:2}" + " " * 37 + "\\")
      print("^" + "-" * 77 + "^")

  hud()

  #Function to clear output and display updated HUD
  def refresh():
    clear()
    hud()

  #Game start
  input("You open the door and begin to take a step outside, by the sudden sunlight causes you to pause... >>>")
  input("You raise your arm to try and block the sun, to let your eyes adjust and take in your surrounds. >>>")
  input("The building you came from is just a small shack in the woods, with no surrounding buildings... >>>")
  print()
  input("You take a few minutes to collect yourself, and to inspect the area... >>>")
  inventory()
  input(">>>")
  refresh()

  #Sequence with necklace momento interaction
  input("There are no signs of anyone being here in a very long time... >>>")
  input("And the only thing here besides the shack is a well. >>>")
  while True:
    user_input = input("Do you inspect the well? (Y/N) [-] ").lower()
    print()
    if user_input == "y":
      print("You approach the well, it is old and there are missing stones on it's walls.")
      input("From what you can tell, there may be water still in the well... >>>")
      print()
      if char_inv.count(momento_list[0]) == 1:
        print("As you lean over the ledge, the clasp on your "f"{char_momento}"" comes undone and it falls down the well.")
        input("You can't quite see the bottom, but the splash leads you to believe it is deeper than you think... >>>")
        input("-1 "f"{char_momento}"" >>>")
        char_inv.pop(momento_remove)
        break
      else:
        print("Upon inspection, the well has not been used in what seems like years...")
        input("You can't see the bottom, or tell if there's any water left. >>>")
        break
    elif user_input == "n":
      input("Now is not the time, you must find out where you are. >>>")
      break
    else:
      input("Please type 'y' or 'n'")
  refresh()

  #Sequence with Handkerchief momento interaction
  direction_l=["north", "east", "south,", "west"]
  input("It must be the evening, as you have noticed the sun moving closer to the tree line... >>>")
  input("You decide it is best to go and find a village... >>>")
  input("Without any clues, you decide to pick a direction... >>>")
  refresh()

  while True:
    print("Choose 1: North, East, South, or West")
    direction=input("You decide to go [-] ").lower()
    if direction_l.count(direction) == 1:
      print()
      input("You decide to take a risk, and head towards what you believe to be " f"{direction}"" >>>")
      if char_inv.count(momento_list[2]) == 1:
        input("As you walk, you take a look at your "f"{char_momento}"" and notice something... >>>")
        input("It seems there's a map on it! You take a moment to look at the distinguishing features on the map... >>>")
        input("After studying it for some time, a sudden gust of wind carries the "f"{char_momento}"" away... >>>")
        input("-1 "f"{char_momento}"" >>>")
        char_inv.pop(momento_remove)
        break
      else:
        break
    else:
      print("~~~Remember, you can only go North, East, South, or West~~~")
      refresh()
  refresh()

  #Sequence with Knife momento interaction
  input("As you continue forward, the sun continues to set behind the tree line... >>>")
  input("Before you realize it, night has started to fall... >>>")
  input("With the falling night, comes a chill that runs through to your bones... >>>")
  print()
  if char_inv.count(momento_list[1]) == 1:
    refresh()
    input("Walking through the encroaching darkness, you stumble over something... >>>")
    input("It seems to be some sort of stone, and upon closer inspection, it's flint! >>>")
    input("You remember your "f"{char_momento}"", and use it to strike the flint! >>>")
    print()
    input("After repeatedly striking the flint over some leaves, you manage to create a small fire to warm yourself. >>>")
    print("But the "f"{char_momento}"" breaks in the attempt.")
    print("-1 "f"{char_momento}")
    char_inv.pop(momento_remove)
    input()
    refresh()
  refresh()

  #Transition to NPC sequence
  input("As time passes, your eyes catch the errie glow of what seems like light in the distance... >>>")
  print("Without hesitation, you hurry your way in that direction with the hope that you may find")
  input("Someone else out here with you... >>>")
  refresh()

  #NPC dialogue with specific responses from character creation
  input("You see a strange man in the distance >>>")
  input("As you approach, you can tell from his clothes that he is a traveller... >>>")
  input("He notices you get closer, and speaks to you... >>>")
  refresh()

  input("'Ah... come closer friend... the night is dark and my eyes are old...' >>>")
  print()
  if char_race.count(race_list[0]) == 1:
    print("'Well well... an "f"{char_race.capitalize()}" " I haven't seen one of your kind in many years...'")
    input("Come, sit by the fire with me. I have fresh game and good ale to share... >>>")
  elif char_race.count(race_list[1]) == 1:
    print("'Do my old eyes decieve me? An " f"{char_race.capitalize()}""! I thought you folk left decades ago...'")
    input("'Come, sit with me a while... If you have tales to share, would you humor this old man?' >>>")
  elif char_race.count(race_list[2]) == 1:
    print("'Well met friend! Another "f"{char_race.capitalize()}"" out here in the wilderness?'")
    input("'These are dangerous parts my friend, what brings you out here so late at night? >>>'")
  elif char_race.count(race_list[3]) == 1:
    print("'A child? No... not with such a glorious beard! You must be a "f"{char_race.capitalize()}""!'")
    input("'Please come have a drink! The night is cold, but the ale warms you faster than the fire!' >>>")
  refresh()


  input("A few hours pass... while you and the traveler rest near the fire... >>>")
  input("Through your conversation you have learned that you are currently in the Evergreen Hollow. >>>")
  input("An uninhabited forest, except for those who do not desire to be found. >>>")
  input("He does not question why you are here, and you reciprocate... >>>")
  refresh()

  #Sequence with Opal momento interaction
  if char_inv.count(momento_list[3]) == 1:
    input("While bending over to stoke the fire, the small "f"{char_momento}"" falls out of your pocket... >>>")
    input("The stanger's eyes grow wide, and before you realize it he hurriedly picks it up off the ground. >>>")
    input("'Wh...where... where did you get this?!' He says in an exasperated, almost desperate tone... >>>")
    print("-1 "f"{char_momento}")
    char_inv.pop(momento_remove)
    print()
    input("But before you can respond... >>>")
    refresh()

  #First combat - Be sure to introduce a random.randint function to combat, take into account the weapon chosen?

  input("Seemingly out of nowhere... a group of beings surround the campfire... >>>")
  input("Almost instinctually, you grasp your "f"{char_weapon}""... >>>")
  input("You open your mouth to speak, but are interrupted with screams as they rush toward you ... >>>")
  print()

  enemy_hp = 10

  #Fighter
  if char_class == class_list[0]:
    print("~~~You can either Attack or Defend~~~")
    print("~~~Attacking costs 10 Stamina~~~")
    input("~~~Defending restores 20 Stamina, and has a chance to avoid damage~~~ >>>")
    while enemy_hp >0 or hp_lower >0:
      refresh()
      if hp_lower == 0:
        break
      #Victory sequence to outro
      elif enemy_hp == 0:
        input("Feeling victorious, you turn around swifly, only to find a club swinging right at you... >>>")
        break
      else:
        action = input("Attack or Defend? Enemy HP: "f"{enemy_hp}"" [-]").lower()
        if action == "attack":
          input("You attack with your "f"{char_weapon}"", costing 10 stamina. >>>")
          stamina_lower -= 10
          attack = random.randint(1,3)
          if attack >1:
            damage = random.randint(1,2)
            input("You deal "f"{damage}"" damage. >>>")
            enemy_hp -= damage
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print()
              print("The enemy swings....")
              input("You take "f"{enemy_damage}"" damage. >>>")
              hp_lower -= enemy_damage
            else:
              input("The enemy misses... >>>")
          elif attack == 1:
            input("But your attack misses... >>>")
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print("You take "f"{enemy_damage}"" damage.")
              hp_lower -= enemy_damage
        elif action == "defend":
          input("You brace yourself, and restore 20 stamina. >>>")
          stamina_lower += 20
          enemy_attack = random.randint(1,6)
          if enemy_attack >4:
            enemy_damage = random.randint(1,2)
            print()
            input("The enemy swings... >>>")
            input("You take "f"{enemy_damage}"" damage. >>>")
            hp_lower -= enemy_damage
          else:
            input("The enemy misses... >>>")
        else:
          input("Remember, you can only 'Attack' or 'Defend' >>>")



  #Wizard
  elif char_class == class_list[1]:
    print("~~~You can either Attack or Defend~~~")
    print("~~~Attacking costs 4 Mana~~~")
    input("~~~Defending restores 8 Mana, and has a chance to avoid damage~~~ >>>")
    while enemy_hp >0 or hp_lower >0:
      refresh()
      if hp_lower == 0:
        break
      #Victory sequence to outro
      elif enemy_hp == 0:
        input("Feeling victorious, you turn around swifly, only to find a club swinging right at you... >>>")
        break
      else:
        action = input("Attack or Defend? Enemy HP: "f"{enemy_hp}"" [-]").lower()
        if action == "attack":
          input("You attack with your "f"{char_weapon}"", costing 4 mana. >>>")
          mana_lower -= 4
          attack = random.randint(1,3)
          if attack >1:
            damage = random.randint(1,2)
            input("You deal "f"{damage}"" damage. >>>")
            enemy_hp -= damage
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print()
              print("The enemy swings....")
              input("You take "f"{enemy_damage}"" damage. >>>")
              hp_lower -= enemy_damage
            else:
              input("The enemy misses... >>>")
          elif attack == 1:
            input("But your attack misses... >>>")
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print("You take "f"{enemy_damage}"" damage.")
              hp_lower -= enemy_damage
        elif action == "defend":
          input("You brace yourself, and restore 8 mana. >>>")
          mana_lower += 8
          enemy_attack = random.randint(1,6)
          if enemy_attack >4:
            enemy_damage = random.randint(1,2)
            print()
            input("The enemy swings... >>>")
            input("You take "f"{enemy_damage}"" damage. >>>")
            hp_lower -= enemy_damage
          else:
            input("The enemy misses... >>>")
        else:
          input("Remember, you can only 'Attack' or 'Defend' >>>")

  #Thief
  elif char_class == class_list[2]:
    print("~~~You can either Attack or Defend~~~")
    print("~~~Attacking costs 6 Wits~~~")
    input("~~~Defending restores 12 Wits, and has a chance to avoid damage~~~ >>>")
    while enemy_hp >0 or hp_lower >0:
      refresh()
      if hp_lower == 0:
        break
      #Victory sequence to outro
      elif enemy_hp == 0:
        input("Feeling victorious, you turn around swifly, only to find a club swinging right at you... >>>")
        break
      else:
        action = input("Attack or Defend? Enemy HP: "f"{enemy_hp}"" [-]").lower()
        if action == "attack":
          input("You attack with your "f"{char_weapon}"", costing 6 wits. >>>")
          wits_lower -= 6
          attack = random.randint(1,3)
          if attack >1:
            damage = random.randint(1,2)
            input("You deal "f"{damage}"" damage. >>>")
            enemy_hp -= damage
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print()
              print("The enemy swings....")
              input("You take "f"{enemy_damage}"" damage. >>>")
              hp_lower -= enemy_damage
            else:
              input("The enemy misses... >>>")
          elif attack == 1:
            input("But your attack misses... >>>")
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print("You take "f"{enemy_damage}"" damage.")
              hp_lower -= enemy_damage
        elif action == "defend":
          input("You brace yourself, and restore 12 wits. >>>")
          wits_lower += 12
          enemy_attack = random.randint(1,6)
          if enemy_attack >4:
            enemy_damage = random.randint(1,2)
            print()
            input("The enemy swings... >>>")
            input("You take "f"{enemy_damage}"" damage. >>>")
            hp_lower -= enemy_damage
          else:
            input("The enemy misses... >>>")
        else:
          input("Remember, you can only 'Attack' or 'Defend' >>>")

  #Barbarian
  elif char_class == class_list[3]:
    print("~~~You can either Attack or Defend~~~")
    print("~~~Attacking costs 8 Rage~~~")
    input("~~~Defending restores 16 Rage, and has a chance to avoid damage~~~ >>>")
    while enemy_hp >0 or hp_lower >0:
      refresh()
      if hp_lower == 0:
        break
      #Victory sequence to outro
      elif enemy_hp == 0:
        input("Feeling victorious, you turn around swifly, only to find a club swinging right at you... >>>")
        break
      else:
        action = input("Attack or Defend? Enemy HP: "f"{enemy_hp}"" [-]").lower()
        if action == "attack":
          input("You attack with your "f"{char_weapon}"", costing 8 rage. >>>")
          rage_lower -= 8
          attack = random.randint(1,3)
          if attack >1:
            damage = random.randint(1,2)
            input("You deal "f"{damage}"" damage. >>>")
            enemy_hp -= damage
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print()
              print("The enemy swings....")
              input("You take "f"{enemy_damage}"" damage. >>>")
              hp_lower -= enemy_damage
            else:
              input("The enemy misses... >>>")
          elif attack == 1:
            input("But your attack misses... >>>")
            enemy_attack = random.randint(1,4)
            if enemy_attack >2:
              enemy_damage = random.randint(1,2)
              print("You take "f"{enemy_damage}"" damage.")
              hp_lower -= enemy_damage
        elif action == "defend":
          input("You brace yourself, and restore 16 rage. >>>")
          rage_lower += 16
          enemy_attack = random.randint(1,6)
          if enemy_attack >4:
            enemy_damage = random.randint(1,2)
            print()
            input("The enemy swings... >>>")
            input("You take "f"{enemy_damage}"" damage. >>>")
            hp_lower -= enemy_damage
          else:
            input("The enemy misses... >>>")
        else:
          input("Remember, you can only 'Attack' or 'Defend' >>>")

  #End of game sequence
  os.system("clear")
  os.system("cls")
  input("Suddenly... your vision grows dim... your mind becomes clouded and your thoughts eratic... >>>")
  input("You feel yourself falling forward, but when you try to throw your arms in front to catch you... >>>")
  input("Your body begins to feel weightless... >>>")
  input("You feel your mind slipping away... you no longer seem to recall where you are... >>>")
  input("Why are you here? >>>")
  input("What were you doing? >>>")
  input("Who even are you? >>>")
  input("Your mind races with these questions... but the questions escape as soon as they come... >>>")
  input("Little by little... less thoughts fill your mind, and are replaced with just an emptiness... >>>")
  input(">>>")
  input("Only one thought remains... >>>")
  os.system("clear")
  os.system("cls")

  #Replay sequence
  while True:
    print("Do you wish to remember?")
    restart=input("Y/N [-]").lower()
    if restart == "y":
      refresh()
      break
    elif restart == "n":
      replay = False
      break
    else:
      print("Please respond Y or N.")
      print()
    break
  break
