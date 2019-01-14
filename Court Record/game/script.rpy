# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define d = Character("Dog")
define m = Character("Tuscon Rong")
define m2 = Character("Tucson Rong", what_color='#add8e6')
define s = Character("Mr. Sun")
define n = Character(None)

define picked_up_ball = False
define seen_ladder = False
define threw_ball = False

screen sun_n_friends:
    # nobody to present to on this screen
    imagebutton:
        xpos 10
        ypos 10
        auto "mr_sun_%s.png"
        action Jump ('sun')

    imagebutton:
        xpos 200
        ypos 200
        auto "ladder_%s.png"
        if seen_ladder == False:
            action Jump ('ladder')
        else:
            action Jump ('seenladder')

    imagebutton:
        xpos 800
        ypos 400
        auto "dog_%s.png"
        action Jump ('dog')

    if picked_up_ball == False:
        imagebutton:
            xpos 90
            ypos 500
            idle "ball_0.png"
            hover "ball_hover.png"
            action Jump ('ball')

 
# The game starts here.



label start:
    # This demo contains the following evidence:
        # PROFILES: Mr. Sun, Eileen, Dog, Tuscon Wrong, some random profiles added to show the second screen
        # EVIDENCE: Attorney's badge, ball, stepladder

    # I've pulled out the multi-line evidence descriptions for the sake of readability
    # That's not necessary, but make sure that the info section is formatted as a list even if it's only one string
    $ info_sun = ["This is the sun. Yeah, THE sun.", "Ironically, he's a pretty cool guy"]
    $ info_ball = ["BALL!!", "(It's just a ball)"]
    $ info_dog = ["Woof woof", "Arf arf", "Bark bork"]
    $ info_badge = ["This is my attorney's badge.", "It's my proof of lawyerhood."]

    # Here are the profiles. They can be customized over in court_record.py 
        # short name, full name, occupation, info, base name
    $ p_eileen =  profile("Eileen", "Eileen", "Assistant", ["She'll be helping us out today."], "eileen")
    $ p_dog = profile("Dog", "Baroness Doggetta von Pupperstein", "Dog", info_dog, "dog")
    $ p_mr_sun = profile("Sun", "The Sun", "The Sun", info_sun, "mr_sun")
    $ p_tucson = profile("Tucson", "Tucson Rong", "Defense Attorney", ["This is me."], "tucson")

    # more profiles to show multiple evidence pages
    $ mikan = profile("Clementine", "Clementine Wormwood", "Former Assistant", ["This is my former assistant.", "She's a bit clumsy, but her heart is in the right place.", "I'm sure she'd never kill anyone!"], "mikan")
    $ kuzu = profile("BB", "Boss Baby", "Yakuza", ["The yakuza is recruiting younger and younger these days.", "They're worse than the prosecution office."], "kuzu")
    $ ibuki = profile("Josie", "Josie Jem", "Pop Star", ["A sweet girl full of energy and heart.", "I'm looking forward to seeing her up on stage."], "ibuki")
    $ sonia = profile("Teena", "Teena Spi'rhit", "Princess", ["The elegant princess of Neh'vermind."], "sonia")
    $ teruteru = profile("Terry", "Terry Yaki", "Chef", ["He's weird, but you can't hate his cooking." "Seriously, this guy makes the best tempura in town"], "teruteru")   
    $ gundam = profile("Simon", "Simon Blackquill", "Prosecutor/Prisoner", ["Age: 28", "Gender: Male", "A skilled prosecutor known as the Twisted Samurai"], "gundam")
    $ akane = profile("Pam", "Final Pam", "Athlete", ["I WILL FIX THE BABY"], "akane")

    #And here's the evidence:
        #name, info, base name
    $ e_ball = evidence("Ball", info_ball, "ball")
    $ e_ladder = evidence("Stepladder", ["YOU'RE NOT MY REAL LADDER!!"], "ladder")
    $ e_badge = evidence("Attorney's Badge", info_badge, "badge")

    # You can present evidence to NPCs. They don't respond to everything. Here's where you set the evidence they are interested in talking about
    # note that these lists refer to whatever you've set as the evidence's base names 
    # each of these corresponds to a label below
    $ sunlist = ["ladder", "ball", "dog", "eileen", "tucson", "badge", "mr_sun"]
    $ doglist = ["ball", "badge", "dog", "tucson"]
    $ eileenlist = ["eileen", "badge", "tucson"]

    # n "Monday, 8:25 AM. Year: 199X. Location: Persons Park" (what_color="#003300")
    # m "My name is Tuscon Rong. I'm a defense attorney and I'm in big trouble - my assistant has been arrested for murder!"
    # m "Thankfully, the agency has sent me a replacement. I won't let another assistant go to jail!"
    # m "Fourth time's the charm, right?"
    # e "I'm here."

    # the items you start out with
    $ my_evidence = [e_badge]
    $ my_profiles = [p_tucson, p_eileen, p_dog]

    # your assistant ("assistant" button goes to a label of the same name)
    $ assistant = "eileen"



label park:
    #the buttons in the upper-right-hand corner
    show screen evidence_menu

    #this tells the evidence screen where to go when it closes
    $ current_scene = "park"

    # There's nobody to present to on this screen
    $ npc = False

    scene lovely_background

    call screen sun_n_friends


