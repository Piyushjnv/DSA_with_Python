import time 
import math

class BubboleSort:
    def __init__(self , arr):
            self.arr = arr

    def INS(self):
        ir = len(self.arr)
        for i in range(ir):
             pointer = 0
             for x in range(1,len(self.arr)-i):
                  a = self.arr[pointer]
                  b = self.arr[pointer + 1]
                  
                  if a >= b:
                       self.arr[pointer] = b
                       self.arr[pointer+1] = a
                #   print(self.arr, pointer)
                  if x < (len(self.arr)-1):
                     pointer = pointer+1
        return self.arr
arr = [54, 12, 34, 56,33,11,75, 6,21,31,88,1,15,4,99,16]
x = BubboleSort(arr)
start  = time.time()
print(x.INS() ,time.time()-start)