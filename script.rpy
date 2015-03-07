
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define y = Character("[name]", color="#c8ffc8")
define d = Character("Default")


# The game starts here.
label start:
    
    # add in char selection later
    
    python:
        name = renpy.input("Enter your name: ")
        i = renpy.input("So, your name is... [y]?")
        
        # turn into a while false loop?
        if i == "no":
            y = renpy.input("Enter your name: ")
        else:
            pass
    
    # comment based on the season
    
    "A gentle breeze caresses the dry, brittle air respite from the tendrils of enduring heat ever since dryseason began."
    
    "You can still remember the events of a few days ago. Engraved, fresh in your mind...."
    
    d "hi!!! [y]"
    
    d "You've created a new Ren'Py game."

    d "Once you add a story, pictures, and music, you can release it to the world!"

    return
