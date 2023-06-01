#This is your starter file for the creature battle project
#The lines that start with a # are comments and will not show up in your code
#You should utilize this feature to leave notes about what variables are for
#And what operations your code is performing

#Try to have your program be inutitive for the user to interact with

#import all libraries
import random, time, os, sys
play = True


#set up all functions

def typingPrint(text): #stuff i borrowed off the internet for typewriter effect {
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  value = input()  
  return value  # }

#initialize all classes
class Creature: #CREATURES CLASS OBJECT STUFF
    def __init__(self, name, spec, HP, ATK, DEF, SPE, moves):
        self.name = name
        self.spec = spec
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SPE = SPE
        self.moves = moves
        
class Moves: #MOVES FOR ATK
    def __init__ (self, name, acc, bp = None, bf = None, dbf = None, perc = None):
        self.name = name
        self.bp = bp
        self.acc = acc
        self.bf = bf
        self.dbf = dbf
        self.perc = perc
        
    def use(self, attacker, defender):
        typingPrint(f'\n{attacker.name} used {self.name}!')
        
        if random.randint(1, 100) < self.acc:
            if self.bp:
                damage = self.damageCalc(attacker, defender)
                defender.HP -= damage
                typingPrint(f'\n{defender.name} took {str(damage)} damage.')
                if defender.HP < 0:
                    typingPrint(f'\n{defender.name} has 0 HP left!')
                else:
                    typingPrint(f'\n{defender.name} has {defender.HP} HP left.')

            if self.bf:
                if self.bf == 'ATK':
                    self.applyBfATK(attacker)
                if self.bf == 'SPE':
                    self.applyBfSPE(attacker)
                if self.bf == 'DEF':
                    self.applyBfDEF(attacker)

            if self.dbf:
                if self.dbf == 'ATK':
                    self.applyDbfATK(defender)
                if self.dbf == 'SPE':
                    self.applyDbfSPE(defender)
                if self.dbf == 'DEF':
                    self.applyDbfDEF(defender)
        else:
            typingPrint(f'\n{self.name} missed!')

    def damageCalc(self, attacker, defender):
        #damage = int((((attacker.ATK*self.bp)/defender.DEF)/3)*round(random.uniform(0.8, 1.2), 5))# DAMAGE CALC
        ##new test damage
        damage =(round(random.uniform(4.5, 5.5), 5)*attacker.ATK*self.bp/(defender.DEF*50) + 5)
        if random.randint(1, 100) < 7:
            damage *= 2
            typingPrint('\nCritical hit!')
        ##ADD CRIT
        damage = round(damage)
        return (damage)

    def applyBfATK(self, attacker): #BF
        attacker.ATK *= self.perc
        typingPrint(f'\n{attacker.name}\'s {self.bf} stat was raised by {(self.perc*100)-100}%.')
    def applyBfSPE(self, attacker):
        attacker.SPE *= self.perc
        typingPrint(f'\n{attacker.name}\'s {self.bf} stat was raised by {(self.perc*100)-100}%.')
    def applyBfDEF(self, attacker):
        attacker.DEF *= self.perc
        typingPrint(f'\n{attacker.name}\'s {self.bf} stat was raised by {(self.perc*100)-100}%.')


    def applyDbfATK(self, defender): #DBF
        defender.ATK *= self.perc
        typingPrint(f'\n{defender.name}\'s {self.dbf} stat was lowered by {(1-self.perc)*100}%.')
    def applyDbfSPE(self, defender):
        defender.SPE *= self.perc
        typingPrint(f'\n{defender.name}\'s {self.dbf} stat was lowered by {(1-self.perc)*100}%.')
    def applyDbfDEF(self, defender):
        defender.DEF *= self.perc
        typingPrint(f'\n{defender.name}\'s {self.dbf} stat was lowered by {(1-self.perc)*100}%.')


def attack(attacker, defender): #FUNCTION FOR THE ATTACK SEQUENCE
    while True:
        movePick = typingInput(f'\n\n{attacker.name} Pick your move \n1: {attacker.moves[0].name} \n2: {attacker.moves[1].name} \n3: {attacker.moves[2].name} \nor \"?\" for info')
        if movePick in ['1', '2', '3']:
            movePick = int(movePick)
            movePick -=1
            attacker.moves[movePick].use(attacker, defender)
            break;
        elif movePick == '?': #print master list of all moves/what they do
            typingPrint('\nMOVE LIST')
            print('\nScratch: 45BP, 100% \nPound: 50BP, 95% \nLick: 60BP, 90% \nBite: 70BP, 80% \nDestroy: 100BP, 50% \n\nFire Punch: 35BP, 90%, de-buffs ATK \nIce Punch: 35BP, 95%, de-buffs SPE \nThunder Punch: 35BP, 90%, de-buffs DEF \n\nRampage Strike: 35BP, 90%, buffs ATK \nSpeedy Strike: 35BP, 95%, buffs SPE \nShield Strike: 35BP, 90%, buffs DEF \n\nHumiliate, 95%, great de-buff ATK \nHypnosis: 95%, great de-buff SPE \nTickle: 95%, great de-buff DEF \n\nPower Surge: 100%, great buff ATK \nVelocity Boost: 100%, great buff SPE \nFortify: 100%, great buff DEF')
            
        else:
            typingPrint('please enter a correct number\n')


