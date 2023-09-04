import random

def enter():
    x=input("Do you already have an account?  Y/N: ")
    if x.upper() == "Y":
        login()
    if x.upper() == "N":
        register()

#gets all usernames and passwords into 2 lists
#do the same thing for date of birth
f=open("users.txt","rt")
usersAndPasswordsAndBirthdays=f.readlines()
userNames  =  [x.split("-")[0] for x in usersAndPasswordsAndBirthdays]
userPasswords=[x.split("-")[1].strip("\n") for x in usersAndPasswordsAndBirthdays]
userBirthdays=[x.split("-")[2].strip("\n") for x in usersAndPasswordsAndBirthdays]

print(userNames)
print(userPasswords)
print(userBirthdays)
f.close()


def login():
    while True:
        print("Log in: ")
        username=input("Username: ")
        password=input("Password: ")

        if username in userNames:
            index= userNames.index(username)

            if password == userPasswords[index]:
                print("You logged in!")
                break
            else: print("Your password is incorrect")

        else: print("Your username is incorrect")
    return options()
        
        
def register():
    while True:
        print("Register:")  
        username = input("Username: ")
        if username in userNames:
            print("This username is already taken:")
        else: break

    global password
    password=input("Password: ")
    print("Put your date pf birth")

    day=input("Day: ")
    month=input("Month: ")
    year=input("Year: ")
    global dateOfBirth
    dateOfBirth=f"{day}.{month}.{year}"
    

    f=open("users.txt","a")
    f.write(f"\n{username}-{password}-{dateOfBirth}")
    userNames.append(username)
    userPasswords.append(password)
    userBirthdays.append(dateOfBirth)
    return login()

f.close()

mathQuestions=[]
mathAnswers=[]

geographyQuestions=[]
geographyAnswers=[]

biologyQuestions=[]
biologyAnswers=[]

class Questions:
    def __init__(self, question, answer):
        self.question=question
        self.answer=answer

    def getQuestion(self):
        return self.question

    def getAnswear(self):
        return self.answer

class MathQuestions(Questions):
    def __init__(self, question, answer):
        super().__init__(question, answer)

        mathQuestions.append(self.question)
        mathAnswers.append(self.answer)

class GeographyQuestions(Questions):
    def __init__(self, question, answer):
        super().__init__(question, answer)

class BiologyQuestions(Questions):
    def __init__(self, question, answer):
        super().__init__(question, answer)

          
    
M1 = MathQuestions("What is 2 + 2?", "4")
M2 = MathQuestions("What is 5 - 3?", "2")
M3 = MathQuestions("What is 10 divided by 2?", "5")
M4 = MathQuestions("What is 3 times 4?", "12")
M5 = MathQuestions("What is 8 squared?", "64")
M6 = MathQuestions("What is 20 percent of 50?", "10")
M7 = MathQuestions("What is 9 multiplied by 7?", "63")
M8 = MathQuestions("What is 15 divided by 3?", "5")
M9 = MathQuestions("What is 18 minus 9?", "9")
M10 = MathQuestions("What is 6 times 9?", "54")

G1 = GeographyQuestions("What is the capital of France?",
                         "Paris")
G2 = GeographyQuestions("Which river is the longest in Europe?",
                         "Volga")
G3 = GeographyQuestions("Which country is known as the 'Land of the Midnight Sun'?", 
                        "Norway")
G4 = GeographyQuestions("What is the largest island in the Mediterranean Sea?",
                         "Sicily")
G5 = GeographyQuestions("Which mountain range stretches across seven countries in Europe?",
                         "The Alps")
G6 = GeographyQuestions("Which European city is famous for its canals and gondolas?",
                         "Venice")
G7 = GeographyQuestions("What is the smallest independent country in the world by area?",
                         "Vatican City")
G8 = GeographyQuestions("Which river flows through the city of London?",
                         "River Thames")
