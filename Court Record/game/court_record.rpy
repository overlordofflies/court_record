init python:

    class profile:
        """ basically, whatever fields you want for your profiles will go here
        base: all files/references to this character have this name"""
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
        #  the character you are presenting evidence to
        def __init__(self, name, evidenceList):
            self.name = name
            self.evidenceList = evidenceList
        def checkEvidence(self, currentEvidence):
            if str(currentEvidence) in self.evidenceList:
                return currentEvidence
            else:
                return "default"

    class courtRec:
        i = 0
        def __init__(self, evidence):
            self.evidence = evidence
            self.evidenceDict = {}
            if evidence_type == "profiles":
                for e in evidence:
                    self.evidenceDict[e.base] = [e.fullname, e.occupation, e.info]
            else:
                for e in evidence:
                    self.evidenceDict[e.base] = [e.name, e.info]
                
        def currentPic(self):
            for e in self.evidence:
                self.i += 1
                if self.i <= (ev_page + 1) * ev_icons and self.i > ev_page * ev_icons:
                    current_pic = "images/" + e.base + "_0.png"
                    renpy.ui.imagebutton(idle=str(current_pic), hover=str(current_pic), action=[SetVariable("current", e.base), ShowMenu("cr_detail")])                    
        def getPage(self):
            next_ev_page = ev_page + 1
            if next_ev_page > int(len(self.evidence)/ev_icons):
                next_ev_page = 0
            prev_ev_page = ev_page - 1
            if prev_ev_page < 0:
                prev_ev_page = 0
            return [prev_ev_page, next_ev_page]
        def baseList(self):
            baselist = []
            for e in self.evidence:
                baselist.append(e.base)
            return baselist
        def entryNumbers(self, currentEntry):
            self.currentEntry = currentEntry
            baselist = self.baseList()
            numdic = {k: v for v, k in enumerate(baselist)}
            currentEntryIndex = numdic[self.currentEntry]
            prevEntryIndex = currentEntryIndex - 1
            nextEntryIndex = currentEntryIndex + 1               
            if prevEntryIndex < 0:
                prevEntryIndex = len(self.evidence) -1
            nextEntryIndex = currentEntryIndex + 1
            if nextEntryIndex > len(self.evidence) - 1:
                nextEntryIndex = 0
            return [prevEntryIndex, nextEntryIndex]
        def getDetails(self):
            return self.evidenceDict[current]


##### COURT RECORD SCREEN

init -2:
    $ ev_xpos = 0
    $ ev_ypos = 120
    $ ev_icon_size = 270
    $ ev_row1 = 120
    $ ev_row2 = 520
    $ ev_row3 = 120

    #Icon grid 
    $ ev_icon_column = 4
    $ ev_icon_row = 2
    $ ev_icons = ev_icon_column * ev_icon_row
    $ ev_page = 0
    $ next_ev_page = 0
    $ prev_ev_page = 0

    $ info = ""
    $ current = "" 
    $ evidence_type = "profiles" 

screen court_record:
    tag menu
    modal True

    if evidence_type == "evidence":
        $ records = courtRec(my_evidence)
    elif evidence_type == "profiles":
        $ records = courtRec(my_profiles)

    frame:
        $ pages = records.getPage()
        xsize 1280
        ysize 720
        background Frame("evidence_window.png") 
        if ev_page > 0:
            imagebutton:
                idle "0_left_button.png"
                hover "1_left_button.png"
                action [SetVariable('ev_page', pages[0])]

        hbox:
            xpos 105
            xsize 1080

            vpgrid: 
                cols ev_icon_column 
                rows ev_icon_row
                draggable False
                mousewheel False
                
                
                $ records.currentPic()

        hbox: 
            xpos 1180
            xsize 100
            if pages[1] > 0:
                imagebutton:
                    yalign 0.5
                    idle "0_right_button.png"
                    hover "1_right_button.png"
                    action [SetVariable('ev_page', pages[1])]

    vbox:
        ypos 500
        xpos 20
        xsize 880
        hbox:
            xpos 640
            xanchor 0.5
            if evidence_type == "evidence":
                imagebutton auto "profile_button_%s.png" action [SetVariable("current", ""), SetVariable("ev_page", 0), SetVariable("evidence_type", "profiles")] 

            elif evidence_type == "profiles":
                imagebutton auto "evidence_button_%s.png" action [SetVariable("current", ""), SetVariable("ev_page", 0), SetVariable("next_ev_page", 0), SetVariable("evidence_type", "evidence")] 
            imagebutton auto "close_%s.png" action [Hide('court_record'), Jump(current_scene)]

