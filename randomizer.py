import sys
import distribution
import json
import os

# Load role weights and quantities from roles.json
ROLES_PATH = os.path.join(os.path.dirname(__file__), 'roles.json')
with open(ROLES_PATH, 'r', encoding='utf-8') as f:
    roles_data = json.load(f)
ROLE_WEIGHTS = roles_data['weights']
CARD_LIST = roles_data['quantities']

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
