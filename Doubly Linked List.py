'''Assignment-11: Write a program of Linked List where you can :
1. Insert a Node at the Beginning
2. Insert a Node at the End
3. Insert a Node in between two Data Nodes'''

#defining node class.
class Node:
    def __init__(self,dataval = None):
        self.preval = None
        self.dataval = dataval
        self.nextval = None

#defining Singly Linked list.
class DLinkedList:
    def __init__(self):
        self.headval = None

    #function to print values in forward direction.
    def listprintforward(self):
        printval = self.headval
        verify = printval.dataval
        c = 0
        while printval is not None:
            if verify == printval.dataval:
                c +=1
            if c > 1:
                break
            else:
                print(printval.dataval)
                printval = printval.nextval

    #function to print values in backward direction.
    def listprintbackward(self):
        printval = self.headval
        verify = printval.dataval
        c = 0
        while printval is not None:
            if verify == printval.dataval:
                c +=1
            if c > 1:
                break
            else:
                print(printval.dataval)
                printval = printval.preval

    #defining a function to create a node inbetween 2 nodes
    def add_inbetween(self):
        val = input("Enter the value for the node:\n")
        inb = Node(val)

        n1 = int(input("Enter the number of node 1: "))
        input("Enter the number of node 2: ")

        list = self.headval
        for i in range(0,n1):
            list = list.nextval

        inb.nextval = list.nextval
        inb.preval = list
        list.nextval = inb

#defining switch case function
def operations(opt,llist):

            if (opt < 1 & opt > 3):
                opt = 6

            match opt:

                case 1:
                    llist.add_inbetween()

                case 2:
                    llist.listprintforward()

                case 3:
                    llist.listprintbackward() 
                
                case 6:
                    print("Operation not valid. Please try again")

#getting the number of node user wants to create.
no_of_nodes = int(input("Enter the number of nodes you want to create: "))

#try-except block for creating list of nodes and inserting values in it.
try:

    #initializing Singly Linked List
    llist = DLinkedList()
    #getting the value and initalizing first node of the linked list.
    val = input("Enter value for Node 0: ")
    llist.headval = Node(val)

    #creating the list of nodes.
    no_of_nodes -= 1
    nodes = []
    for i in range(0, no_of_nodes):
        nodes.append("n"+str(i+1))
        i += 1

    #creating nodes and assigning values.
    for i in range(0, no_of_nodes):
        val = input("Enter the value for Node "+str(i+1)+": ")
        nodes[i] = Node(val)

    #creating link between nodes.
    llist.headval.nextval = nodes[0]
    llist.headval.preval = nodes[no_of_nodes-1]

    for i in range(0, no_of_nodes):
        if i == 0:
            tmp = llist.headval
            nodes[i].nextval = nodes[i+1]
            nodes[i].preval = tmp
        elif(i == len(nodes)-1):
            nodes[i].nextval = llist.headval
            nodes[i].preval = nodes[i-1]
        else:
            nodes[i].nextval = nodes[i+1]
            nodes[i].preval = nodes[i-1]
            
    #Providing users possible operations that can be done on the linked list.
    while True:

        print('You can perform this operations on the Linked List:\n1. Add a node inbetween the list.\n2. Print the contents of the list in forward direction.\n3. Print the contents of the list in backward direction\n4. Exit.')
        
        opt = int(input("Which operation you want to perform:\n"))
        if opt == 4:
            exit()
        else:
            operations(opt,llist)

except:
    pass 
