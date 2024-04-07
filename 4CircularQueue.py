class queue:
    def __init__(self,K):
        self.capacity=K 
        self.number=0
        self.array=[None]*K
        self.rear=self.front=-1
    
    def isEmpty(self):
        return self.number==0  
    def isFull(self):
        return self.number==self.capacity
    def enqueue(self,data):
        if self.isFull():
            print("Queue Full")
            return
        if self.isEmpty():
            self.front=self.rear=0 
        else:
            self.rear=(self.rear+1)%self.capacity 
        self.array[self.rear]=data 
        self.number+=1
        print("Current queue is:",self.array)
         
    def dequeue(self):
        if self.isEmpty():
            print("Queue Empty")
        value=self.array[self.front]
        self.array[self.front]=None 
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.capacity   
            self.number-=1
            print("current queue:",self.array)
            print("dequeued element:",value)
            return
    def rEle(self):
        if self.isFull():
            print("Queue is empty")
            return None
        else:
            ele=self.array[self.rear]
            print(ele," is rear element")
    def fEle(self):
        if self.isEmpty():
            print("Queue is empty")
            return None 
        else:
            ele=self.array[self.front]
            print(ele," is front element")
q=queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
q.enqueue(60)
q.dequeue()
q.fEle()
q.rEle()
