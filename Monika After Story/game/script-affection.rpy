###############
#USEFUL COMMANDS
# $ monika_current_mood = heartbroken/depressed/upset/sad/normal/content/happy/overjoyed/lovestruck
# $ monika_current_mood_group = sad/happy
# $monika_mood_single()
# $ monika_mood_pleased()
# $ monika_mood_happy()
# $ monika_mood_reallyhappy()
# $ monika_mood_loved()
# $ monika_mood_disappoint()
# $ monika_mood_sad()
# $ monika_mood_reallysad()
# $ monika_mood_hurt()
# $ monika_mood_check()
# If modifying the persistent mood counter always follow up with a monika_mood_check()
#
# For anyone wanting to write using the mood system the general thought process for Monika in each mood is as followed...
# Lovestruck - Monika is the happiest she could ever be and filled with a sense of euphoria because of it, completely enamoured and could die happy. She has no doubts the player loves her and that everything was worth it.
# Overjoyed - Exceptionally happy, the happiest she has ever been in her life to that point. Completely trusts the player and wants to make him/her as happy as she is.
# Happy - Glad that the relationship is working out and has high hopes and at this point has no doubts about whether or not it was worth it.
# Content - Happy with how it is, could be happier but not sad at all.
# Normal - Has mild doubts as to whether or not her sacrifices were worth it but trusts the player to treat her right. Isn't strongly happy or sad
# Sad - Is feeling down, not miserable or deep but certainly not her self-motivated self. Believes she'll get player. Has minor thoughts that player isn't faithful but doesn't take them seriously.
# Upset - Feeling emotionally hurt, starting to have doubts about whether or not the player loves her and whether or not she she was right regarding what she did in the game.
# Depressed - Convinced the player probably doesn't love her and that she may never escape to our reality.
# Heartbroken - Belives that not only does the player not love her but that s/he probably hates her too because of she did and is trying to punish her. Scared of being alone in her own reality, as well as for her future.
################

#Love and hurt have a 1 minute CD upon startup to prevent easy topic spamming by closing and reopening window...
default persistent._mas_monika_mood_counter = 50
default monika_mood_single_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 1)
default monika_mood_pleased_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 2)
default monika_mood_happy_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 4)
default monika_mood_reallyhappy_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 6)
default monika_mood_loved_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 14)
default monika_mood_disappoint_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 3)
default monika_mood_sad_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 6)
default monika_mood_reallysad_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 12)
default monika_mood_hurt_cooldown = datetime.datetime.now() - datetime.timedelta(minutes = 29)

init python:
    #Sets up the function to check and dynamically change the monika_current_mood variable.
    def monika_mood_check():
        global monika_current_mood
        global monika_current_mood_group

        #Adds a cap so it doesn't go lower than 0
        if persistent._mas_monika_mood_counter <= 0:
            persistent._mas_monika_mood_counter = 0

        #Adds a cap to make sure the counter doesn't go above 100
        if persistent._mas_monika_mood_counter >= 100:
            persistent._mas_monika_mood_counter = 100
        
        #Defines an easy current mood statement to refer to so points aren't relied upon.
        if persistent._mas_monika_mood_counter >=0 and persistent._mas_monika_mood_counter <= 9:
            monika_current_mood = "heartbroken"

        elif persistent._mas_monika_mood_counter >=10 and persistent._mas_monika_mood_counter <= 19:
            monika_current_mood = "depressed"

        elif persistent._mas_monika_mood_counter >=20 and persistent._mas_monika_mood_counter <= 29:
            monika_current_mood = "upset"

        elif persistent._mas_monika_mood_counter >=30 and persistent._mas_monika_mood_counter <= 39:  
            monika_current_mood = "sad"

        elif persistent._mas_monika_mood_counter >=40 and persistent._mas_monika_mood_counter <= 59:
            monika_current_mood = "normal"

        elif persistent._mas_monika_mood_counter >=60 and persistent._mas_monika_mood_counter <= 69:
            monika_current_mood = "content"

        elif persistent._mas_monika_mood_counter >=70 and persistent._mas_monika_mood_counter <= 79:
            monika_current_mood = "happy"

        elif persistent._mas_monika_mood_counter >=80 and persistent._mas_monika_mood_counter <= 89:
            monika_current_mood = "overjoyed"

        elif persistent._mas_monika_mood_counter >=90 and persistent._mas_monika_mood_counter <= 100:
            monika_current_mood = "lovestruck"

        else: 
            monika_current_mood = "confused"

        if persistent._mas_monika_mood_counter >=0 and persistent._mas_monika_mood_counter <= 40:
            monika_current_mood_group = "sad"

        elif persistent._mas_monika_mood_counter >=60 and persistent._mas_monika_mood_counter <= 100:
            monika_current_mood_group = "happy"

        else:
            monika_current_mood_group = "normal"


