import sys
import distribution

# add features
#  only add apprentice tanner after adding tanner
#  only add apprentice seer after adding seer
#  only add aura seer after adding seer
#  only add beholder after adding seer
#  only add minion OR squire after adding werewolf


ROLE_WEIGHTS = {
    "Alpha Wolf": 0.9,
    "Apprentice Seer": 1.0,
    "Apprentice Tanner": 0.2,
    "Aura Seer": 0.9,
    "Beholder": 0.7,
    "Bodyguard": 0.0000001,
    "Copycat": 1.0,
    "Cursed": 0.0000001,
    "Doppelgänger": 1.0,
    "Dream Wolf": 0.2,
    "Drunk": 1.0,
    "Gremlin": 0.0,
    "Hunter": 1.5,
    "Insomniac": 1.0,
    "Mason": 1.0, # automatically adds both masons
    "Minion": 0.8,
    "Mystic Wolf": 0.9,
    "Paranormal Investigator": 1.0,
    "Prince": 1.0,
    "Revealer": 1.0,
    "Robber": 1.5,
    "Seer": 1.5,
    "Squire": 0.4,
    "Tanner": 0.4,
    "Troublemaker": 0.0,
    "Villager": 0.0, # excludes Villagers
    "Werewolf": 1.4, # accounts for two separate werewolves
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
    "Doppelgänger": 1,
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

def randomize(numPlayers):
    if numPlayers < 3:
        return "Not enough players"
    if numPlayers > 16:
        return "Too many players"
    
    # Create a fresh copy of the card list for each randomization
    card_list_copy = CARD_LIST.copy()
    dist = distribution.RoleDistribution(ROLE_WEIGHTS, card_list_copy)
    chosenRoles = dist.randomize(numPlayers)
    
    if not chosenRoles:  # Handle case where randomization failed
        return "Failed to generate roles - please try again"
    
    output = ""
    for i, role in enumerate(chosenRoles):
        output += f"{i + 1}. {role}\n"
    return output

def main():
    if len(sys.argv) == 2:
        numPlayers = int(sys.argv[1])
    else:
        numPlayers = int(input("How many players? "))
    print(randomize(numPlayers))

if __name__ == "__main__":
    main()
