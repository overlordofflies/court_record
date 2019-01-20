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
define dangans = False

# our main scene for this demo
screen sun_n_friends:
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

 


label start:
    # Here's where I'll declare my evidence

    # I've pulled out the multi-line evidence descriptions for the sake of readability
    # That's not necessary, but do make sure that the info section is formatted as a list even if it's only one string
    $ info_sun = ["This is the sun. Yeah, THE sun.", "Ironically, he's a pretty cool guy"]
    $ info_ball = ["BALL!!", "(It's just a ball)"]
    $ info_dog = ["Woof woof", "Arf arf", "Bark bork"]
    $ info_badge = ["This is my attorney's badge.", "It's my proof of lawyerhood."]

    # Here are the profiles. They can be customized over in court_record.rpy 
        # Current format: short name, full name, occupation, info, image base name
    $ p_eileen =  profile("Eileen", "Eileen", "Assistant", ["She'll be helping us out today."], "eileen")
    $ p_dog = profile("Dog", "Baroness Doggetta von Pupperstein", "Dog", info_dog, "dog")
    $ p_mr_sun = profile("Sun", "The Sun", "The Sun", info_sun, "mr_sun")
    $ p_tucson = profile("Tucson", "Tucson Rong", "Defense Attorney", ["This is me."], "tucson")

    # more profiles to show multiple evidence pages
    $ mikan = profile("Clementine", "Clementine Wormwood", "Former Assistant", ["This is my former assistant who was recently accused of murder.", "She's a bit clumsy, but her heart is in the right place.", "I'm sure she'd never hurt anyone!"], "mikan")
    $ kuzu = profile("BB", "Boss Baby", "Yakuza", ["The yakuza is recruiting younger and younger these days.", "They're worse than the prosecution office."], "kuzu")
    $ ibuki = profile("Josie", "Josie Jem", "Pop Star", ["A sweet girl full of energy and heart.", "I haven't heard her music yet, but I love a nice, wholesome pop song.", "I'm looking forward to seeing her up on stage."], "ibuki")
    $ sonia = profile("Teena", "Teena Spi'rhit", "Princess", ["The elegant princess of Neh'vermind.", "", "...Do you think she'd go out with me?"], "sonia")
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
    # each of these corresponds to a label below, ex. dog_badge
    $ sunlist = ["ladder", "ball", "dog", "eileen", "tucson", "badge", "mr_sun"]
    $ doglist = ["ball", "badge", "dog"]
    $ eileenlist = ["eileen", "badge", "tucson"]

    n "Monday, 8:25 AM. Year: 201X. Location: Persons Park" (what_color="#7FFFA9")
    m2 "(My name is Tuscon Rong. I'm a defense attorney and I'm in big trouble - my assistant has been arrested for murder!)"
    m2 "(Thankfully, the agency has sent me a replacement. I won't let another assistant go to jail!)"
    m2 "(Fourth time's the charm, right?)"
    show eileen happy
    e "Good morning. My name's Eileen. I'll be helping you out today."
    hide eileen 
    show tucson
    m "Nice to meet you."
    m "...Wow, it's obvious our art assets weren't created by the same person."
    hide tucson 
    m "I think I'll stay off-screen. That gives a cool 'first person' type of feel, anyway."
    m2 "(That and I only have the one expression...)"
    show eileen concerned
    e "If you say so..."
    show eileen happy
    e "Anyway, let's try out the demo. If you need help, click the 'Assistant' button in the upper-right-hand corner."
    hide eileen with fade

    # the items you start out with
    $ my_evidence = [e_badge]
    $ my_profiles = [p_tucson, p_eileen, p_dog, p_mr_sun]

    # your assistant (the "assistant" button goes to a label of the same name)
    $ assistant = "eileen"



label park:
    scene lovely_background

    #the buttons in the upper-right-hand corner
    show screen evidence_menu

    #this tells the evidence screen where to go when it closes
    $ current_scene = "park"

    # There's nobody to show evidence to on this screen
    $ npc = False

    call screen sun_n_friends


