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
        X=[f.name for f in self.__class__.instances]
        self.__class__.instances=[x for _, x in sorted(zip(X, self.__class__.instances))]

    def return_stats(self):
        return [self.name.title(), ":\n\nStrength: ", str(self.strength), "\nSpeed: ", str(self.speed),
                "\nStealth: ", str(self.stealth), "\nCunning: ", str(self.cunning), "\n\n\n"]


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
    if type is None:
        raise SystemExit
    return type


def edit_card():
    card_stats = error_check(
        ui.multenterbox("Enter the stats of your monster (Max is 25 for each stat)", "Stats", stats))
    all_clear = "no"
    while all_clear == "no":
        all_clear = "yes"
        for i in range(0, len(card_stats)):
            try:
                int(card_stats[i])
                if 1 > int(card_stats[i]) or int(card_stats[i]) > 25:
                    print(0 / 0)

            except:
                error_check(ui.msgbox("A " + stats[i] + " of " + str(card_stats[i]) + " is not valid "
                                                                                      "input\nTry an integer,"
                                                                                      " or make sure it is "
                                                                                      "between 1 and 25",
                                      title="Invalid input"))
                replacement_stat = error_check(
                    ui.integerbox("Please enter a new value for " + stats[i], title="Replacement Value",
                                  upperbound=25, lowerbound=1))
                error_check(ui.msgbox("Input accepted", title="Accepted"))
                card_stats[i] = replacement_stat
                all_clear = "no"
    return card_stats, all_clear


stats = ["Strength", "Speed", "Stealth", "Cunning"]
while 1:
    choice = error_check(ui.buttonbox("What do you want to do?", title="Choice",
                                      choices=["Add new card", "Search for a card", "View the full deck"]))
    if choice == "Add new card":
        while 1:
            name = error_check(ui.enterbox("What is the name of your monster?", title="Name"))
            if name == "":
                error_check(ui.msgbox("Please enter a name"))
            else:
                break
        add_card = "yes"
        while 1:
            variableconvertor = edit_card()
            all_clear = variableconvertor[1]
            card_stats = variableconvertor[0]
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
            card(name=name.lower(), strength=card_stats[0], speed=card_stats[1], stealth=card_stats[2],
                 cunning=card_stats[3])

    if choice == "Search for a card":
        card_search = error_check(ui.choicebox("Select the card you want to view", title="Card Search",
                                               choices=[f.name.title() for f in card.instances]))
        user_card = card.instances[[f.name for f in card.instances].index(card_search.lower())]
        option = error_check(
            ui.buttonbox("Here is your card, what do you want to do?\n\n" + "".join(card.return_stats(user_card)),
                         choices=["Continue", "Edit", "Delete"], title=user_card.name.title()))
        if option == "Edit":
            add_card = "yes"
            while 1:
                variableconvertor = edit_card()
                all_clear = variableconvertor[1]
                card_stats = variableconvertor[0]
                if all_clear == "yes":
                    add_to_deck = error_check(ui.buttonbox(
                        "".join(["Here is your card:\n", user_card.name.title(), ":\nStrength: ", str(card_stats[0]),
                                 "\nSpeed: ",
                                 str(card_stats[1]),
                                 "\nStealth: ", str(card_stats[2]), "\nCunning: ", str(card_stats[3]),
                                 "\n\nWould you like to update it or edit the values"]),
                        choices=["Update", "Edit", "Discard"]))
                    if add_to_deck == "Update":
                        break
                    if add_to_deck == "Discard":
                        add_card = "no"
                        card.instances.remove(user_card)
                        error_check(ui.msgbox(user_card.name.title() + " removed"))
                        break

            if add_card == "yes":
                card.instances.remove(user_card)
                card(name=user_card.name.lower(), strength=card_stats[0], speed=card_stats[1], stealth=card_stats[2],
                     cunning=card_stats[3])

        if option == "Delete":
            card.instances.remove(user_card)
            error_check(ui.msgbox(user_card.name.title() + " removed"))

    if choice == "View the full deck":
        full_card_deck = []
        for monster in card.instances:
            full_card_deck.extend(card.return_stats(monster))
        error_check(ui.codebox(msg="The entire deck", text="".join(full_card_deck)))
