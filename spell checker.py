from textblob import TextBlob

x=input("Input a word:")

y=TextBlob(x)

print("Correct Spelling is: ",y.correct())
