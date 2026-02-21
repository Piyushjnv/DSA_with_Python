# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old."
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# print(dog1)  
# print(dog2)

list1 = [9,9,9,9,9,9,9]
list2 = [9,9,9,9]

re = str(int( "".join(map(str, list1))) + int( "".join(map(str, list2))))
re = [int(i) for i in list(re)]
print(re[::-1] == [8,9,9,9,0,0,0,1])

lidt =[]
for i in range(5):
    lidt.insert(0,i)
print(lidt)
# class ListNode(object):/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(lidt[0])
temp = head
for i in range(1,len(lidt)):

    temp.next = ListNode(lidt[i])
    temp = temp.next

temp1 = head
while temp1 is not None:
    print(temp1.val, end=" ")
    temp1 = temp1.next