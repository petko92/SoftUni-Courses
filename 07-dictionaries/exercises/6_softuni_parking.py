#Read user input
n = int(input())
#Logic
registered = {}

for _ in range(n):
    line = input().split()
    command = line[0]
    username = line[1]

    if command == "register":
        if username not in registered:
            license_plate = line[2]
            registered[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else: #already registered
            license_plate = line[2]
            print(f"ERROR: already registered with plate number {license_plate}")

    elif command == "unregister":
        if username in registered:
            print(f"{username} unregistered successfully")
            registered.pop(username)
        else: #not present in the database
            print(f"ERROR: user {username} not found")

#Extract data, Print output
for username, license_plate in registered.items():
    print(f"{username} => {license_plate}")


'''
6.	SoftUni Parking
SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
The program receives 2 types of commands:
•	"register {username} {license_plate_number}":
o	The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
"ERROR: already registered with plate number {license_plate_number}"
o	If the check above passes successfully, the user should be registered, so the system should print:
 "{username} registered {license_plate_number} successfully"
•	"unregister {username}":
o	If the user is not present in the database, the system should print:
"ERROR: user {username} not found"
o	If the check above passes successfully, the system should print:
"{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users and their license plates in the format:
•	"{username} => {license_plate_number}"
Input
•	First line: n - number of commands - integer
•	Next n lines: commands in one of the two possible formats:
o	Register: "register {username} {license_plate_number}"
o	Unregister: "unregister {username}"
The input will always be valid, and you do not need to check it explicitly.
Examples:
Input	                             Output
5
register John CS1234JS
register George JAVA123S
register Andy AB4142CD
register Jesica VR1223EE
unregister Andy	             John registered CS1234JS successfully
                             George registered JAVA123S successfully
                             Andy registered AB4142CD successfully
                             Jesica registered VR1223EE successfully
                             Andy unregistered successfully
                             John => CS1234JS
                             George => JAVA123S
                             Jesica => VR1223EE



4
register Jony AA4132BB
register Jony AA4132BB
register Linda AA9999BB
unregister Jony	             Jony registered AA4132BB successfully
                             ERROR: already registered with plate number AA4132BB
                             Linda registered AA9999BB successfully
                             Jony unregistered successfully
                             Linda => AA9999BB


6
register Jacob MM1111XX
register Anthony AB1111XX
unregister Jacob
register Joshua DD1111XX
unregister Lily
register Samantha AA9999BB	 Jacob registered MM1111XX successfully
                             Anthony registered AB1111XX successfully
                             Jacob unregistered successfully
                             Joshua registered DD1111XX successfully
                             ERROR: user Lily not found
                             Samantha registered AA9999BB successfully
                             Anthony => AB1111XX
                             Joshua => DD1111XX
                             Samantha => AA9999BB

'''