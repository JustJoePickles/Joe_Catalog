import easygui as ui


class card:
    instances = []

    def __init__(self, name, strength, speed, stealth, cunning):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.stealth = stealth
        self.cunning = cunning
        self.__class__.instances.append(self)


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


stats = ["Strength", "Speed", "Stealth", "Cunning"]
while 1:
    choice = error_check(ui.buttonbox("What do you want to do?", title="Choice",
                                      choices=["Add new card", "Search for a card", "Delete a card",
                                               "View the full deck"]))
    if choice == "Add new card":
        while 1:
            name = error_check(ui.enterbox("What is the name of your monster?", title="Name"))
            if name == "":
                ui.msgbox("Please enter a name")
            else:
                break

        while 1:
            card_stats = error_check(
                ui.multenterbox("Enter the stats of your monster (Max is 25 for each stat)", "Stats", stats))
            all_clear = "no"
            add_card = "yes"
            while all_clear == "no":
                all_clear = "yes"
                for i in range(0, len(card_stats)):
                    try:
                        int(card_stats[i])
                        if 1 > int(card_stats[i]) or int(card_stats[i]) > 25:
                            print(0 / 0)

                    except:
                        error_check(ui.msgbox("A " + stats[i] + " of " + str(card_stats[i]) + "is not valid "
                                                                                              "input\nTry an integer,"
                                                                                              " or make sure it is "
                                                                                              "between 1 and 25",
                                              title="Invalid input"))
                        replacement_stat = error_check(
                            ui.integerbox("Please enter a new value for " + stats[i], title="Replacement Value",
                                          upperbound=25, lowerbound=1))
                        card_stats[i] = replacement_stat
                        all_clear = "no"
            if all_clear == "yes":
                add_to_deck = error_check(ui.buttonbox(
                    "".join(["Here is your card:\n", name.title(), ":\nStrength: ", str(card_stats[0]), "\nSpeed: ",
                             str(card_stats[1]),
                             "\nStealth: ", str(card_stats[2]), "\nCunning: ", str(card_stats[3]),
                             "\n\nWould you like to add it to the deck or edit the values"]),
                    choices=["Add to deck", "Edit", "Discard"]))
                if add_to_deck == "Add to deck":
                    break
                if add_to_deck == "Discard":
                    add_card = "no"
                    break

        if add_card == "yes":
            card(name=name, strength=card_stats[0], speed=card_stats[1], stealth=card_stats[2], cunning=card_stats[3])

    if choice == "Search for a card":
        None
    if choice == "Delete a card":
        None
    if choice == "View the full deck":
        full_card_deck = []
        for monster in card.instances:
            full_card_deck.extend(
                [monster.name.title(), ":\n\nStrength: ", str(monster.strength), "\nSpeed: ", str(monster.speed),
                 "\nStealth: ", str(monster.stealth), "\nCunning: ", str(monster.cunning), "\n\n\n"])
        error_check(ui.codebox(msg="The entire deck", text="".join(full_card_deck)))
