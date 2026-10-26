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
def selection_sort(arr):
        l = len(arr)
        for  i  in range(l):
              s = i
              for j in range(i, l):
                        if arr[s]> arr[j]:
                            s = j
              if i != s:
                arr[i], arr[s] = arr[s],arr[i]
        return arr
        
# arr = [54, 12, 34, 56,33,11]
arr = [54, 12, 34, 56,33,11,75, 6,21,31,88,1,15,4,99,16 , 11]
arr.sort()
x = BubboleSort(arr)
start  = time.time()
# print(x.INS() ,time.time()-start)
print(selection_sort(arr))