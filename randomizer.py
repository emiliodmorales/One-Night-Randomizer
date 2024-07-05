import random
import distribution

def main():
    # does not include villagers
    dist = distribution.RoleDistribution()
    numPlayers = int(input("How many players? "))
    numRoles = numPlayers + 3
    chosenRoles = []
    i = 0
    while len(chosenRoles) < numRoles:
        # pick a random role
        selectedRole = dist.getRandomRole()
        # input(f"{len(chosenRoles) + 1}/{numRoles} Selected role: {selectedRole} ")
        # If it is Mason:
        #   There must be two open slots
        #   It adds both Masons
        if not dist.roleAvailable(selectedRole):
            # print(f"{selectedRole} was not available")
            continue
        if selectedRole == "Mason":
            if len(chosenRoles) + 2 <= numRoles:
                dist.takeRole(selectedRole)
                chosenRoles.append(selectedRole)

                dist.takeRole(selectedRole)
                chosenRoles.append(selectedRole)
        # If it is Alpha Wolf:
        #   There must be a Werewolf left
        #   It also adds a Werewolf
        elif selectedRole == "Alpha Wolf":
            if dist.roleAvailable("Werewolf"):
                numRoles += 1

                dist.takeRole(selectedRole)
                chosenRoles.append(selectedRole)

                dist.takeRole("Werewolf")
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
                dist.takeRole(selectedRole)
                chosenRoles.append(selectedRole)

                dist.takeRole("Seer")
                chosenRoles.append("Seer")
        # Otherwise it adds the selected role
        else:
            dist.takeRole(selectedRole)
            chosenRoles.append(selectedRole)
    for i, role in enumerate(chosenRoles):
        print(f"{i + 1}. {role}", end="\n")
    # prints the remaining roles
    # print(roles)
    return ""

if __name__ == "__main__":
    main()
