import time 
import math

class BubboleSort:
    def __init__(self , arr):
            self.arr = arr

    def INS(self):
        ir = len(self.arr)
        for i in range(ir):
             for x in range(len(self.arr)-i-1):
                  if self.arr[x] >= self.arr[x + 1]:
                       self.arr[x],self.arr[x + 1] = self.arr[x + 1],self.arr[x]
        return self.arr
arr = [54, 12, 34, 56,33,11,75, 6,21,31,88,1,15,4,99,16]
x = BubboleSort(arr)
start  = time.time()
print(x.INS() ,time.time()-start)