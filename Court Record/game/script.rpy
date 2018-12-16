# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define d = Character("Dog")
define m = Character("Me")
define s = Character("Mr. Sun")


screen sun_n_friends:
    imagebutton:
        xpos 1000
        ypos 10
        idle "mr_sun_0.png"
        hover "mr_sun_1.png"
        action Jump ('sun')

    imagebutton:
        xpos 200
        ypos 200
        idle "ladder.gif"
        hover "ladder_1.png"
        action ShowMenu("court_record")

    imagebutton:
        xpos 800
        ypos 400
        idle "dog.png"
        hover "dog_1.png"
        action Jump ('dog')

    imagebutton:
        xpos 90
        ypos 500
        idle "ball_0.png"
        hover "ball_1.png"
        action Jump ('ball')


# The game starts here.

label start:

#declaring evidence variables. the descriptions are done separately so you can have multi-line
    $ info_sun = ["Ironically, he's a pretty cool guy"]
    $ info_ball = ["BALL!!"]
    $ info_dog = ["Woof woof", "Arf arf", "Bark bork"]
    $ info_eileen = ["She'll be helping us out today."]
    $ info_ladder = ["YOU'RE NOT MY REAL LADDER!!"]


    # short name, full name, occupation, info, base
    $ p_eileen =  profile("Eileen", "Eileen", "Assistant", info_eileen, "eileen")
    $ p_dog = profile("Dog", "Dogger von Doggenstein", "Dog", info_dog, "dog")
    $ p_sun = profile("Sun", "The Sun", "The Sun", info_sun, "mr_sun")

    #name, info, base
    $ e_ball = evidence("Ball", info_ball, "ball")
    $ e_ladder = evidence("Stepladder", info_ladder, "ladder")

    #you cannot present to anyone at this time
    $ present = [False]
    $ npc = False
    $ evidence_type = "profiles"
    $ current = ""

    $ my_evidence = [e_ball, e_ladder]
    $ my_profiles = [p_eileen, p_dog, p_sun]

    scene lovely_background

    call screen sun_n_friends


label sun:

    $ present = [True, "sun"]
    $ sun = currentChar("sun", [e_ladder, p_eileen, p_sun])
    m "Hello, Mr. Sun"
    s "HELLO"
    $ npc = currentChar("sun", ["e_ladder"])

    call screen sun_n_friends


label dog:
    s "dog"
    call screen sun_n_friends

label ball:
    s "ball"
    call screen sun_n_friends


label sun_e_ladder:
    s "with the e"

label sun_ladder:
    s "without the e"

label sun_default:
    s "sun don't care"

    return
