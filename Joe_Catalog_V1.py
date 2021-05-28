########################################################################################################################

import easygui as ui  # easygui is required for the graphical interface


########################################################################################################################

class card:  # This is the class that will store the stats for every card
    instances = []  # List that will contain every card object so they can be easily referenced without being assigned

    # to specific variables

    def __init__(self, name, strength, speed, stealth, cunning):  # Will run whenever a Card object is created and
        # will assign the relevant stats for ease of referencing
        self.name = name  # These are pretty self explanatory
        self.strength = strength
        self.speed = speed
        self.stealth = stealth
        self.cunning = cunning

        self.__class__.instances.append(self)  # Add this object to the list

        # The following code sorts the objects list into alphabetical order for consistency when displaying cards
        X = [f.name for f in self.__class__.instances]  # Create a list containing the name property of every object
        self.__class__.instances = [x for _, x in sorted(zip(X, self.__class__.instances))]  # Sorts the list
        # alphabetically

        # zip() combines the list of names with the list of objects into tuple pairs, eg (Rotthing,<__main__.card
        # object at 0x0000012EC63FF970>).   This is then sorted by the names list, meaning that the cards objects
        # will also be sorted in alphabetical order.  Finally, the first element in every tuple will be ignored
        # giving a sorted list of just the card objects

    def return_stats(self):  # Function used to print formatted stats for a card
        return [self.name.title(), ":\n\nStrength: ", str(self.strength), "\nSpeed:    ", str(self.speed),
                "\nStealth:  ", str(self.stealth), "\nCunning:  ", str(self.cunning), "\n\n\n"]  # returns the formatted
        # output for a given object (self)


########################################################################################################################

card(name="stoneling", strength=7, speed=1, stealth=25, cunning=15)  # Initialises the existing cards as card() objects
card(name="vexscream", strength=1, speed=6, stealth=21, cunning=19)
card(name="dawnmirage", strength=5, speed=15, stealth=18, cunning=22)
card(name="blazegolem", strength=15, speed=20, stealth=23, cunning=6)
card(name="websnake", strength=7, speed=15, stealth=10, cunning=5)
card(name="moldvine", strength=21, speed=18, stealth=14, cunning=5)
card(name="vortexwing", strength=19, speed=13, stealth=19, cunning=2)
card(name="rotthing", strength=16, speed=7, stealth=4, cunning=12)
card(name="froststep", strength=14, speed=14, stealth=17, cunning=4)
card(name="wispghoul", strength=17, speed=19, stealth=3, cunning=2)


########################################################################################################################


def error_check(type):  # Very important error checking function, used whenever a ui element is created to check if
    # the user cancelled out of the program
    if type is None:  # If the product of the ui element is None (pressing [x] or cancel
        raise SystemExit  # End the program
    return type  # Otherwise return the product of the ui element


########################################################################################################################


def edit_card():  # Edit/create card stats, used in two places hence the function
    UPPERBOUND = 25  # Using constants rather than literals makes the program more readily adaptable
    LOWERBOUND = 1
    card_stats = error_check(  # Gives the user multiple boxes to enter the respective stats into
        ui.multenterbox("Enter the stats of your monster (Max is 25 for each stat)", "Stats", stats))
    all_clear = "no"  # all_clear records whether the user has entered an invalid input ("yes" means no issues)
    while all_clear == "no":  # Run this loop while there are issues in the input
        all_clear = "yes"  # If no errors are found, all_clear won't be changed and therefore must be "yes"
        for i in range(0, len(card_stats)):  # Primary error checking loop, runs for each stat in the users input (
            # stats are stored as a list)
            try:  # If an error is raised, the users input is invalid and will move to the except loop
                int(card_stats[i])  # Test if the values are integers
                if LOWERBOUND > int(card_stats[i]) or int(card_stats[i]) > UPPERBOUND:  # Boundary testing for if
                    # stat is within the required range (from 1=>25)
                    print(0 / 0)  # This is just used to raise an error message and move to the except, will only run
                    # if the user's input exceeds the bounds (could also use raise SystemError)

            except:
                error_check(ui.msgbox("A " + stats[i] + " of " + str(card_stats[i]) + " is not valid "
                                                                                      "input\nTry an integer,"
                                                                                      " or make sure it is "
                                                                                      "between " + str(
                    LOWERBOUND) + " and " + str(UPPERBOUND), title="Invalid input"))  # Shows the user the invalid
                # input and some potential issues
                replacement_stat = error_check(  # This stat will replace the incorrect input for when the card()
                    # object is created
                    ui.integerbox("Please enter a new value for " + stats[i], title="Replacement Value",
                                  upperbound=UPPERBOUND, lowerbound=LOWERBOUND))  # Using an integer box ensures the
                # user has to enter an integer, the upper and lowerbounds ensures the input fits in the required range.
                # As such, the user's input will always be valid after this step
                error_check(ui.msgbox("Input accepted", title="Accepted"))  # let's the user know they entered a valid
                # input; improves user experience when there are multiple incorrect stats
                card_stats[i] = replacement_stat  # replace the invalid stat with its relevant valid stat
                all_clear = "no"  # Records that there has been an invalid input
    return card_stats, all_clear  # Returns the list of stats and the all clear status as a tuple


########################################################################################################################

stats = ["Strength", "Speed", "Stealth", "Cunning"]  # List of possible stats, used when displaying a card

########################################################################################################################

