import random
print('''   _____      _ _          __   _____                                         
  / ____|    | | |        / _| |  __ \                                        
 | |     __ _| | |   ___ | |_  | |  | |_   _ _ __   __ _  ___  ___  _ __  ___ 
 | |    / _` | | |  / _ \|  _| | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __|
 | |___| (_| | | | | (_) | |   | |__| | |_| | | | | (_| |  __/ (_) | | | \__ |
  \_____\__,_|_|_|  \___/|_|   |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|___/
                                                    __/ |                     
                                                   |___/                      ''')
print('Welcome To Call Of The Dungeons')

#making player class
class player:
    def __init__(self, name, path = ''):
        self.name = name
        self.path = path
        self.health = 0
        self.relationship = False
        self.agility = 0
        self.attack = 100
  
    def __repr__(self):
        return '\nI {} am a {} and with my {} health and {} agility i am ready'.format(self.name, self.path, self.health, self.agility)
  
#making path class
class path:
    def __init__(self, name, health, agility):
        self.name = name
        self.health = health
        self.agility = agility

    def __repr__(self):
        return '\nThe path of the {} gives you {} health and {} agility'.format(self.name, self.health, self.agility)

#making enemy class
class enemy:
    def __init__(self, name, path = ''):
        self.name = name
        self.path = path
        self.health = 0
        self.attack = 50
    def __repr__(self):
        return '\nI {} have chosen the {} path and with my power i will do terrible things to the people of honneywood!!!'.format(self.name, self.path)

#making battle class  
class Battle:
    def __init__(self, p1_name, p1_attack, p1_health, p2_name, p2_attack, p2_health, e1_name, e1_attack, e1_health, e2_name, e2_attack, e2_health):
        self.p1_name = p1_name
        self.p1_attack = p1_attack
        self.p2_name = p2_name
        self.p2_attack = p2_attack
        self.e1_name = e1_name
        self.e1_attack = e1_attack
        self.e2_name = e2_name
        self.e2_attack = e2_attack
        self.p1_health = p1_health
        self.p2_health = p2_health
        self.e1_health = e1_health
        self.e2_health = e2_health
    def __repr__(self):
      return'\n{} and {} are going to fight EVIL!!'.format(self.p1_name, self.p2_name)
    def battle(self):
        print('\nEnemies {} and {} are fast approaching!'.format(self.e1_name, self.e2_name))
        enemies = [{'name': self.e1_name, 'health': self.e1_health, 'attack': self.e1_attack},{'name': self.e2_name, 'health': self.e2_health, 'attack': self.e2_attack}]
        players = [{'name': self.p1_name, 'attack': self.p1_attack},{'name': self.p2_name, 'attack': self.p2_attack}]

        while any(enemy['health'] > 0 for enemy in enemies):
            for player in players:
                choice = input(f"\n{player['name']}, which enemy will you attack ({self.e1_name}/{self.e2_name})? ")
                while choice not in [self.e1_name, self.e2_name]:
                    choice = input("Invalid choice. Please try again: ")

                for enemy in enemies:
                    if choice == enemy['name']:
                        enemy['health'] -= player['attack']
                        print(f"\n{player['name']} attacks {enemy['name']} for {player['attack']} damage.")
                        print(f"{enemy['name']} has {enemy['health']} health left.")
                        if enemy['health'] <= 0:
                            print(f"{enemy['name']} has been defeated!")
                            break

            if all(enemy['health'] <= 0 for enemy in enemies):
                print(f"\n{self.e1_name} and {self.e2_name} have been defeated!")
                break

#making player path function
def set_path(player,path_choice):
    if path_choice == 'beserker':
        player.path = path_beserker.name
        player.health = path_beserker.health
        player.agility = path_beserker.agility
    elif path_choice == 'thief':
        player.path = path_thief.name
        player.health = path_thief.health
        player.agility = path_thief.agility
    elif path_choice == 'warrior':
        player.path = path_warrior.name
        player.health = path_warrior.health
        player.agility = path_warrior.agility
    else:
        print('\nAn error has occured')  


#defining paths
path_beserker = path('beserker', 150, 50)
path_thief = path('thief', 50, 150)
path_warrior = path('warrior', 100, 100)  

#getting names
player_one_name = input('\nHello adventurer, welcome to honneywood, what is your name?')
player_two_name = input('\nAnd who is your companion?')
print('\n\nAh yes {} and {}, I Thought it was you!'.format(player_one_name, player_two_name))

#quest one
def Quest_start(name):
    quest_start = input('\nThese are troubling times, we have a big problem {} and {}, will you help us with the {} Quest?(Y/N)'.format(player_one_name, player_two_name, name))
    try:
        while quest_start not in ['Y', 'N']:
            quest_start = input('Please answer with Y or N')
    except Exception as e:
        print('Error')
    if quest_start == 'Y':
        return 'Y'
    
    elif quest_start == 'N':
        print('\nI am very dissappointed in you adventurer, you dare turn your back on the people of honneyWOOD!?\n I WILL MAKE YOU PAY... \nGUARD!!!')
        print('\n*** The Guard hits you so hard with his sword there is nothing to recover ***')
    fatality_answer = input('''\nWell that didn't last long, do you wish to restart?''')

    try:
        while fatality_answer not in ['Y']:
            fatality_answer = input('\nPlease press Y')
    except Exception as e:
        print('Error')
    if fatality_answer == 'Y':
       return 'fatality'
  
quest_one = Quest_start('starter')

while quest_one not in ['Y']:
    quest_one = Quest_start('starter')

print('''\nNow first, you must choose a path, it is the role you will embody, which determines your strength and agility the options are:''')
print('\n' + str(path_beserker) + '\n' + str(path_thief) + '\n' + str(path_warrior))

#chosing path and defining players
def path_choice(player):
    path_choice = input('\nwhich will it be, {}?'.format(player.name))
    while path_choice not in ['beserker', 'thief', 'warrior']:
      path_choice = input('\nNot in the options, please try again.')
    return path_choice

#first defining players
p1 = player(player_one_name)
p2 = player(player_two_name)

p1_path = path_choice(p1)
print ('\nand you?')
p2_path = path_choice(p2)

set_path(p1, p1_path)
set_path(p2, p2_path)
print('\nGood luck {} {} and {} {}'.format(p1.path, p1.name, p2.path, p2.name))

print(p1)
print(p2)

#defining enemies
e1 = enemy('Reven', 'thief')
e2 = enemy('Baffle', 'thief')

e1_path = 'thief'
e2_path = 'thief'

set_path(e1, e1_path)
set_path(e2, e2_path)

battle_one = Battle(p1.name, p1.attack, p1.health, p2.name, p2.attack, p2.health, e1.name, e1.attack, e1.health, e2.name, e2.attack, e2.health)
print(battle_one)
battle_one.battle()


print('\nThank you for playing this Demo of...')

print('''   _____      _ _          __   _____                                         
  / ____|    | | |        / _| |  __ \                                        
 | |     __ _| | |   ___ | |_  | |  | |_   _ _ __   __ _  ___  ___  _ __  ___ 
 | |    / _` | | |  / _ \|  _| | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __|
 | |___| (_| | | | | (_) | |   | |__| | |_| | | | | (_| |  __/ (_) | | | \__ |
  \_____\__,_|_|_|  \___/|_|   |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|___/
                                                    __/ |                     
                                                   |___/                      ''')
