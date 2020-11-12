import numpy as np
from typing import TypeVar, Generic
from numpy import dtype

T = TypeVar(' T ')

class ArrayQueue(Generic[T]):
    def __init__(self, initialCapacity: int) -> None:
        if (initialCapacity<1):
            raise Exception("No numbers below zero")
        self.front = 0
        self.back = 0
        self.queue = np.empty([initialCapacity], dtype=np.object ) # array of elements
    
    def isEmpty(self):
        return self.back == self.front
    
    def getFrontElement(self) -> T:
        if (self.isEmpty()):
            return None
        else:
            return self.queue[(self.front+1) % self.queue.size]
        
    def put(self, element : T) -> None:
        if((self.back +1) % self.queue.size == self.front):
            newQueue = np.empty( self.queue.size * 2,dtype=np.object )
            start = (self.front +1 ) % self.queue.size
            if(start <2):
                newQueue[0:self.queue.size ] = self.queue[start:self.queue.size]
            else:
                newQueue[0:self.queue.size - start] = self.queue[start : self.queue.size ]
                newQueue[self.queue.size - start : self.back+2 ] = self.queue[0:self.back+1]
            self.front = newQueue.size -1
            self.back = self.queue.size -2
            self.queue = newQueue
        self.back = (self.back+1) % self.queue.size
        self.queue[self.back] = element
        
    def remove(self) -> T:
        if(self.isEmpty()):
            return None
        else:
            self.front = (self.front+1) % self.queue.size
            frontElement = self.queue[self.front]
            self.queue[self.front] = None
            return frontElement
        
        