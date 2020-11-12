import numpy as np
from typing import TypeVar, Generic
from numpy import dtype

T = TypeVar(' T ')

class ArrayStack(Generic[T]):
    def __init__(self, initialCapacity: int) -> None:
        if (initialCapacity<1):
            raise Exception("No numbers below zero")
        self.top = -1
        self.stack = np.empty([initialCapacity], dtype=np.object ) # array of elements
    
    def isEmpty(self):
        return self.top == -1
    
    def peek(self)->T:
        if(self.isEmpty()):
            raise Exception("Empty Stack")
        return self.stack[self.top]
    
    def push(self, element: T):
        if(self.top == self.stack.size -1):
            old = self.stack.copy
            self.stack = np.empty(old.size *2, dtype=np.object )
            self.stack[0:old.size] = old[0:old.size]
        self.stack[self.top] = element
        self.top = self.top + 1
    
    def pop(self)->T:
        if self.isEmpty():
            raise Exception("Empty stack")
        topElement = self.stack[self.top-1]
        self.top = self.top -1
        self.stack[self.top] = None
        return topElement
    
stack = ArrayStack(10)
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())





    