while 1:  # The main body of code, this loop will run until the user exits the program
    choice = error_check(ui.buttonbox("What do you want to do?", title="Choice",  # The 'homepage' in essence, lets
                                      # the user pick which of the program's features to use
                                      choices=["Add new card", "Search for a card", "View the full deck"]))

    ########################################################################################################################

    if choice == "Add new card":  # Adds a new card using - in part - the edit_card function from earlier
        while 1:  # Loops to ensure the user doesn't leave the name field blank
            name = error_check(ui.enterbox("What is the name of your monster?", title="Name"))  # Gets name input
            if name == "":  # If the name field is blank
                error_check(ui.msgbox("Please enter a name"))  # Prompt the user to enter a name
            else:  # Otherwise exit the loop
                break

        add_card = "yes"  # Variable that determines whether the user want to add their card to the deck
        while 1:  # Loop that gets the user's card's stats and asks what they'd like to do with the card
            variableconverter = edit_card()  # Runs the function described earlier. Variable converter is used to
            # convert the single tuple into two separate variables
            all_clear = variableconverter[1]  # Saves the all_clear value
            card_stats = variableconverter[0]  # Saves the list of stats for the card
            if all_clear == "yes":  # If there were no invalid inputs (otherwise the loop will return to the beginning)
                add_to_deck = error_check(ui.buttonbox(  # Presents the user their card and checks what they want to
                    # do with it
                    "".join(["Here is your card:\n", name.title(), ":\nStrength: ", str(card_stats[0]), "\nSpeed:    ",
                             str(card_stats[1]),
                             "\nStealth:  ", str(card_stats[2]), "\nCunning:  ", str(card_stats[3]),
                             "\n\nWould you like to add it to the deck or edit the values"]),
                    choices=["Add to deck", "Edit", "Discard"]))
                if add_to_deck == "Add to deck":  # As add_card is already "yes", this just breaks out of the loop
                    # and the card will be added
                    break
                if add_to_deck == "Discard":  # Set add_card to "no", so the code will continue without creating a
                    # new card() object
                    add_card = "no"
                    break
                # Note: No if statement is required for if the user picks "Edit", as by default the loop will just go
                # again from the beginning, asking the user for new stats and giving the impression they are editing
                # their card's stats (in reality they are overwriting them)

        if add_card == "yes":  # If the user hasn't chosen to discard their card:
            card(name=name.lower(), strength=card_stats[0], speed=card_stats[1], stealth=card_stats[2],
                 cunning=card_stats[3])  # Create a card() object with the relevant stats attached to the relevant
            # properties

    ########################################################################################################################

    if choice == "Search for a card":  # Allows the user to find a specific card in the deck and edit as appropriate
        card_search = error_check(ui.choicebox("Select the card you want to view", title="Card Search",
                                               choices=[f.name.title() for f in card.instances]))  # Presents the
        # user with the list of card() names (using the list compression from earlier) and allows them to select one
        user_card = card.instances[[f.name for f in card.instances].index(card_search.lower())]  # Finds card()
        # object attached to the user's selected name
        option = error_check(  # Presents the user's selected card and offers the choice to edit, continue, or delete it
            ui.buttonbox("Here is your card, what do you want to do?\n\n" + "".join(card.return_stats(user_card)),
                         choices=["Continue", "Edit", "Delete"], title=user_card.name.title()))
        if option == "Edit":  # Edits the card() using modified code from "Add new card"
            # Most of the following has already been explained earlier, so I will annotate where appropriate
            add_card = "yes"
            while 1:
                variableconverter = edit_card()
                all_clear = variableconverter[1]
                card_stats = variableconverter[0]
                if all_clear == "yes":
                    add_to_deck = error_check(ui.buttonbox(
                        "".join(["Here is your card:\n", user_card.name.title(), ":\nStrength: ", str(card_stats[0]),
                                 "\nSpeed:    ",
                                 str(card_stats[1]),
                                 "\nStealth:  ", str(card_stats[2]), "\nCunning:  ", str(card_stats[3]),
                                 "\n\nWould you like to update it or edit the values"]),
                        choices=["Update", "Edit", "Discard"]))
                    if add_to_deck == "Update":  # Note "Update" instead of "Add card"
                        break
                    if add_to_deck == "Discard":
                        add_card = "no"
                        card.instances.remove(user_card)  # In this case, because the card already exists as a card()
                        # object, it has to be removed from the instances list
                        error_check(ui.msgbox(user_card.name.title() + " removed"))  # Notifies the user that the
                        # card has been removed
                        break

            if add_card == "yes":
                card.instances.remove(user_card)  # To update the card's stats, the existing card is removed
                card(name=user_card.name.lower(), strength=card_stats[0], speed=card_stats[1], stealth=card_stats[2],
                     cunning=card_stats[3])  # And the newly created card (of the same name) is added
                # Note the need for alphabetical sorting, now the card remains in the same place in the list whereas
                # otherwise it would have been moved to the bottom, creating confusion for the user

        if option == "Delete":  # Same code as before, simply deletes the card from the instances list and notifies
            # the user
            card.instances.remove(user_card)
            error_check(ui.msgbox(user_card.name.title() + " removed"))

    ########################################################################################################################

    if choice == "View the full deck":  # Outputs the entire deck to an easygui window
        full_card_deck = []  # This list contains all the individually formatted card display messages
        for monster in card.instances:  # For every item in the list of cards
            full_card_deck.extend(card.return_stats(monster))  # Run the formatted stats function for each card and
            # add it to the full_card_deck list
        error_check(ui.codebox(msg="The entire deck", text="".join(full_card_deck)))  # Outputs the entire deck in a
        # code box (scrollable and with a header)

########################################################################################################################
