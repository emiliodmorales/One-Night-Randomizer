import random

def main():
    # does not include villagers
    roles = [
        "Alpha Wolf",
        "Apprentice Seer",
        "Apprentice Tanner",
        "Aura Seer",
        "Beholder",
        "Bodyguard",
        "Copycat",
        "Cursed",
        "Doppelganger",
        "Dream Wolf",
        "Drunk",
        "Gremlin",
        "Hunter",
        "Insomniac",
        "Mason",
        "Minion",
        "Mystic Wolf",
        "Paranormal Investigator",
        "Prince",
        "Revealer",
        "Robber",
        "Seer",
        "Squire",
        "Tanner",
        "Troublemaker",
        "Werewolf",
        "Werewolf",
        "Witch",
    ]

    numPlayers = int(input("How many players? "))
    numRoles = numPlayers + 3
    chosenRoles = []
    i = 0
    while len(chosenRoles) < numRoles:
        # pick a random role
        selectedRole = random.choice(roles)
        # remove it from the list
        roles.remove(selectedRole)
        # If it is Mason:
        #   There must be two open slots
        #   It adds both Masons
        if selectedRole == "Mason":
            if len(chosenRoles) + 2 <= numRoles:
                chosenRoles.append(selectedRole)
                chosenRoles.append(selectedRole)
        # If it is Alpha Wolf:
        #   There must be a Werewolf left
        #   It also adds a Werewolf
        elif selectedRole == "Alpha Wolf":
            if roles.count("Werewolf") > 0:
                numRoles += 1

                chosenRoles.append(selectedRole)

                roles.remove("Werewolf")
                chosenRoles.append("Werewolf")
        # If it is Beholder:
        #   There must be a Seer
        #   If there is not a Seer:
        #       There must be two open slots
        #       It also adds the Seer
        elif selectedRole == "Beholder":
            if chosenRoles.count("Seer") == 1:
                chosenRoles.append(selectedRole)
            elif len(chosenRoles) + 2 <= numRoles:
                roles.remove("Seer")
                chosenRoles.append("Seer")
                chosenRoles.append(selectedRole)
        # Otherwise it adds the selected role
        else:
            chosenRoles.append(selectedRole)
    for i, role in enumerate(chosenRoles):
        print(f"{i + 1}. {role}", end="\n")
    # prints the remaining roles
    # print(roles)
    return ""

if __name__ == "__main__":
    main()
