# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:40:03 2020

@author: DACR9
"""
import pandas as pd
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


SO2_P = Singlylist()
df = pd.read_excel('Dataproject.xlsx', sheet_name='Hoja1')
saturacion = df['Sa02'].values.tolist()
for elemento in saturacion :
    SO2_P.PushBack(elemento)
SO2_P.listprint()
