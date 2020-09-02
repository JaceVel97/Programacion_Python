instruction = 'initial'
is_started = False
while instruction != 'quit':
    instruction = input('> ').lower()

    if instruction == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif instruction == 'start':
        if is_started:
            print('The car is already started')
        else:
            print('Car started...Ready to go!')
            is_started = True
    elif instruction == 'stop':
        if not is_started:
            print('The car is already stopped')
        else:
            print('Car stopped.')
            is_started = False
    elif instruction != 'quit':
        print("I don't undestand that..")
else:
    print('Program terminated')