screen cr_detail:
    tag menu
    modal True

    if npc != False:
        $ ev_label = npc.name + "_" + npc.checkEvidence(str(current))

    if evidence_type == "evidence":
        $ records = courtRec(my_evidence)
        $ 
    elif evidence_type == "profiles":
        $ records = courtRec(my_profiles)
    $ entryNumbers = records.entryNumbers(current)
    $ baselist = records.baseList()
    $ prev_detail_page = entryNumbers[0]
    $ next_detail_page = entryNumbers[1]



    frame:
        xsize 1280
        ysize 720
        background Frame("evidence_detail_window.png") 



        imagebutton:
            idle "0_left_button.png"
            hover "1_left_button.png"
            action [SetVariable('current', baselist[prev_detail_page])]

        hbox:
            xpos 105
            xsize 400

            $ current_pic = "/images/" + current + "_1.png"
            add current_pic
                
        hbox:
            xpos 680
            ypos 60
            vbox:
                ysize 200
                xsize 500
                if current == "":
                    text ""
                else:
                    $ details = records.getDetails()
                if evidence_type == "profiles":
                    text "{size=+5}{b}Name:{/b} " + details[0] + "{/size}"
                if evidence_type == "evidence":
                    text details[0]

                vbox:
                    ysize 120
                if evidence_type == "profiles":
                    text "{b}Occupation:{/b} " + details[1]
                    $ evinfo = details[2]
                if evidence_type == "evidence":
                    $ evinfo = details[1]
                for e in evinfo:
                    text e

        hbox: 
            xpos 1180
            xsize 100
            imagebutton:
                yalign 0.5
                idle "0_right_button.png"
                hover "1_right_button.png"
                action [SetVariable('current', baselist[next_detail_page])]

        vbox:
            xpos 20
            ypos 500
            hbox:
                xpos 640
                xanchor 0.5
                imagebutton auto "profile_button_%s.png" action [Hide("cr_detail"), SetVariable("current", ""), SetVariable("ev_page", 0), SetVariable("evidence_type", "profiles"), Show("court_record ")] 
                imagebutton auto "evidence_button_%s.png" action [Hide("cr_detail"), SetVariable("current", ""), SetVariable("ev_page", 0), SetVariable("next_ev_page", 0), SetVariable("evidence_type", "evidence"), Show("court_record ")]                 
                if npc != False:
                    $ ev_label = npc.name + "_" + npc.checkEvidence(current)
                    imagebutton auto "present_button_%s.png" action [Hide("cr_detail"), Jump(ev_label)]
                imagebutton auto "close_%s.png" action [Hide('cr_detail'), Jump(current_scene)]



############ Evidence Menu Buttons
#the menu for the corner of the screen
screen evidence_menu:
    imagebutton auto "profile_button_sm_%s.png" action [SetVariable("current", ""), SetVariable("evidence_type", "profiles"), ShowMenu("court_record")]  xalign .90 yalign .02  focus_mask True
    imagebutton auto "evidence_button_sm_%s.png" action [SetVariable("current", ""), SetVariable("evidence_type", "evidence"), ShowMenu("court_record")]  xalign .98 yalign .02 focus_mask True
    imagebutton auto "assistant_%s.png" action [Jump(assistant)] xalign .977 yalign .16  focus_mask True



