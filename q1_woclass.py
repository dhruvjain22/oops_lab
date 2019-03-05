from threading import Thread

def perfectDivisor(n,arr):          #function to find perfect Divisor
    Sum=0
    for i in range(1,n):
        if ((n%i) == 0):
            Sum += i
    arr.append(Sum)

def compare(csa,csb,arr):           
    if csa==arr[1] and csb==arr[0]:
        return True

def main():
    csa = int(input("No.1: "))
    csb = int(input("No.2: "))
    arr = []
    t1 = Thread(target=perfectDivisor, args=(csa,arr,))
    t2 = Thread(target=perfectDivisor, args=(csb,arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    if (True and compare(csa,csb,arr)):
        print (csa," and ",csb," are Amicable Numbers.\n")
    else:
        print ("Not Amicable Numbers\n")
    
while(1):
    main()
