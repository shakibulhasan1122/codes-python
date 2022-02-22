book={"T1":' ',"T2":' ',"T3": ' ',"M1":' ',"M2":' ',"M3": ' ',"D1":' ',"D2":' ',"D3": ' '}

def check():
    if((book['T1']=='X' and book["T2"]=="X" and book["T3"]=="X") or 
    (book['M1']=='X' and book["M2"]=="X" and book["M3"]=="X") or
    (book['D1']=='X' and book["D2"]=="X" and book["D3"]=="X") or 
    (book['T1']=='X' and book["M2"]=="X" and book["D3"]=="X") or
    (book['D1']=='X' and book["M2"]=="X" and book["T3"]=="X") or
    (book['T1']=='X' and book["M1"]=="X" and book["D1"]=="X") or
    (book['T2']=='X' and book["M2"]=="X" and book["D2"]=="X") or
    (book['D3']=='X' and book["M3"]=="X" and book["T3"]=="X")):
        print("Team X wins")
        return 2
    elif ((book['T1']=='O' and book["T2"]=="O" and book["T3"]=="O") or 
    (book['M1']=='O' and book["M2"]=="O" and book["M3"]=="O") or
    (book['D1']=='O' and book["D2"]=="O" and book["D3"]=="O") or 
    (book['T1']=='O' and book["M2"]=="O" and book["D3"]=="O") or
    (book['D1']=='O' and book["M2"]=="O" and book["T3"]=="O") or
    (book['T1']=='O' and book["M1"]=="O" and book["D1"]=="O") or
    (book['T2']=='O' and book["M2"]=="O" and book["D2"]=="O") or
    (book['D3']=='O' and book["M3"]=="O" and book["T3"]=="O")):
        print("Team O wins")
        return 1
    else:
        return 0

print("T1","|","T2","|","T3")
print("___+____+___")
print("M1","|","M2","|","M3")
print("___+____+___")
print("D1","|","D2","|","D3")

print("*************************")
turn="X"
for i in range(9):        
    print("turn for "+turn)
    m=input("Enter place:")
    m=m.upper()
    book[m]=turn
    if turn=="X":
        turn='O'
    else:
        turn="X"
        

    print("*******************")
    print(book["T1"],"|",book["T2"],"|",book["T3"])
    print("__+___+___")
    print(book["M1"],"|",book["M2"],"|",book["M3"])
    print("__+___+___")
    print(book["D1"],"|",book["D2"],"|",book["D3"])
    res=check()
    print("********************************")
    if(res==2):
        break
    elif(res==1):
        break
    
if res==0:
    print("No winner")        

input("Press Enter to exit")    
