import random
import sys
import distribution

# role weight chart
#   Always      : 999.0
#   Often       : 1.5
#   Standard    : 1.0
#   Rare        : 0.6
#   Barely      : 0.3
#   Never       : 0.0

ROLE_WEIGHTS = {
    "Alpha Wolf": 0.9,
    "Apprentice Seer": 1.0,
    "Apprentice Tanner": 0.5,
    "Aura Seer": 1.0,
    "Beholder": 1.0,
    "Bodyguard": 0.1,
    "Copycat": 1.0,
    "Cursed": 0.1,
    "Doppelganger": 1.0,
    "Dream Wolf": 0.5,
    "Drunk": 1.0,
    "Gremlin": 0.5,
    "Hunter": 1.0,
    "Insomniac": 1.0,
    "Mason": 1.0, # automatically adds both masons
    "Minion": 0.8,
    "Mystic Wolf": 0.8,
    "Paranormal Investigator": 1.0,
    "Prince": 1.0,
    "Revealer": 1.0,
    "Robber": 1.5,
    "Seer": 1.5,
    "Squire": 0.8,
    "Tanner": 0.6,
    "Troublemaker": 0.3,
    "Villager": 0.0, # excludes Villagers
    "Werewolf": 2.0, # accounts for two separate werewolves
    "Witch": 1.0,
}

CARD_LIST = {
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

def main():
    if len(sys.argv) == 2:
        numPlayers = int(sys.argv[1])
    else:
        numPlayers = int(input("How many players? "))

    dist = distribution.RoleDistribution(ROLE_WEIGHTS, CARD_LIST)
    chosenRoles = dist.randomize(numPlayers)
    for i, role in enumerate(chosenRoles):
        print(f"{i + 1}. {role}", end="\n")
    

if __name__ == "__main__":
    main()
