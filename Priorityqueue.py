# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:18:42 2020

Heaps and priorityqueue
@author: DACR9
"""

class Priorityqueue():
    def __init__(self,n=0):
        self.n = n
        self.Array = [None]*20
        self.size = 0
    def insertitem(self,x):
        self.Array[self.size]=x
        self.moveUp()
        self.size += 1
    def moveUp(self):
        child = self.size
        parent = int((child-1)/2)
        temp = self.Array[child]
        while(child > 0 and temp > self.Array[parent] ):
            self.Array[child]=self.Array[parent]
            child=parent
            parent = int((child-1)/2)
        self.Array[child]=temp
    def Removemax(self):
        if self.size == 0:
            return None
        Max = self.Array[0]
        self.Array[0]=self.Array[self.size-1]
        self.moveDown()
        self.size = self.size-1
        return Max
    def  moveDown(self):
        flag = False
        largest =0
        parent = 0
        child = 2*parent +1
        temp = self.Array[parent]
        while(child<self.size and not flag):
            largest = self.Array[child]
            if(child+1>self.size and self.Array[child+1]< self.Array [child]):
                largest=self.Array[++child]
            if(largest>temp):
                self.Array[parent]=largest
                parent = child
            else:
                flag=True
            child=2*parent+1;
        self.Array[parent]=temp
                


#cola = Priorityqueue(20)
#cola.insertitem(2)
#cola.insertitem(5)
#cola.insertitem(7)
#cola.insertitem(4)
#cola.insertitem(8)
#cola.insertitem(1)
#cola.insertitem(1)
#print(cola.Removemax())
#print(cola.Removemax())        
#print(cola.Removemax())
#print(cola.Removemax())    
#print(cola.Removemax())
#print(cola.Removemax())    
#print(cola.Removemax())
#print(cola.Removemax())    
#print("Hola")
            
        
        
        