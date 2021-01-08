# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("hello their future coder! before we move on with THE CODEING EXPERIENCE!tm. please enter your name.\n")
print("hello, " + name + ". welcome too THE CODEING EXPERIENCE!tm. a state of the art simulator of what its like too be a coder!")
print("before we start you must turn on your computer.")
print("whould you like too turn on your computer?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("whould you like too turn on your computer?\nyes/no\n")
    if response == "yes":
        print("You boot up your computer and open up python but OH NO! your program crashed. again. who do you go too in your time of need? \n")
    elif response == "no":
        print("then why are you here? you know what just, game over " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# part 1 crash
response = ""
while response not in directions:
    print("By the water cooler is Ron (the IT guy).")
    print("in his office their is your boss, Mr Muffins(the boss).")
    print("on your right in the next cubicle is jareld (jareld).")
    print("or you can fix it your self.\n")
    response = input("What do you do?\n/R/M/J/me\n")
    if response == "R":
        print("ron helps you with your computer and manages too fix it " ".")
        print("You open up your logs and pick your project souls of life thats half 3. you start working on the code when all of a suden the head coder nabe gewell walks up too you and says")
        print("hey " + name + " I dont mean too troble you or anything but can you add a little fan service too the game we need too get atleast a 9 on metacritic")
    elif response == "M":
        print("Mr Muffins yells at you for not working and just makes ron fix it.\n")
        print("You open up your logs and pick your project souls of life thats half 3. you start working on the code when all of a suden the head coder nabe gewell walks up too you and says")
        print("hey " + name + " I dont mean too troble you or anything but can you add a little fan service too the game we need too get atleast a 9 on metacritic")
        response = ""
        while response not in directions:
          print("will you add fanservice?")
    response = input("yes/no")
  elif response == "J":
          print("Jareld stares at your for an uncomfortable amount of time whist breathing heavily. you stare at your compoter for the rest of the day and get nothing done.")
      print("CONGRATS, YOU HAVE UNLOCKED THE PROCASTINATOR ENDING! (ending 1)")
      quit()
    elif response == "me":
        print("You fail so hard at fixing the computer that you cause it too breack down and explode! you die instantly.")
        print("CONGRATS YOU HAVE UNLOCKED THE HEVANLY CODER ENDING! (ending 2)")
        quit()
    else:
        print("I didn't understand that.\n")

# part 2 fanservice
response = ""
while response not in directions:
    print("will you add fanservice?")
    response = input("yes/no")