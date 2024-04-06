#Excercise 1
message = input("Type word: ")

messageLength = len(message)
capitalCount = sum(1 for c in message if c.isupper())


vowels = ["a","e","i","o","u"]

vowelCount = 0
SameLetter = False
MessageList = []
SameList = []

for a in message:
    MessageList.append(a)
     
    if a in vowels or a in [x.upper() for x in vowels]:
         vowelCount += 1
   
for x in range(len(message)):

    letter = MessageList[x]
    MessageList.pop(x)
    if letter in MessageList:
        SameLetter = True
        if not letter in SameList:
            SameList.append(letter)
    MessageList.append(letter)

       
         
print("Capital Letters: ", capitalCount)
print("Other Characters: ", messageLength - capitalCount)
print("Vowels: ", vowelCount)
print("Consonants: ", messageLength - vowelCount)
print("Same letters: ", SameLetter, SameList)
print("Middle Letter: ", message[int(messageLength/2)])
print("Total letters: ", messageLength)

#Part 2

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(dicto):
   count = 0
   for x in dicto.keys():
       if dicto[x] == "online":
           count += 1
   return count

        
    
print("Online users: ", online_count(statuses))

