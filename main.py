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

class Questions:
    def __init__(self, question, answear):
        self.question=question
        self.answear=answear

    def getQuestion(self):
        return self.question

    def getAnswear(self):
        return self.answear

class HistoryQuestions(Questions):
    def __init__(self, question, *answear):
        super().__init__(question, answear)

class GeographyQuestions(Questions):
    def __init__(self, question, answear):
        super().__init__(question, answear)

class BiologyQuestions(Questions):
    def __init__(self, question, answear):
        super().__init__(question, answear)
    
H1 = HistoryQuestions("Who was the first President of the United States?",
                       "George Washington")
H2 = HistoryQuestions("In what year did Christopher Columbus first arrive in the Americas?",
                       "1492")
H3 = HistoryQuestions("Which ancient civilization built the Great Pyramid of Giza?",
                       "Ancient Egyptians")
H4 = HistoryQuestions("What event marked the start of World War I?",
                       "Assassination of Archduke Franz Ferdinand")
H5 = HistoryQuestions("What document declared the American colonies independent from Great Britain?",
                       "Declaration of Independence")
H6 = HistoryQuestions("Who is known for leading the civil rights movement in the United States?",
                       "Martin Luther King Jr.")
H7 = HistoryQuestions("Which famous explorer completed the first circumnavigation of the Earth?",
                       "Ferdinand Magellan")
H8 = HistoryQuestions("What major conflict took place between the Northern and Southern states of the USA from 1861 to 1865?",
                       "American Civil War")
H9 = HistoryQuestions("What ancient wonder was a colossal statue of the Greek god Zeus?",
                       "Statue of Zeus at Olympia")
H10 =HistoryQuestions("Which queen is known for her reign during the Victorian era?",
                       "Queen Victoria")

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


historyQuestions=[H1.question,H2.question,H3.question,H4.question,
                  H5.question,H6.question,H7.question,H8.question,H9.question,B10.question]
historyAnswers=[H1.answear,H2.answear,H3.answear,H4.answear,
                H5.answear,H6.answear,H7.answear,H8.answear,H9.answear,H10.answear]

biologyQuestions=[B1.question,B2.question,B3.question,B4.question,
                  B5.question,B6.question,B7.question,B8.question,B10.question]
biologyAnswers=[B1.answear,B2.answear,B3.answear,B4.answear,
               B5.answear,B6.answear,B7.answear,B8.answear,B10]

geographyQuestions = [G1.question, G2.question, G3.question, G4.question,
                    G5.question, G6.question, G7.question, G8.question, G9.question, G10.question]

geographyAnswers = [G1.answear, G2.answear, G3.answear, G4.answear,
                    G5.answear, G6.answear, G7.answear, G8.answear, G9.answear, G10.answear]


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
    print("What Quizz do you want to start:")
    print("1. History")
    print("2. Biology")
    print("3. Geography")
    print("4. Mixed")
    option=input("1/2/3/4: ")
    if option=="History":
        return historyQuizz()
    
def historyQuizz():
    print("Starting quizz:")
    for question in historyQuestions:
        print(question)


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