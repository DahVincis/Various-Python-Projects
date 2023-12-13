def getdata():
    data = []
    with open("USPopulation.txt", "r") as file:
        for readr in file:
            population = int(readr.strip()) # remove leading/trailing whitespaces
            data.append(population)
    return data

def putdata(data):
    for population in data:
        print(population)

def annual_increase(data):
    annual_increase = []
    for i in range(1, len(data)):
        annual_increase.append(data[i] - data[i-1])
    return annual_increase

def main():
    data = getdata()
    putdata(data)
    annual_pop_increase = annual_increase(data)
    putdata(annual_pop_increase)
    maxIN = annual_pop_increase.index(max(annual_pop_increase))
    minIN = annual_pop_increase.index(min(annual_pop_increase))
    print("This year had the largest increase in population:", 1950 + maxIN + 1)
    print("This year had the smallest increase in population:", 1950 + minIN + 1)

if __name__ == "__main__":
    main()

# The function getdata() reads the contents of the file USPopulation.txt 
# and returns a list of populations. The function putdata(data) takes a 
# list as an argument and prints its contents. The function annual_increase(data) 
# calculates the annual increase in population and returns the results in a list. 
# The main() function calls the above functions and outputs the results to the shell.