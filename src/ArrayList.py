import numpy as np
from typing import TypeVar, Generic
from numpy import dtype

T = TypeVar(' T ')


class ArrayLinerList(Generic[T]):
    
    #Constructor
    def __init__(self, initialCapacity: int) -> None:
        if (initialCapacity<1):
            raise Exception("No numbers below zero") 
        self.elements = np.empty([initialCapacity], dtype=np.object ) # array of elements
        self.size = 0 #Number of elements
    
    #Methods
    def push(self, item: T) -> None:
        self.elements[0] = item
        
    def pop(self) -> T:
        return self.elements[0]

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def size(self) -> int:
        return self.size
    
    def checkIndex(self, i: int) -> None:
        if(i<0 or i >= self.size):
            raise Exception("Index Out of bounds")
    
    def get(self, i: int) -> T:
        self.checkIndex(i)
        return self.elements[i]
    
    def indexOf(self, item: T) -> int:
        for i in range(0 , self.size-1):
            if item is self.elements[i]:
                return i;
        return -1;
    
    def remove(self, i: int) -> T:
        self.checkIndex(i)
        removedElement = self.elements[i]
        for j in range(i+1,self.size-1):
            self.elements[j-1] = self.elements[j]
        self.size = self.size - 1
        self.elements[self.size] = None
        return removedElement
    
    def add(self,i : int, t : T):
        if (i<0 or i > self.size):
            raise Exception("Index out of Bounds")
        if(self.size == self.elements.size):
            old = self.elements.copy()
            self.elements = np.empty([old.size*2], dtype=np.object)
            self.elements[0:old.size] = old
        for j in range(self.size-1,i-1,-1):
            self.elements[j+1] = self.elements[j]
        
        self.elements[i] = t
        self.size = self.size + 1
    

    
    def __str__(self):
        string = ' [ '
        for i in range(0,self.size):
            string = string + str(self.elements[i]) + '  ;  '
        
        string = string +  ' ] '
        return string
