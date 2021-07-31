command =""
started = False
stopped = False
while True != "quit":
    command = input ("> ").lower()
    if command == "start":
        if started:
            print("Car is already started, idiot!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if stopped:
            print("Car needs to be on to be stopped, stupid")
        else:
            stopped = True
            print ("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car 
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry,I don't seem to understand ")