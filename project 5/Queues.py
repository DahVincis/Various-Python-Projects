import random

class Customer:
    def __init__(self, name, Atime):
        self.name = name
        self.Atime = Atime
        self.Wtime = 0  # wait time for the customer, initialized to 0
        self.Sertime = 0  # remaining service time for the customer, initialized to 0

class Queue:
    def __init__(self):
        self.items = []  # list to hold the customers in the queue
        self.teller = None  # variable to keep track of the currently attending customer, initially set to None
    
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.append(item)  # add the customer to the end of the queue
        
    def dequeue(self):
        if not self.teller:  # if no one is being attended
            self.teller = self.items.pop(0)  # attend the next customer by removing them from the front of the queue
            return self.teller
        else:
            return None  # can't dequeue because someone is being attended
    
    def size(self):
        return len(self.items)  # return the number of customers in the queue
    
Bqueue = Queue()  # create a new queue object called Bqueue
SimTime = 30  # set the simulation time to 30 minutes

def BankLoop():
    for Thismin in range(SimTime):  # loop through each minute of the simulation
        if random.randint(0, 1) == 1:  # generate a random number between 0 and 1, add a new customer to the queue if it's 1
            Cust_new = Customer('Customer {}'.format(Thismin), Thismin)
            Bqueue.enqueue(Cust_new)
            print("{} arrived at {} minutes".format(Cust_new.name, Cust_new.Atime))

        if Bqueue.teller:  # if there is a customer being attended
            Cust_next = Bqueue.teller  # get the next customer in line
            Wtime = Thismin - Cust_next.Atime - Cust_next.Sertime  # calculate the wait time for the customer
            if Wtime > 0:  # if there is a wait time
                Cust_next.Wtime = Wtime  # update the customer's wait time
                print('{} had to wait for {} minutes before being attended to.'.format(Cust_next.name, Cust_next.Wtime))
            Cust_next.Sertime -= 1  # reduce the remaining service time for the customer by 1
            if Cust_next.Sertime == 0:  # if the current customer's service time is over
                Bqueue.teller = None  # no one is being attended now
                print('{} is done and left the bank.'.format(Cust_next.name))
        else:  # if there is no customer being attended
            if not Bqueue.isEmpty():  # if there are customers in the queue
                Cust_next = Bqueue.dequeue()  # dequeue the next customer in line
                Cust_next.Sertime = random.randint(1, 10)  # set the service time for the customer randomly between 1 and 10 minutes
                print('{} is being attended for the next {} minutes.'.format(Cust_next.name, Cust_next.Sertime))
        if Bqueue.size() > 0:  # if there are still customers in the queue
            print('There are still {} customers in the queue'.format(Bqueue.size()))
        else:  # if there are no customers in the queue
            print('No customers in the queue.')
    
def main():
    BankLoop()

if __name__ == "__main__":
    main()
