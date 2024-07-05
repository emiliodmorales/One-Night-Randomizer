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
        "Alpha Wolf": 1.0,
        "Apprentice Seer": 1.0,
        "Apprentice Tanner": 1.0,
        "Aura Seer": 1.0,
        "Beholder": 1.0,
        "Bodyguard": 1.0,
        "Copycat": 1.0,
        "Cursed": 1.0,
        "Doppelganger": 1.0,
        "Dream Wolf": 1.0,
        "Drunk": 1.0,
        "Gremlin": 1.0,
        "Hunter": 1.0,
        "Insomniac": 1.0,
        "Mason": 2.0,
        "Minion": 1.0,
        "Mystic Wolf": 1.0,
        "Paranormal Investigator": 1.0,
        "Prince": 1.0,
        "Revealer": 1.0,
        "Robber": 1.0,
        "Seer": 1.0,
        "Squire": 1.0,
        "Tanner": 1.0,
        "Troublemaker": 1.0,
        "Villager": 0.0, # excludes Villagers
        "Werewolf": 2.0,
        "Witch": 1.0,
    }

    def __init__(self) -> None:
        pass

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
        return self.remainingRoles[role]

    def roleAvailable(self, role: str) -> bool:
        return self.numRoleRemaining(role) > 0

    def takeRole(self, role: str) -> bool:
        self.remainingRoles[role] -= 1
        return self.remainingRoles[role] >= 0