#WHAT THE USER SEES
def interface():
    global player1
    global player2
    global player
    typingPrint('Welcome to Creature Battle™\n')
    while player < 3:
        #next: recieve number input (check for number), display info on selected creature, ask if user wants the creature to use
        creatures = {"1":tachom,"2":paradiddle,"3":vitrescible,"4":sedent,"5":adriat,"6":monachism}
        while True:
            typingPrint(f'\nplayer {player} Please select an option\n')
            typingPrint('1) Tachom: tank \n2) Paradiddle: quick \n3) Vitrescible: fragile \n4) Sedent: balanced \n5) Adriat: aggro \n6) Monachism: bully')
            choice = input()
            if choice in ["1", "2", "3", "4", "5", "6"]:
                if player == 1:
                    player1 = creatures[choice]
                    player += 1
                    break
                else:
                    if creatures[choice] == player1:
                        typingPrint('\nChoose a different Creature!')
                    else:
                        player2 = creatures[choice]
                        player += 1
                        break
            else:
                typingPrint("\nplease enter a correct number")
    

def battle(): #battle function
    while player1.HP > 0 and player2.HP > 0:
        if player1.SPE > player2.SPE: #player 1 faster
            attack(player1, player2)
            if player2.HP < 1: #check if creature dies before gets turn
                break
            attack(player2, player1)
        else: #player 2 faster or tie on speed
            attack(player2, player1)
            if player1.HP < 1: #check if creature dies before gets turn
                break
            attack(player1, player2)
    if player1.HP < 1:
        typingPrint(f'\n{player2.name} wins!')
    else:
        typingPrint(f'\n{player1.name} wins!')

# MOVES MVOES MVOES MOVES MOVES MOVESM OVES
#ATK moves
Scratch = Moves('Scratch', 100, bp=45)
Pound = Moves('Pound', 95, bp=50)
Lick = Moves('Lick', 90, bp=60)
Bite = Moves('Bite', 80, bp=70)
Destroy = Moves('Destroy', 50, bp=100)
#ATK/DBF moves
FirePunch = Moves('Fire Punch', 90, bp=35, dbf='ATK', perc=.50)
IcePunch = Moves('Ice Punch', 95, bp=35, dbf='SPE', perc=.50)
ThunderPunch = Moves('Thunder Punch', 90, bp=35, dbf='DEF', perc=.50)
#ATK/BF moves
RampageStrike = Moves('Rampage Strike', 90, bp=35, bf='ATK', perc=1.50)
SpeedyStrike = Moves('Speedy Strike', 95, bp=35, bf='SPE', perc=1.50)
ShieldStrike = Moves('Shield Strike', 90, bp=35, bf='DEF', perc=1.50)
#DBF moves
Humiliate = Moves('Humiliate', 95, dbf='ATK', perc=.25)
Hypnosis = Moves('Hypnosis', 95, dbf='SPE', perc=.75)
Tickle = Moves('Tickle', 95, dbf='DEF', perc=.25)
#BF moves
PowerSurge = Moves('Power Surge', 100, bf='ATK', perc=2)
VelocityBoost = Moves('Velocity Boost', 100, bf='SPE', perc=2)
Fortify = Moves('Fortify', 100, bf='DEF', perc=2)

#list of moves to assign
moves = [Scratch, Pound, Bite, Destroy, FirePunch, IcePunch, ThunderPunch, RampageStrike, SpeedyStrike, ShieldStrike, Humiliate, Hypnosis, Tickle, PowerSurge, VelocityBoost, Fortify]


#CREATURES CREATURES CREATUESC CREATURES CREATEUS


while play: #big loop to play again!
    player = 1

    rndMovePool = random.sample(moves, 3) #randomly picks 3 moves, different for every creature!
    tachom = Creature('Tachom', 'Tank', random.randint(40, 50), random.randint(4, 7), random.randint(8, 10), random.randint(1, 3), rndMovePool)
    rndMovePool = random.sample(moves, 3)
    paradiddle = Creature('Paradiddle', 'Quick', random.randint(30, 40), random.randint(1, 3), random.randint(4, 7), random.randint(8, 10), rndMovePool)
    rndMovePool = random.sample(moves, 3)
    vitrescible = Creature('Vitrescible', 'Fragile', random.randint(15, 30), random.randint(8, 10), random.randint(1, 3), random.randint(8, 10), rndMovePool)
    rndMovePool = random.sample(moves, 3)
    sedent = Creature('Sedent', 'Balanced', random.randint(30, 40), random.randint(4, 7), random.randint(4, 7), random.randint(4, 7), rndMovePool)
    rndMovePool = random.sample(moves, 3)
    adriat = Creature('Adriat', 'Aggro', random.randint(40, 50), random.randint(8, 10), random.randint(1, 3), random.randint(4, 7), rndMovePool)
    rndMovePool = random.sample(moves, 3)
    monachism = Creature('Monachism', 'Bully', random.randint(15, 30), random.randint(4, 7), random.randint(8, 10), random.randint(8, 10), rndMovePool)

    
    interface()
    typingPrint(f"-----------------\n{player1.name} vs {player2.name}!!!\n-------------------")
    battle()

    while True:
        again = typingInput('\nPlay again? Y/N').lower() #ask play again
        if again in ['y', 'n']:
            if again == 'n':
                typingPrint('Thank you for playing!')
                play = False
                break;
            break;
        else:
            typingPrint('Try again')