label sun:
    $ npc = currentChar("sun", sunlist)
    show sun
    menu:
        "Sun":
            m "What's up, Sun?"
            s "ME. HA HA HA"
        "Ball" if threw_ball == True:
            s "THAT DOG LOVES BALLS."
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
    show dog
    menu:
        "BARK! WOOF, BARK! (What's wrong, girl?)":    
            d "BOOF! (BALL?)"
            m "She seems to want something..."
        "ARF ARF *PANT* (Who's a good girl?)":
            d "???"
            m2 "(She doesn't know!? I'll have to show her some evidence!)"
    jump park

label ball:
    m "This is a nice ball. I'll pick it up just in case it's important to my murder case."
    n "Ball added to Court Record."
    $ picked_up_ball = True
    $ my_evidence.append(e_ball)    
    jump park

label ladder:
    $ seen_ladder = True
    m "(I came to this park last night and surreptitiously placed this stepladder in order to fulfill my long-time dream: Having a ladder-vs-stepladder verbal debate with my assistant!)"
    m "*ahem*"
    m "Say, Eileen... what would you call this object here?"
    show eileen happy
    e "You mean the stepladder?"
    m "Aha! So you think it's a stepladder! But what if I said it's just a ladder?"
    e "I would agree."
    m "BUT IF WE EXAMINE THE FUNCTION OF THE DEVICE- huh?"
    e "A stepladder is a type of ladder. You could refer to it either way."
    show eileen concerned
    e "I am a bit curious as to why it's been set up here in the middle of this park, though."
    hide eileen with fade
    m "Never mind... *grumble, mumble*"
    m2 "(I'll add it to the Court Record so I remember to come pick it up again later.)"
    $ my_evidence.append(e_ladder)
    n "Stepladder added to Court Record"
    jump park

label seenladder:
    m "Ladder. Stepladder. The eternal question."
    show eileen concerned
    e "...?"
    jump park


# The sun's reactions to evidence
label sun_ladder:
    show sun
    s "EVEN WITH THAT LADDER, YOU CAN'T REACH ME."
    m "But I can dream, Mr. Sun. I can dream."
    jump park

label sun_eileen:
    show sun
    s "I SEE YOU HAVE A NEW ASSISTANT, TUCSON."
    m "This is Eileen. She's helping me get my previous assistant out of jail."
    hide sun
    show eileen happy
    e "Actually, I'm here to help demonstrate the court record."
    m "H-huh? You're really not going to help out in court?"
    e "I can't make any promises. But if there's ever a version of this that includes a trial, I'd be happy to help."
    jump park

label sun_ball:
    show sun
    m "What do you think of this?"
    s "I LIKE IT. IT REMINDS ME OF ME."
    jump park

label sun_dog:
    show sun
    m "Have you seen this dog before?"
    s "IVE SEEN EVERYTHING UNDER THE ME. WHAT ABOUT THE DOG?"
    m "Oh. Nothing, really. I just think she's a good dog."
    s "I AGREE."
    jump park

label sun_badge:
    show sun
    s "FLASHING YOUR BADGE AROUND AS USUAL, EH TUCSON?"
    m "You know it!"
    jump park

label sun_default:
    show sun
    s "I AM THE ALMIGTY SUN. BOW TO MY RESPLENDENCE."
    m2 "(It seems like he doesn't have anything to say about this.)"
    jump park

label sun_tucson:
    show sun
    s "I REMEMBER WHEN YOU WERE JUST A BOY-"
    m "Wow, look at the time! Talk to you later, Mr. Sun!"
    jump park 

