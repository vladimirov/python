command = ""
while True:
    command = input("").lower()
    if command == 'start':
        print('Car started! Ready to go!')
    elif command == 'stop':
        print('Car stopped.')
    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print('I dont understand')
