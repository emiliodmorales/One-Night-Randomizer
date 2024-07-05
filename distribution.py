import math
import random

class RoleDistribution:
    remainingRoles = {
        "Alpha Wolf": 1,
        "Apprentice Seer": 1,
        "Apprentice Tanner": 1,
        "Aura Seer": 1,
        "Beholder": 1,
        "Bodyguard": 1,
        "Copycat": 1,
        "Cursed": 1,
        "Doppelganger": 1,
        "Dream Wolf": 1,
        "Drunk": 1,
        "Gremlin": 1,
        "Hunter": 1,
        "Insomniac": 1,
        "Mason": 2,
        "Minion": 1,
        "Mystic Wolf": 1,
        "Paranormal Investigator": 1,
        "Prince": 1,
        "Revealer": 1,
        "Robber": 1,
        "Seer": 1,
        "Squire": 1,
        "Tanner": 1,
        "Troublemaker": 1,
        "Villager": 3,
        "Werewolf": 2,
        "Witch": 1,
    }
    roleWeights = {
        "Alpha Wolf": 1,
        "Apprentice Seer": 1,
        "Apprentice Tanner": 1,
        "Aura Seer": 1,
        "Beholder": 1,
        "Bodyguard": 1,
        "Copycat": 1,
        "Cursed": 1,
        "Doppelganger": 1,
        "Dream Wolf": 1,
        "Drunk": 1,
        "Gremlin": 1,
        "Hunter": 1,
        "Insomniac": 1,
        "Mason": 1,
        "Minion": 1,
        "Mystic Wolf": 1,
        "Paranormal Investigator": 1,
        "Prince": 1,
        "Revealer": 1,
        "Robber": 1,
        "Seer": 1,
        "Squire": 1,
        "Tanner": 1,
        "Troublemaker": 1,
        "Villager": 0, # excludes Villagers
        "Werewolf": 1,
        "Witch": 1,
    }

    def __init__(self) -> None:
        pass

    def getRandomRole(self) -> str:
        # self.normalizeWeights()
        r = math.floor(random.random() * self.totalWeight())
        # print(r)
        cumulativeSum = 0
        for role, weight in self.roleWeights.items():
            cumulativeSum += weight
            # print(cumulativeSum)
            # print(role, weight)
            if r <= cumulativeSum:
                return role
        return "N/A"

    def totalWeight(self) -> int:
        total = 0
        for _, weight in self.roleWeights.items():
            total += weight            
        return total
    
    def normalizeWeights(self) -> None:
        total = self.totalWeight()
        for role, weight in self.roleWeights.items():
            self.roleWeights[role] = weight / total

    def numRoleRemaining(self, role: str) -> int:
        return self.remainingRoles[role]

    def roleAvailable(self, role: str) -> bool:
        return self.numRoleRemaining(role) > 0

    def takeRole(self, role: str) -> str:
        self.remainingRoles[role] -= 1
        return self.remainingRoles[role] >= 0