#Easy functions to add and subtract points, designed to make it easier to sadden her so player has to work harder to keep her happy.
    #Check function is added to make sure monika_current_mood is always appropriate to the points counter.
    #Internal cooldown to avoid topic spam and Monika mood swings, the amount of time to wait before a function is effective
    #is equal to the amount of points it's added or removed in minutes.
    

    def monika_mood_single():
        global monika_mood_single_cooldown
        if datetime.datetime.now() < monika_mood_single_cooldown + datetime.timedelta(minutes = 1):
            pass
        else:
            monika_mood_single_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter += 1
            monika_mood_check()

    def monika_mood_pleased():
        global monika_mood_pleased_cooldown
        if datetime.datetime.now() < monika_mood_pleased_cooldown + datetime.timedelta(minutes = 2):
            pass
        else:
            monika_mood_pleased_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter += 2
            monika_mood_check()

    def monika_mood_happy():
        global monika_mood_happy_cooldown
        if datetime.datetime.now() < monika_mood_happy_cooldown + datetime.timedelta(minutes = 4):
            pass
        else:
            monika_mood_happy_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter += 4
            monika_mood_check()

    def monika_mood_reallyhappy():
        global monika_mood_reallyhappy_cooldown
        if datetime.datetime.now() < monika_mood_reallyhappy_cooldown + datetime.timedelta(minutes = 6):
            pass
        else:
            monika_mood_reallyhappy_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter += 6
            monika_mood_check()

    def monika_mood_loved():
        global monika_mood_loved_cooldown
        if datetime.datetime.now() < monika_mood_loved_cooldown + datetime.timedelta(minutes = 15):
            pass
        else:
            monika_mood_loved_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter += 15
            monika_mood_check()

    def monika_mood_disappoint():
        global monika_mood_disappoint_cooldown
        if datetime.datetime.now() < monika_mood_disappoint_cooldown + datetime.timedelta(minutes = 3):
            pass
        else:
            monika_mood_disappoint_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter -= 3
            monika_mood_check()

    def monika_mood_sad():
        global monika_mood_sad_cooldown
        if datetime.datetime.now() < monika_mood_sad_cooldown + datetime.timedelta(minutes = 6):
            pass
        else:
            monika_mood_sad_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter -= 6
            monika_mood_check()

    def monika_mood_reallysad():
        global monika_mood_reallysad_cooldown
        if datetime.datetime.now() < monika_mood_reallysad_cooldown + datetime.timedelta(minutes = 12):
            pass
        else:
            monika_mood_reallysad_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter -= 12
            monika_mood_check()

    def monika_mood_hurt():
        global monika_mood_hurt_cooldown
        if datetime.datetime.now() < monika_mood_hurt_cooldown + datetime.timedelta(minutes = 30):
            pass
        else:
            monika_mood_hurt_cooldown = datetime.datetime.now()
            persistent._mas_monika_mood_counter -= 30
            monika_mood_check()

