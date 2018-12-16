init python:
    class profile:
        """ 
        name, fullname, occupation, info: 
            basically, whatever fields you want for your profiles will go here
        base: this is the base for all file names that refer to this character"""
        def __init__(self, name, fullname, occupation, info, base):
            self.name = name 
            self.fullname = fullname
            self.occupation = occupation
            self.info = info 
            self.base = base
        def change(self, info): 
            # this allows you to change the "info" field. 
            if info:
                self.info = info

    class evidence:
        #this follows exactly the same format as profiles
        def __init__(self, name, info, base):
            self.name = name 
            self.info = info 
            self.base = base
        def change(self, info): 
            if info:
                self.info = info


    class currentChar:
        # Here is where you set up the character you are presenting evidence to
        def __init__(self, name, evidenceList):
            self.name = name
            self.evidenceList = evidenceList
        def checkEvidence(self, currentEvidence):
            if str(currentEvidence) in self.evidenceList:
                return currentEvidence
            else:
                return "default"


##### COURT RECORD SCREEN

init -2:
    $ ev_xpos = 0
    $ ev_ypos = 120
    $ ev_icon_size = 260
    $ ev_row1 = 120
    $ ev_row2 = 520
    $ ev_row3 = 120

    #Icon grid 
    $ ev_icon_column = 4
    $ ev_icon_row = 2
    $ ev_icons = ev_icon_column * ev_icon_row
    $ ev_page = 0

screen court_record:
    tag menu
    modal True

    if evidence_type == "evidence":
        for e in my_evidence:
            if current == "blank":
                pass
            elif current == e.base:
                $ name = "{b}" + e.name + "{/b}"
                $ info = e.info
                $ pic = e.base + "_0.png"
    elif evidence_type == "profiles":
        for p in my_profiles:
            if current == "blank":
                pass
            elif current == p.base:
                $ fullname = "{b}Name:{/b} " + p.fullname
                $ occupation = "{b}Occupation:{/b} " + p.occupation
                $ info = p.info
                $ pic = p.base + "_0.png"                
    else:
        textbutton "something went wrong dude" action [Hide('court_record')] xpos 500 ypos 500

    if npc != False:
        $ ev_label = npc.name + "_" + npc.checkEvidence(str(current))

    hbox:
        xpos ev_xpos
        ypos ev_ypos
        vbox:
            xsize ev_icon_size * ev_icon_column
            ysize ev_icon_size * ev_icon_row
            grid ev_icon_column ev_icon_row:
                $ i = 0
                $ next_ev_page = ev_page + 1
                $ prev_ev_page = ev_page - 1
                if next_ev_page > int(len(my_evidence)/ev_icons):
                    $ next_ev_page = 0
                if evidence_type == "evidence":
                    for e in my_evidence:
                        $i += 1
                        if i <= (ev_page + 1) * ev_icons and i > ev_page * ev_icons:
                            $current_pic = e.base + "_0.png"
                            imagebutton idle current_pic hover current_pic action SetVariable("current", e.base)
                elif evidence_type == "profiles":
                    for p in my_profiles:
                        $i += 1
                        if i <= (ev_page + 1) * ev_icons and i > ev_page * ev_icons:
                            $current_pic = p.base + "_0.png"
                            imagebutton idle current_pic hover current_pic action SetVariable("current", p.base)
                else:
                    $ current_pic = "dog_0.png"
                for j in range(i, (ev_page + 1)*ev_icons):
                    null 
            hbox:
                if ev_page > 0:
                    textbutton _("<-") action [SetVariable('ev_page', prev_ev_page)]
                if next_ev_page > 0:
                    textbutton _("->") action [SetVariable('ev_page', next_ev_page)]
        vbox:
            ysize ev_row3
            if current == "":
                text "No evidence selected"
            else:
                add current_pic
                if evidence_type == "evidence":
                    text name
                    text info
                elif evidence_type == "profiles":
                    text fullname
                    text occupation
                    text info
  






############ Evidence Menu Buttons
#the menu that hangs out with the text box
screen evidence_menu:
    $ ev_menu_x = 850
    $ ev_menu_y = 500
    $ ev_menu_spacing = 100

    textbutton "Profiles" action ShowMenu("profile_screen")  xpos ev_menu_x ypos ev_menu_y  focus_mask True
    $ ev_menu_x += ev_menu_spacing
    textbutton "Evidence" action ShowMenu("evidence_screen") xpos ev_menu_x ypos ev_menu_y focus_mask True