G9 = GeographyQuestions("Which country is bordered by Germany, Austria, Slovakia, and Poland?", 
                        "Czech Republic")
G10 =GeographyQuestions("What is the official currency of the European Union?",
                         "Euro")

B1 = BiologyQuestions("What is the basic unit of life?",
                       "Cell")
B2 = BiologyQuestions("Which gas do plants use for photosynthesis?",
                       "Carbon Dioxide (CO2)")
B3 = BiologyQuestions("What is the largest organ in the human body?",
                       "Skin")
B4 = BiologyQuestions("What is the process by which organisms maintain a stable internal environment?",
                       "Homeostasis")
B5 = BiologyQuestions("Which molecule stores genetic information in cells?",
                       "DNA")
B6 = BiologyQuestions("What is the powerhouse of the cell?",
                       "Mitochondria")
B7 = BiologyQuestions("What process allows plants to make their own food using sunlight?",
                       "Photosynthesis")
B8 = BiologyQuestions("What is the process by which animals eliminate waste products?",
                       "Excretion")
B9 = BiologyQuestions("Which system is responsible for circulating blood throughout the body?",
                       "Circulatory System")
B10 = BiologyQuestions("What is the study of heredity and the variation of inherited characteristics?",
                         "Genetics")


print(mathQuestions)
print(mathAnswers)

def options():
    print("1. Start a new quiz")
    print("2. View the results of your past quizzes")
    #ce inseamna asta?
    print("3. View the top 20 for a specific quiz")
    print("4. Change settings. You can change your password and date of birth")
    print("5. Exit")

    option=input("1/2/3/4/5: ")
    #aici am ramas
    if option=="1":
        return quiz()

    elif option=="2":
        print("Results:")
    elif option=="3":
        print("Top 20: ")
    elif option=="4":
        return settings()
    else: exit()



def quiz():
    print("What Quiz do you want to start:")
    print("1. Math")
    print("2. Biology")
    print("3. Geography")
    print("4. Mixed")
    option=input("1/2/3/4: ")
    if option=="1":
        return mathQuiz()
    
def mathQuiz():
    x=0
    print("Starting quiz:")
    for question, answer in zip(mathQuestions, mathAnswers):
        userAnswer=input(question+": ")
        if userAnswer==answer:
            print("Correct")
            x+=1
        else: print("Incorrect")
    print(f"You got {x}/10 correct answers")

def biologyQuiz():
    print("Starting quiz:")
    for question, answer in zip(biologyQuestions, biologyAnswers):
        userAnswer=input(question+": ")
        if userAnswer==answer:
            print("Correct")
            x=0
            x+=1
        else: print("Incorrect")
        print(f"You got {x}/10 correct answers")

def geographyQuiz():
    print("Starting quiz:")
    for question, answer in zip(geographyQuestions, geographyAnswers):
        userAnswer=input(question+": ")
        if userAnswer==answer:
            print("Correct")
            x=0
            x+=1
        else: print("Incorrect")
        print(f"You got {x}/10 correct answers")

def settings():
    print("Settings:")
    print("1. Change password:")
    print("2. Change date of birth")
    option=input("1/2: ")
    #changing password
    if option=="1":
        print("Changing password...")
        newPassword=input("New Password: ")

        with open("users.txt", "r") as f:
            info=f.readlines()

        with open("users.txt", "w") as f:
            for line in info:
                update=line.replace(password, newPassword)
                f.write(update)
        print("Password changed successfully!")
        f.close()
    #changing birthday
    else: 
        print("New Date of Birth: ")
        day=input("Day: ")
        month=input("Month: ")
        year=input("Year: ")
        newBirthday=f"{day}.{month}.{year}"

        with open("users.txt", "r") as f:
            info=f.readlines()

        with open("users.txt", "w") as f:
            for line in info:
                update=line.replace(newBirthday, dateOfBirth)
                f.write(update)
        print("Birthday changed successfully!")
        f.close()

enter()