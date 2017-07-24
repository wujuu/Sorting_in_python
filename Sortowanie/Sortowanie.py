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

    #doesn't work
    def insert_sort(self): 
        for i in range(1,self.size):
            tmp=self.a[i]
            for j in range(i-1,-1):
                if self.a[j] > tmp:
                    self.a[j+1]=self.a[j]
                else:
                    self.a[j+1]=tmp
                    break

    def bubble_sort(self):
        swap=True
        while swap==True:
            swap=False
            for i in range(0,self.size-1):
                if self.a[i] > self.a[i+1]:
                    self.swap(i,i+1)
                    swap=True

    def partition(self,start,end):
        x=self.a[end]
        i=start-1
        j=end+1

        while i<j:
            i+=1
            j-=1
            while self.a[i] < x:
                i+=1
            while self.a[j] > x:
                j-=1
            if i<j:
                self.swap(i,j)
        return j

    def quick_sort(self, start, end):

        if start < end:
            middle=self.partition(start,end)
            self.quick_sort(start,middle)
            self.quick_sort(middle+1,end)








                    





#MAIN
T=Array(10)
T.print()
T.bubble_sort()
T.print()




