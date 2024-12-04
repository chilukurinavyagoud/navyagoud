questions = ("Who is the first female president of india?:",
             "http://www.indiabix.com - is an example of what?",
             "What is part of a database that holds only one type of information?",
             "'OS' computer abbreviation usually means ?",
             "How many bits is a byte?")
options = (("A.Indira Gandhi" ,  "B.Sarojini naidu" , "C.Soniya Gandhi" , "D.Smt.Prathibha Patil"),
          ("A.URL" , "B.An access code" , "C.A directory" , "D.A server"),
          ("A.Report"  , "B.Field"  , "C.Record", "D.File"),
          ("A.Order of Significnce"  , "B.Open Software" ,  "C.Operating System"   "D.Optical Sensor"),
          ("A.4" ,  "B.8"  , "C.16"  , "D.32"))
answers =("D", "A", "B", "C" , "B")
guesses = [] #we are using list to append the list items
score = 0
questions_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)  
    
    guess =input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
       score+=1
       print("COREECT")
    else:
       print("INCOREECT")
       print(f"{answers[questions_num]} is correct answer")
    questions_num+=1

print("results")
print("answers:",end =" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:" , end = " ")
for guess in guesses:
    print(guess, end =" ")
print()
score = int(score/len(questions)*100)
print(f" total score is:{score}%")
