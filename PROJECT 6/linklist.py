class sRec: 
    def __init__(self, name):
        self.name = name
        self.courses = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def register(self, courses):
        self.courses = courses

    def __str__(self):
        return self.name + ": " + ", ".join(self.courses)
# This code defines several classes and functions to manage a list of students and their 
# courses. Here are some comments to explain each part of the code:

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
# This class defines a student record, with a name and a list of courses.

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData().getName() == item.getName():
                found = True
            else:
                if current.getData().getName() > item.getName():
                    stop = True
                else:
                    current = current.getNext()
        return found, current, stop

    def addNode(self, item):
        temp = Node(item)
        found, current, stop = self.search(item)
        if not found:
            if current == None:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current.getNext())
                current.setNext(temp)

    def delNode(self, item):
        found, current, stop = self.search(item)
        if found:
            if current == None:
                self.head = current.getNext()
            else:
                previous = self.head
                while previous.getNext() != current:
                    previous = previous.getNext()
                previous.setNext(current.getNext())

    def getCList(self, course):
        current = self.head
        result = []
        while current != None:
            if course in current.getData().courses:
                result.append(current.getData())
            current = current.getNext()
        return result

    def __str__(self):
        current = self.head
        result = []
        while current != None:
            result.append(str(current.getData()))
            current = current.getNext()
        return "\n".join(result)
# This class defines a node in a linked list, with a data field and a 
# pointer to the next node.

def readNames(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    students = []
    for line in lines:
        name = line.strip()
        students.append(sRec(name))
    return students
# This class defines an ordered linked list of student records.

def readCourses(filename, students):
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        parts = line.strip().split(":")
        name = parts[0].strip()
        courses = parts[1].strip().split(",")
        for student in students:
            if student.getName() == name:
                student.register(courses)


def main():
    students = readNames("studentNames21203.txt")
    readCourses("studentCourses21203.txt", students)
    orderedList = OrderedList()
    for student in students:
        orderedList.addNode(student)
    print("Initial student list:")
    print(orderedList)
    coursesToWithdraw = ["MAT252"]
    for course in coursesToWithdraw:
        studentsToWithdraw = orderedList.getCList(course)
        for student in studentsToWithdraw:
            student.courses.remove(course)
            print("Updated student list:")
            print(orderedList)
