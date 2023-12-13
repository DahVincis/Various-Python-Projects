import random


def getdata():      # read file and enter state as key and city as value into dictionary
    data = {}
    with open("capitals of states.txt", "r") as file:
        for readr in file:
            cap1 = readr.rstrip("\n")
            city, state = cap1.split(", ")
            data[state] = city
    return data

def phaseOne(data):    # Phase one of game: asks user input, creates while loop that helps user practice for game

    while True:
        userIn = input("Please select a state or type 'exit' to go to the next phase!: ")
        stateVal = data.get(userIn)

        if userIn == "exit":
            break

        if stateVal is not None:
            print(f"The capital of {userIn} is {stateVal}")
        else:
            print(f"{userIn} is not a state! Please try again.")

def phaseTwo(data):         # Phase Two of game: gives random state name so the user can guess
    cityList = list(data.keys())
    randCity = random.choice(cityList)
    userIn2 = input(f"What is the capital of {randCity}?: ")

def main():     # Main that calls all functions
    data = getdata()
    phaseOne(data)
    phaseTwo(data)

if __name__ == "__main__":      # This thing
    main()