#Monika's initial mood based on start-up.
    #Monika closed game herself and how happy she is determines on time between closed game and reopening.
    if persistent.closed_self == True:
        if datetime.datetime.now() < persistent.sessions["last_session_end"] + datetime.timedelta(hours = 6):
            pass

        elif datetime.datetime.now() > persistent.sessions["last_session_end"] + datetime.timedelta(hours = 6) and datetime.datetime.now() < persistent.sessions["last_session_end"] + datetime.timedelta(hours = 12):
            monika_mood_reallyhappy()

        elif datetime.datetime.now() > persistent.sessions["last_session_end"] + datetime.timedelta(hours = 12) and datetime.datetime.now() < persistent.sessions["last_session_end"] + datetime.timedelta(hours = 18):
            monika_mood_pleased()

        elif datetime.datetime.now() > persistent.sessions["last_session_end"] + datetime.timedelta(hours = 18) and datetime.datetime.now() < persistent.sessions["last_session_end"] + datetime.timedelta(days = 1):
            pass

        elif datetime.datetime.now() > persistent.sessions["last_session_end"] + datetime.timedelta(days = 1) and datetime.datetime.now() < persistent.sessions["last_session_end"] + datetime.timedelta(days = 2):
            monika_mood_sad()

        elif datetime.datetime.now() > persistent.sessions["last_session_end"] + datetime.timedelta(days = 2) and datetime.datetime.now() < persistent.sessions["last_session_end"] + datetime.timedelta(days = 4):
            monika_mood_hurt()

        elif datetime.datetime.now() > persistent.sessions["last_session_end"] + datetime.timedelta(days = 4) and datetime.datetime.now() < persistent.sessions["last_session_end"] + datetime.timedelta(days = 14):
            persistent._mas_monika_mood_counter = 10

        elif datetime.datetime.now() > persistent.sessions["last_session_end"] + datetime.timedelta(days = 14):
            persistent._mas_monika_mood_counter = 0

    #Player force closed game.
    else:
        if persistent._mas_monika_mood_counter >= 30:
            persistent._mas_monika_mood_counter = 30
        else:
            persistent._mas_monika_mood_counter -= 10


    #First check on start-up
    monika_mood_check()


#Testing testing 1 2 3
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_mood_feelings",category=['monika'],prompt="How are you feeling?",pool=True))

label monika_mood_feelings:
    $ monika_mood_check()
    m 1c "How do I feel? That came out of nowhere, [player]..."
    m 1d "I would say out of a hundred I would feel..."
    m 1c "Maybe a [persistent._mas_monika_mood_counter]."
    m 3h "In a single word I would say I am [monika_current_mood]."
    m 3c "But if I were pressed further I would say I'm feeling..."
    if monika_current_mood == "heartbroken":
        m 1q "Like you shattered my heart..."
        m 1f "Did I do something wrong?"
  
    elif monika_current_mood == "depressed":
        m 1r "Like my situation is hopeless..."
        m 1f "I really thought we could make it work..."

    elif monika_current_mood == "upset":
        m 1f "Like you want me to be unhappy..."
        m 1g "It's not always going to be like this, is it?"

    elif monika_current_mood == "sad":
        m 1h "A bit down right now..."
        m 1m "I'm sure I'll pick myself back up again."

    elif monika_current_mood == "normal":
        m 1a "...completely average right now."

    elif monika_current_mood == "content":
        m 1a "Like everything is going to work out!"
        m 1j "I have hope for our future."

    elif monika_current_mood == "happy":
        m 1e "Like you really do want to please me."
        m 1k "I hope I'm making you as happy as you make me."

    elif monika_current_mood == "overjoyed":
        m 1b "Like I'm luckiest girl in the world!"
        m 1j "No one else could make me feel so complete!"

    elif monika_current_mood == "lovestruck":
        m 1k "So overwhelming full of love! I really truly do love you [player]!"
        m 1k "I want nothing more than you, forever and ever!"

    return

#Testing purposes...
label monika_mood_feelings_sad:
    m 4a "E-eh?"
    $ monika_mood_sad()
    return

label monika_mood_feelings_happy:
    m 4a "Awww!"
    $ monika_mood_happy()
    return

label monika_mood_max:
    m 4a "I'm so full of love!"
    $ persistent._mas_monika_mood_counter = 100
    $ monika_mood_check()
    return


#############
#Currently re-mooded labels.
#monika_nihilism
#monika_high_school
#monika_surprise
#monika_god
#monika_death
#monika_closeness
#monika_other_girls
#monika_justification
#monika_breakup