# consult Eileen
label eileen:
    show eileen happy
    $ npc = currentChar("eileen", eileenlist)
    menu:
        "How does this work?":
            m "Could you tell me more about this... 'court record' thing?"
            show eileen concerned
            e "That question is a bit concerning from a lawyer..."
            show eileen happy
            e "But I'm happy to explain. This is meant to replicate the feel of the Ace Attorney games."
            e "You collect evidence by clicking on it and interacting with the characters on the scene."
            e "When you speak to a character, a menu pops up with dialogue options. However, you can also choose to present them evidence by selecting that evidence in the Court Record and hitting the 'present' button."
            show eileen vhappy
            e "Why don't you try showing something to me?"            
        "The murder case" if dangans == False:
            $ dangans = True
            m "Sssso, I have this murder case coming up..."
            show eileen concerned
            e "...About that. It seems like the demo doesn't go that far..."
            m "What!? So I'm not going to be able to defend my assistant in court?"            
            show eileen happy
            e "That would seem to be the case, yes. I'm sorry. But I can show you something. Here."
            $ my_profiles.append(mikan)
            $ my_profiles.append(gundam)
            $ my_profiles.append(kuzu)
            $ my_profiles.append(ibuki)
            $ my_profiles.append(sonia)
            $ my_profiles.append(teruteru)
            $ my_profiles.append(akane)
            n "Eileen hands Tucson the files he forgot in the office."
            e "As you can see, if you have more than eight profiles, the court record will have more than one page."
            pass
        "Never mind":
            jump park
    jump eileen

label eileen_default:
    show eileen happy
    e "There are a number of inventory screens that can be used in Ren'py games, but this one's unique feature is the ability to present evidence to NPCs."
    e "If they don't have anything to say about the evidence, it'll go to a default response, like this one."
    m2 "(In other words... you don't have anything to say about it.)"
    jump park

label eileen_badge:
    m "What do you think? It's my lawyer's badge."
    show eileen concerned
    e "Actually, I've been wondering... is that a real lawyer's badge?"
    m "*gulp* Wh-what do you mean?"
    e "I feel like Ive seen that design somewhere else..."
    m "*double gulp* You've probably just seen a lot of defense attorneys."
    e "And doesn't the lettering seem a bit shaky? It looks like it was written in marker."
    m "That's a common misunderstanding. Here, I'll amend the Court Record to prove it."
    $ e_badge.change(["This is my completely authentic lawyer's badge.", "It's definitely a real badge and not a toy from a vending machine that I wrote on with a Sharpie."])    
    jump park

label eileen_tucson:
    m "So I have this photo..."
    show eileen vhappy
    e "You're getting the hang of presenting evidence. Good job, Tucson!"
    m2 "(She seems proud of me. Now I'm too self-conscious to ask if she thinks this is a good photo...)"
    jump park

label eileen_eileen:
    m "Tell me about yourself. If we're going to work together, I want to be friends."
    show eileen happy
    e "Well, I-"
    m "Like what's your favorite Saturday morning children's show?"
    m "Do you prefer burgers or ramen?"
    m "Do you believe in justice, evidence, the truth, or your clients? How about ghosts?" 
    m "How about your tragic backstory? Were your parents neglectful, murderers, or both?"
    show eileen concerned
    e "..."
    show eileen happy
    "Let's keep a professional relationship."
    hide eileen with fade
    m2 "(Was it something I said?)"
    jump park

# The dog's reactions to evidence

label dog_ball:
    show dog
    d "BALL!! THROW THE BALL!!"
    m "D'aww, I can't say no to that face. Do you want to throw the ball, Eileen?"
    hide dog
    show eileen vhappy
    e "Sure!"
    n "Eileen throws the ball and the dog runs to fetch it. She returns with the ball in her mouth, tail wagging."
    $ my_evidence.remove(e_ball)
    hide eileen
    show dog
    d "THROW BALL!!"
    hide dog
    show eileen concerned
    e "Drop it."
    hide eileen
    show dog
    d "NO DROP... ONLY THROW!!"
    hide dog
    m2 "(I don't think we're getting that back...)"
    $ threw_ball = True
    jump park

label dog_dog:
    show dog
    m "Who's a good girl?"
    d "Rrr? (Who among us is truly good?)"
    m "Take a look at this evidence."
    d "!"
    m "That's right! It's youuuu!"
    d "*aggressive tail wagging* (OH MY GOD)"
    jump park

label dog_badge:
    show dog
    d "Shiny!"
    m "Thanks!!"

    jump park

label dog_default:
    show dog
    d "*sniff, sniff*"
    m "Hmm, she doesn't seem interested in this."
    hide dog
    show eileen vhappy
    e "She's still a good girl, though."
    n "We spend some time petting the dog."
    jump park


