# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 07:49:02 2020

@author: DACR9
"""

class Stack():
    def __init__(self,top=0):
        self.item = []
        self._top = top
    def empty(self):
            return self._top <=0
    def pop (self):
        
        
        
        ultimo = self.item[self._top-1]
        self.item = self.item[:-1]
        self._top  -= 1
        return ultimo
        
        
    def push (self, item):
        
        #self.item[self._top]= item
        self._top += 1 
        self.item.append(item)
            
if __name__ == '__main__':
    n = int(input())
    Stack1 = Stack()
    Stack2 = Stack()
    for i in range (n):
        h1 = list(map(int, input().rstrip().split()))
        if h1[0] == 1 :
            Stack1.push(h1[1])
            if Stack2.empty():
                for j in range (len(Stack1.item)) :
                    Stack2.push(Stack1.item[(Stack1._top-1)-j])
            else:
                for j in range (len(Stack2.item)) :
                    Stack2.pop()
                for j in range (len(Stack1.item)) :
                    Stack2.push(Stack1.item[(Stack1._top-1)-j])
        if h1[0]==2:
            print(Stack2.pop())
            if Stack2.empty():
                Stack1.pop()
            else:
                for j in range (len(Stack1.item)) :
                    Stack1.pop()
                for j in range (len(Stack2.item)) :
                    Stack1.push(Stack2.item[(Stack2._top-1)-j])
        if h1[0]==3:
           if Stack2.empty():
                print("Stack Empty")
           else:
                print(Stack2.item[Stack2._top-1])
    