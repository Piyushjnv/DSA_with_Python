import time 
import math

class BubboleSort:
    def __init__(self , arr):
            self.arr = arr

    def INS(self):
        ir = len(self.arr)
        z = 0 
        for i in range(ir):
             y = 0
             for x in range(1,len(self.arr)-z):
                  a = self.arr[y]
                  b = self.arr[y + 1]
                  
                  if a >= b:
                       self.arr[y] = b
                       self.arr[y+1] = a
                #   print(self.arr, y)
                  if x < (len(self.arr)-1):
                     y = y+1
             z = z + 1
        return self.arr
arr = [54, 12, 34, 56,33,11,7, 75, 6,21,31,88,1,15,4,99,16]
x = BubboleSort(arr)
y  = time.time()
print(x.INS() , math(time.time()-y))