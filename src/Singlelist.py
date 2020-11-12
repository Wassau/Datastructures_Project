# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:38:10 2020

@author: DACR9
"""

# Singly Linked- List
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class Singlylist():
    def __init__(self):
        self.head = None
        self.Tail = None
    def PushFront(self, item):
        New = Node(item)
        New.nextval = self.head
        self.head= New
        if (self.Tail == None) :
            self.Tail=self.head
    def PopFront(self):
        if (self.head == None) :
            print("Error: Empty lyst")
        else: 
            self.head = self.head.nextval
        if (self.head == None):
            self.Tail = None
    def PushBack(self,item):
        New = Node(item)
        New.nextval = None
        if self.Tail == None :
            self.head = New
            self.Tail= New
        else:
            self.Tail.nextval = New
            self.Tail = New
    def PopBack(self):
        if self.head == None :
            print("Error: Empty Lyst")
        if self.head == self.Tail :
            self.head = None
            self.Tail = None
        else:
            current = self.head
            while current.nextval.nextval is not None :
                current = current.nextval 
            current.nextval= None 
            self.Tail = current()     
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
        
        # Node.nextval = self.head()
        # self.head
Pila = Singlylist()
Pila.PushFront(5)
Pila.PushFront(7)
Pila.PushFront(10)
Pila.PushFront(15)
Pila.listprint()
Pila.PopFront()
print(" ")
Pila.listprint()


        
