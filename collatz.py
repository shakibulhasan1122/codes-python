import sys

def collatz(num):
    if(num%2==0):
        print(num//2)
        return num//2
    else:
        print(3*num+1)
        return 3*num+1    

n=int(input())
m=collatz(n)
if(m==1):
    print(m,"Done")
    sys.exit()
else:    
    while True:
        m=collatz(m)    
        if(m==1):
            break
        else:
            continue    
    print("done")    