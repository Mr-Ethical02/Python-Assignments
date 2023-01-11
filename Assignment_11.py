'''Assignment-11: Write a program of Linked List where you can :
1. Insert a Node at the Beginning
2. Insert a Node at the End
3. Insert a Node in between two Data Nodes'''

#defining node class.
class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None

#defining Singly Linked list.
class SLinkedList:
    def __init__(self):
        self.headval = None

    #function to print values.
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    #defining a funcction to add node at the beginning.
    def addstart(self):
        val = input("Enter the value for the node:\n")
        n = Node(val)
        n.nextval = self.headval
        self.headval = n
    
    #defining a function to add node at the end.
    def addend(self):
        val = input("Enter the value for the node:\n")
        end = Node(val)
        printval = self.headval
        while(printval.nextval):
            printval = printval.nextval
        printval.nextval = end
    
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
        list.nextval = inb

#defining switch case function
def operations(opt,llist):

            if (opt < 1 & opt > 5):
                opt = 6

            match opt:

                case 1:
                    llist.addstart()

                case 2:
                    llist.addend()

                case 3:
                    llist.add_inbetween()
                
                case 4:
                    llist.listprint()
                
                case 5:
                    exit()

                case 6:
                    print("Operation not valid. Please try again")

#getting the number of node user wants to create.
no_of_nodes = int(input("Enter the number of nodes you want to create: "))

#try-except block for creating list of nodes and inserting values in it.
try:

    #initializing Singly Linked List
    llist = SLinkedList()
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
    for i in range(0,no_of_nodes):
        if i+1 == no_of_nodes:
            break
        else:
            nodes[i].nextval = nodes[i+1]
    #Providing users possible operations that can be done on the linked list.
    while True:

        print('You can perform this operations on the Linked List:\n1. Add a node at the beginning of list.\n2. Add a node at the end of list.\n3. Add a node inbetween the list.\n4. Print the contents of the list.\n5. Exit.')
        
        opt = int(input("Which operation you want to perform:\n"))

        operations(opt,llist)

except:
    pass 
