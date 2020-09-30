started = False
while True:
    command = input(">").lower()
    if command =="start":
        if started:
            print("Car is already started..")
        else:
            started=True
            print('Car started')
    elif command =="stop":
        if not started:
            print("Car is already stopped. ")
        else:
            print("Car stopped")
    elif command=="help":
        print("Start - to start a car\nstop - to stop a car\nquit-to exit")
    elif command=="quit":
        break
    else:
        print("I did not understand that.")