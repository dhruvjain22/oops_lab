from threading import Thread

class calculate:
    def __init__(self,csa,csb,arr):
        self.csa=csa
        self.csb=csb
        self.arr=arr
        
    def perfectDivisor(self,n):
        Sum=0
        for i in range(1,n):
            if ((n%i) == 0):
                Sum += i
        self.arr.append(Sum)
    
    def compare(self):
        if c.csa==c.arr[1] and c.csb==c.arr[0]:
            return True
        
def main():
    c.csa = int(input("No.1: "))
    c.csb = int(input("No.2: "))
    t1 = Thread(target=c.perfectDivisor, args=(c.csa,))
    t2 = Thread(target=c.perfectDivisor, args=(c.csb,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    if c.compare() and True:
        print (c.csa," and ",c.csb," are Amicable Numbers.\n")
    else:
        print ("Not Amicable Numbers\n")
    
    
c = calculate(0,0,[])
main()
