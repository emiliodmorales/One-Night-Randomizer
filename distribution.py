import math
import random

class RoleDistribution:
    

    def __init__(self, weights, deck) -> None:
        self.roleWeights = weights
        self.cardlist = deck

    def getRandomRole(self) -> str:
        r = math.floor(random.random() * self.totalWeight())
        cumulativeSum = 0
        for role, weight in self.roleWeights.items():
            cumulativeSum += weight
            if r <= cumulativeSum:
                return role
        return "N/A"

    def totalWeight(self) -> int:
        total = 0
        for _, weight in self.roleWeights.items():
            total += weight            
        return int(total)

    def numRoleRemaining(self, role: str) -> int:
        return self.cardlist[role]

    def roleAvailable(self, role: str) -> bool:
        return self.numRoleRemaining(role) > 0

    def takeRole(self, role: str) -> bool:
        self.cardlist[role] -= 1
        return self.cardlist[role] >= 0
    
    def randomize(self, numPlayers: int) -> list:
        numRoles = numPlayers + 3
        chosenRoles = []
        while len(chosenRoles) < numRoles:
            # pick a random role
            selectedRole = self.getRandomRole()
            # If it is Mason:
            #   There must be two open slots
            #   It adds both Masons
            if not self.roleAvailable(selectedRole):
                # print(f"{selectedRole} was not available")
                continue
            if selectedRole == "Mason":
                if len(chosenRoles) + 2 <= numRoles:
                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)

                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)
            # If it is Alpha Wolf:
            #   There must be a Werewolf left
            #   It also adds a Werewolf
            elif selectedRole == "Alpha Wolf":
                if self.roleAvailable("Werewolf"):
                    numRoles += 1

                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)

                    self.takeRole("Werewolf")
                    chosenRoles.append("Werewolf")
            # If it is Beholder:
            #   There must be a Seer
            #   If there is not a Seer:
            #       There must be two open slots
            #       It also adds the Seer
            elif selectedRole == "Beholder":
                if chosenRoles.count("Seer") == 1:
                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)
                elif len(chosenRoles) + 2 <= numRoles:
                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)

                    self.takeRole("Seer")
                    chosenRoles.append("Seer")
            # Otherwise it adds the selected role
            else:
                self.takeRole(selectedRole)
                chosenRoles.append(selectedRole)

        return chosenRoles