label sun:
    $ npc = currentChar("sun", sunlist)
    menu:
        "Sun":
            show tucson at left
            m "What's up, Sun?"
            show sun at center
            s "ME. HA HA HA"
        "Ball" if threw_ball == True:
            show sun at center
            s "THAT DOG LOVES BALLS."
            show tucson at left
            m "Too much! She won't drop it." 
            s "HERE'S ANOTHER ONE"
            $ my_evidence.append(e_ball)
            n "A fresh new ball added to the Court Record"
        "Never mind":
            pass
    jump park


label dog:
    $ npc = currentChar("dog", doglist)
    m2 "(The dog is barking... but thankfully, I can speak dog!)"
    menu:
        "BARK! WOOF, BARK! (What's wrong, girl?)":    
            show dog at right
            d "BOOF! (BALL?)"
            m "She seems to want something..."
        "ARF ARF *PANT* (Who's a good girl?)":
            d "???"
            m2 "(She doesn't know... I'll have to show her some evidence!)"
    jump park

label ball:
    m "This is a nice ball. I'll pick it up just in case it's important."
    n "Ball added to Court Record."
    $ picked_up_ball = True
    $ my_evidence.append(e_ball)    
    jump park

label ladder:
    $ seen_ladder = True
    m "(I came to this park last night and surreptitiously placed this stepladder in order to fulfill my long-time dream: Having a ladder-vs-stepladder verbal debate with my assistant!)"
    m "*ahem*"
    m "Say, Eileen... what would you call this object here?"
    e "You mean the stepladder?"
    m "Aha! So you think it's a stepladder! But what if I said it's just a ladder?"
    e "I would agree."
    m "BUT IF WE EXAMINE THE FUNCTION OF THE DEVICE- huh?"
    e "A stepladder is a type of ladder. You could refer to it either way."
    e "I am a bit curious as to why it's been set up here in the middle of this park, though."
    m "Never mind... *grumble, mumble*"
    m "(I'll add it to the Court Record so I remember to come pick it up again later.)"
    n "Stepladder added to Court Record"
    $ my_evidence.append(e_ladder)
    jump park

label seenladder:
    m "Ladder. Stepladder. The eternal question."
    e "...?"
    jump park


# The sun's reactions to evidence
label sun_ladder:
    s "EVEN WITH THAT LADDER, YOU CAN'T REACH ME."
    m "But I can dream, Mr. Sun. I can dream."
    jump park

label sun_eileen:
    s "HELLO THERE"
    e "Hello, Mr. Sun."
    jump park

label sun_ball:
    jump park

label sun_dog:
    jump park

label sun_badge:
    s "FLASHING YOUR BADGE AROUND AS USUAL, EH TUCSON?"
    m "You know it!"
    jump park

label sun_default:
    s "I AM THE ALMIGTY SUN. BOW TO MY RESPLENDENCE."
    m "(It seems like he doesn't have anything to say about this.)"
    jump park

# consult Eileen
label eileen:
    $ npc = currentChar("eileen", eileenlist)
    menu:
        "Eileen":
            jump park
        "The Court Record":
            jump park
        "The case":
            jump park
        "That's all":
            jump park

label eileen_default:
    e "There are a number of inventory screens that can be used in Ren'py games, but this one's unique feature is the ability to present evidence to NPCs."
    e "If they don't have anything to say about the evidence, it'll go to a default response, like this one."
    t "In other words... you don't have anything to say about it."
    jump park

label eileen_badge:
    jump park

label eileen_tucson:
    jump park

label eileen_eileen:
    jump park

# The dog's reactions to evidence

label dog_ball:
    d "BALL!! THROW THE BALL!!"
    m "D'aww, I can't say no to that face. Do you want to throw the ball, Eileen?"
    e "Sure."
    n "Eileen throws the ball and the dog runs to fetch it. She returns with the ball in her mouth, tail wagging."
    d "THROW BALL!!"
    e "Drop it."
    d "NO DROP... ONLY THROW!!"
    $ my_evidence.remove(e_ball)
    m "(I don't think we're getting that back...)"
    $ threw_ball = True
    jump park

label dog_dog:
    jump park

label dog_tucson:
    jump park

label dog_badge:
    d "Shiny!"
    m "Thanks!!"
    e "Are you showing your badge to a dog...?"
    m "I show my badge to everyone I meet as a matter of principle... because I'm a lawyer."
    e "Actually, I've been wondering... is that a real lawyer's badge?"
    m "*gulp* Wh-what do you mean?"
    e "I feel like Ive seen it somewhere else..."
    m "*double gulp* You've probably just seen a lot of defense attorneys."
    e "And doesn't the lettering seem a bit shaky? It looks like it was written in marker."
    m "That's a common mistake. Here, I'll amend the Court Record to prove it."
    $ e_badge.change(["This is my completely authentic lawyer's badge.", "It's definitely a real badge and not a toy from a vending machine that I wrote on with a Sharpie."])
    jump park

label dog_default:
    d "*sniff, sniff*"
    m "Hmm, she doesn't seem interested in this."
    show eileen vhappy
    e "She's still a good girl, though."
    n "We spend some time petting the dog."
    jump park


