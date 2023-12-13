#       Pedro Henrique Fernandes || CSC 212 || 03/21/2023
#       Project 4: Postfix notation evaluation (Stack) 

class Stack:        # create class stack with all functions
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

class Popush:
    def __init__(self, num1, num2, num3, num4):
        self.Elem1 = num1
        self.Elem2 = num2
        self.Elem3 = num3
        self.Elem4 = num4

    def Stack_create(self):     # Call Stack Class and create stack
        self.my_Stack = Stack()

    def Stack_firstPush(self):      # Push numbers 3,5,1
        self.my_Stack.push(self.Elem1)
        self.my_Stack.push(self.Elem2)
        self.my_Stack.push(self.Elem3)

    def Stack_firstPop(self):       # Pop 1 and 5 subtract and push the answer which is 4
        popdOne = self.my_Stack.pop()
        popdTwo = self.my_Stack.pop()
        num5 = popdTwo - popdOne
        self.my_Stack.push(num5)

    def Stack_secondPop(self):      # pop 4 and 3 and multiply, push the answer which is 12
        popdThree = self.my_Stack.pop()
        popdFour = self.my_Stack.pop()
        num6 = popdThree * popdFour
        self.my_Stack.push(num6)

    def Stack_secondPush(self):     # push 2
        self.my_Stack.push(self.Elem4)

    def Stack_thirdPop(self):      # pop 2 and 12 and add, push the answer which is 14
        popdFive = self.my_Stack.pop()
        popdSix = self.my_Stack.pop()
        num7 = popdFive + popdSix
        self.my_Stack.push(num7)
        
    def Stack_final(self):      # print the final value in the stack which is 14
        while not self.my_Stack.is_empty():
            print(self.my_Stack.pop())


def main():     # call all functions
    popush = Popush(3, 5, 1, 2)
    popush.Stack_create()
    popush.Stack_firstPush()
    popush.Stack_firstPop()
    popush.Stack_secondPop()
    popush.Stack_secondPush()
    popush.Stack_thirdPop()
    popush.Stack_final()

if __name__ == "__main__":
    main()
