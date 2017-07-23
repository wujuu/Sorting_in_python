import random

#CLASSES
class Array:
 
    def __init__(self,n):
        self.a=[]
        for i in range(0,n):
            self.a.append(random.randrange(0,1000))
        self.size=len(self.a)

    def print(self):
        print(self.a)

    def swap(self,i,j):
        x=self.a[j]
        self.a[j]=self.a[i]
        self.a[i]=x

    def reverse(self):
        self.a.reverse()

    def get_min(self,i=0):
        min=self.a[i]
        min_id=i
        for x in range(i+1,self.size):
            if self.a[x] < min:
                min=self.a[x]
                min_id=x
        return min_id

    def select_sort(self):
        for i in range(0,self.size):
            min_id=self.get_min(i)
            self.swap(i,min_id)

    def insert(self,id):
        next_id=0
        for i in range(0,id+1):
            if self.a[id] >= self.a[i]:
                next_id=i
                break

        for i in range(id,next_id-1):
            self.a[i]=self.a[i-1]

        self.a[next_id]=val
    
    def insert_sort(self):
        for i in range(1,self.size):
            self.insert(i)






#MAIN
T=Array(10)
T.print()
T.insert_sort()
T.print()




