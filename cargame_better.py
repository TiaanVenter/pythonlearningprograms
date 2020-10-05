u_command = ""
car_started = False
while True:
    u_command = input("> ").lower()
    if u_command == "start":
        if car_started:
            print("Car has already started!")
        else:
            car_started = True
            print("Car has started")
    elif u_command == "stop":
        if not car_started:
            print("Car has already stopped!")
        else:
            car_started = False
            print("Car has stopped")
    elif u_command == "quit":
        quit()
    elif u_command == "help":
        print("""
start - starts the car
stop - stops the car
quit - quits program
        """)
    else:
        print("Sorry, I don't understand.")

#important: in a loop, keep assignment to the loop using single equator operator, not double. That seems to only assign it inside the loop...strange