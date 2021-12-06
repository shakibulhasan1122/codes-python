import json
import mysql.connector

#with open("fruits.txt","a") as myf:
 #   myf.write("\nlichie")

#with open("vegetables.txt", "r") as f:
    #v=f.read()
    #print(v)
  #  f.write(input("Vegetable name: "))
    
#i="garlic"
#for j in v:
 #   print(j)



data=json.load(open('data.json'))
a="alex"
b=input("Password: ")
if a in data:
    if b==data[a]:
        print("done")
    else:
        print("wrong")
    