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
            # Only add Apprentice Tanner after adding Tanner
            if selectedRole == "Apprentice Tanner" and chosenRoles.count("Tanner") == 0:
                continue
            # Only add Apprentice Seer after adding Seer
            if selectedRole == "Apprentice Seer" and chosenRoles.count("Seer") == 0:
                continue
            # Only add Aura Seer after adding Seer
            if selectedRole == "Aura Seer" and chosenRoles.count("Seer") == 0:
                continue
            # Only add Beholder after adding Seer
            if selectedRole == "Beholder":
                if chosenRoles.count("Seer") == 1:
                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)
                    continue
                elif len(chosenRoles) + 2 <= numRoles:
                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)

                    self.takeRole("Seer")
                    chosenRoles.append("Seer")
                    continue
                else:
                    continue
            # Only add Minion OR Squire after adding Werewolf
            if selectedRole in ("Minion", "Squire") and chosenRoles.count("Werewolf") == 0:
                continue
            # Mason logic
            if selectedRole == "Mason":
                if len(chosenRoles) + 2 <= numRoles:
                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)

                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)
                continue
            # Alpha Wolf logic
            if selectedRole == "Alpha Wolf":
                if self.roleAvailable("Werewolf"):
                    numRoles += 1

                    self.takeRole(selectedRole)
                    chosenRoles.append(selectedRole)

                    self.takeRole("Werewolf")
                    chosenRoles.append("Werewolf")
                continue
            # Otherwise it adds the selected role
            self.takeRole(selectedRole)
            chosenRoles.append(selectedRole)

        return chosenRoles

