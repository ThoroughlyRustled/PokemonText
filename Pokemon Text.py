import random
 
gender = input('Hello. Are you a boy or a girl?\n')
user = input('What is your name?\n')
print ('Welcome to the world of Pokémon, ' + user +'.')
while 1:
    while 1:
        pokemon = input('Which Pokémon would you like to have? Bulbasaur, Squirtle, or Charmander?\n')
        if pokemon == 'Bulbasaur' or pokemon == 'bulbasaur' or pokemon == 'Squirtle' or pokemon == 'squirtle' or pokemon == 'Charmander' or pokemon == 'charmander': break
        else:
            print ('That was not one of the options, please pick again.')
    if pokemon == 'Bulbasaur' or pokemon == 'bulbasaur':
        print ('You now have a Bulbasaur!')
        pokemon = 'Bulbasaur'
        rivalPokemon = 'Charmander'
    elif pokemon == 'Squirtle' or pokemon == 'squirtle':
        print ('You now have a Squirtle!')
        pokemon = 'Squirtle'
        rivalPokemon = 'Bulbasaur'
    elif pokemon == 'Charmander' or pokemon == 'charmander':
        print ('You now have a Charmander!')
        pokemon = 'Charmander'
        rivalPokemon = 'Squirtle'
    nextStep = input('Press enter to continue.')
 
    rival = input('As you walk out into the world, your rival interrupts you. What was his name again?\n')
    print (rival + ' wants to battle with you. It looks like you don\'t have a choice. Prepare to fight.')
    preBattle = input('When you are ready to enter the fight, press enter.\n')
 
    print (user + ' sends out ' + pokemon + '.')
    print (rival + ' sends out ' + rivalPokemon + '.\n')
 
    Tackle = (1,2,3,4,5,6,7,8,9)
    VineWhip = (10,11,12,13,14,15)
    Bubble = (10,11,12,13,14,15)
    Ember = (10,11,12,13,14,15)
    health = 150
    rivalHealth = 150
 
    bulbasaurMoves = ['Tackle, Vine Whip']
    squirtleMoves = ['Tackle, Bubble']
    charmanderMoves = ['Tackle, Ember']
 
    rivalTackle = 'Tackle'
    rivalVineWhip = 'Vine Whip'
    rivalBubble = 'Bubble'
    rivalEmber = 'Ember'
 
    rivalBulbasaur = rivalTackle, rivalVineWhip
    rivalSquirtle = rivalTackle, rivalBubble
    rivalCharmander = rivalTackle, rivalEmber
 
    while 1:
        if pokemon == 'Bulbasaur':
            print ('What would you like to do?')
            print (bulbasaurMoves)
            while 1:
                attack = input('Type the move you want to use: ')
                if attack == 'Tackle' or attack == 'tackle' or attack == 'VineWhip' or attack == 'Vine Whip' or attack == 'vine whip': break
                else:
                    print ('Bulbasaur doesn\'t know that move. Please choose from one of the options.\n')
        if pokemon == 'Squirtle':
            print ('What would you like to do?')
            print (squirtleMoves)
            while 1:
                attack = input('Type the move you want to use: ')
                if attack == 'Tackle' or attack == 'tackle' or attack == 'Bubble' or attack == 'bubble': break
                else:
                    print ('Squirtle doesn\'t know that move. Please choose from one of the options.\n')
        if pokemon == 'Charmander':
            print ('What would you like to do?')
            print (charmanderMoves)
            while 1:
                attack = input('Type the move you want to use: ')
                if attack == 'Tackle' or attack == 'tackle' or attack == 'Ember' or attack == 'ember': break
                else:
                    print ('Charmander doesn\'t know that move. Please choose from one of the options.\n')
 
        if attack == 'Tackle' or attack == 'tackle':
            t = random.choice(Tackle)
            print ('You have dealt ' + str(t) + ' damage.')
            rivalHealth -= t
            print (rival + '\'s ' + rivalPokemon + ' has ' + str(rivalHealth) + ' health points left.\n')
        elif attack == 'Bubble' or attack == 'bubble':
            t = random.choice(Bubble)
            print ('You have dealt ' + str(t) + ' damage.')
            rivalHealth -= t
            print (rival + '\'s ' + rivalPokemon + ' has ' + str(rivalHealth) + ' health points left.\n')
        elif attack == 'VineWhip' or attack == 'Vine Whip' or attack == 'vine whip':
            t = random.choice(VineWhip)
            print ('You have dealt ' + str(t) + ' damage.')
            rivalHealth -= t
            print (rival + '\'s ' + rivalPokemon + ' has ' + str(rivalHealth) + ' health points left.\n')
        elif attack == 'Ember' or attack == 'ember':
            t = random.choice(VineWhip)
            print ('You have dealt ' + str(t) + ' damage.')
            rivalHealth -= t
            print (rival + '\'s ' + rivalPokemon + ' has ' + str(rivalHealth) + ' health points left.\n')
        else:
            print ('That was not one of the moves. Please choose from one of the options.\n')
           
        if rivalHealth <= 0:
            print ('Congratulations. You have won!')
            if gender == 'girl':
                print (rival + ': "What! Beaten by a girl!"')
        if rivalHealth <= 0: break
 
        phase1 = input('It is now ' + rival + '\'s turn. Press enter to continue.\n')
       
        if rivalPokemon == 'Bulbasaur':
            rivalAttack = random.choice(rivalBulbasaur)
            if rivalAttack == rivalTackle:
                rivalAttack = random.choice(Tackle)
                rivalAttack2 = 'Tackle'
            elif rivalAttack == rivalVineWhip:
                rivalAttack = random.choice(VineWhip)
                rivalAttack2 = 'Vine Whip'
        if rivalPokemon == 'Squirtle':
            rivalAttack = random.choice(rivalSquirtle)
            if rivalAttack == rivalTackle:
                rivalAttack = random.choice(Tackle)
                rivalAttack2 = 'Tackle'
            elif rivalAttack == rivalBubble:
                rivalAttack = random.choice(Bubble)
                rivalAttack2 = 'Bubble'
        if rivalPokemon == 'Charmander':
            rivalAttack = random.choice(rivalCharmander)
            if rivalAttack == rivalTackle:
                rivalAttack = random.choice(Tackle)
                rivalAttack2 = 'Tackle'
            elif rivalAttack == rivalEmber:
                rivalAttack = random.choice(Ember)
                rivalAttack2 = 'Ember'
           
        print (rival + '\'s ' + rivalPokemon + ' uses ' + rivalAttack2 + '.')
        if rivalAttack2 == 'Tackle':
            print (rivalPokemon + ' has dealt ' + str(rivalAttack) + ' damage.')
            health -= rivalAttack
            print ('Your ' + pokemon + ' has ' + str(health) + ' health points left.\n')
        elif rivalAttack2 == 'Vine Whip':
            print (rivalPokemon + ' has dealt ' + str(rivalAttack) + ' damage.')
            health -= rivalAttack
            print ('Your ' + pokemon + ' has ' + str(health) + ' health points left.\n')
        elif rivalAttack2 == 'Bubble':
            print (rivalPokemon + ' has dealt ' + str(rivalAttack) + ' damage.')
            health -= rivalAttack
            print ('Your ' + pokemon + ' has ' + str(health) + ' health points left.\n')
        elif rivalAttack2 == 'Ember':
            print (rivalPokemon + ' has dealt ' + str(rivalAttack) + ' damage.')
            health -= rivalAttack
            print ('Your ' + pokemon + ' has ' + str(health) + ' health points left.\n')
           
        if health <= 0:
            print ('Oh no! You have lost!')
        if health <= 0: break
 
    choice = input('Do you want a rematch? Yes(Y)/No(N)')
    if choice == 'Yes' or choice == 'yes' or choice == 'Y' or choice == 'y':
        continue
    else: 
        print("")
        