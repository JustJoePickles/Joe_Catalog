import easygui as ui


class card:
    def __init__(self, name, strength, speed, stealth, cunning):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.stealth = stealth
        self.cunning = cunning


card(name="stoneling", strength=7, speed=1, stealth=25, cunning=15)
card(name="vexscream", strength=1, speed=6, stealth=21, cunning=19)
card(name="dawnmirage", strength=5, speed=15, stealth=18, cunning=22)
card(name="blazegolem", strength=15, speed=20, stealth=23, cunning=6)
card(name="websnake", strength=7, speed=15, stealth=10, cunning=5)
card(name="moldvine", strength=21, speed=18, stealth=14, cunning=5)
card(name="vortexwing", strength=19, speed=13, stealth=19, cunning=2)
card(name="rotthing", strength=16, speed=7, stealth=4, cunning=12)
card(name="froststep", strength=14, speed=14, stealth=17, cunning=4)
card(name="wispghoul", strength=17, speed=19, stealth=3, cunning=2)


def error_check(type):
    if type == None:
        raise SystemExit
    return type


choice = error_check(ui.buttonbox("What do you want to do?", title="Choice",
                                  choices=["Add new card", "Search for a card", "Delete a card", "View the full deck"]))
if choice=="Add new card":
    name=error_check(ui.enterbox("What is the name of your monster?", title="Name"))
    while True:
        stats=error_check(ui.multenterbox("Enter the stats of your monster (Max is 25 for each stat)", "Stats", ["Strength","Speed","Stealth","Cunning"]))
if choice=="Search for a card":
    None
if choice=="Delete a card":
    None
if choice=="View the full deck":
    None