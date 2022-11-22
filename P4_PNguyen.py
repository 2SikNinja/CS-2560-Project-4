#Authors: Peter Nguyen
#Assignment: Project #4
#Completed (or last revision): 11/22/22

import random
class Question:
     choices = []
     answer = int()
     def __Question__(self):
          print("Question message reached! \n")
     def addQuestion(self, q, c, a):
          self.question = q
          self.choices = c
          self.answer = a
     def getQuestion(self):
          print(self.question)
          for j in range(len(self.choices)):
               print(j + 1, ".)", self.choices[j])
     def getAnswer(self):
          return self.answer
class Student:
     name = "default name"
     id = "dummy mail"
     def setStudent(self, n, email):
          self.name = n
          self.email = email
          self.currentScore = 0
          self.highestScore = 0
     def setScore(self, s):
          self.currentScore = s
          if (s > self.highestScore):
               print("You did better than your last high score, nice work!")
               self.highestScore = s
     def getName(self):
          return self.name
     def getHS(self):
          return self.highestScore
class Test:
     QList = []
     SList = []
     def __Test__(self):
          print("Test message reached! \n")
     def addQuestion(self, q, c, a):
          question = Question()
          question.addQuestion(q, c, a)
          self.QList.append(question)
     def getTest(self):
          for i in range(len(self.QList)):
               self.QList[i].getQuestion()
               print("Right answer:", self.QList[i].getAnswer(),"\n")
     def takeTest(self, stu, count):
          score = 0
          temp = []
          print(stu.getName(), "is taking an exam")
          while count > 0:
               i = random.randint(0,19)
               while True:
                    if i not in temp:
                         temp.append(i)
                         break
                    i = random.randint(0,19)
               self.QList[i].getQuestion()
               ans = int(input("Your answer: "))
               if ans == self.QList[i].getAnswer():
                    score += 1
               print()
               count -= 1
          print("Test over, you got", score, "points")
          stu.setScore(score)
          print(stu.getName() + "'s highest score:", stu.getHS())

def main():
     test = Test()
     test.addQuestion("Q1: What does CPP stand for?", ["C++", "Cal Poly Pomona", "California Ping Pong", "Chrismas Professional Performace"], 2)
     test.addQuestion("Q2: How many people are on Earth now?", ["5 Billion", "6 Billion", "7 Billion", "8 Billion"], 4)
     test.addQuestion("Q3: Who is the current president?", ["Donald Trump", "Bill Clinton", "George Washington", "Joe Biden"], 4)
     test.addQuestion("Q4: When is Halloween?", ["Oct 30", "Oct 31", "Nov 1", "Dec 1"], 2)
     test.addQuestion("Q5: What is the phrase that children use to get candies during Halloween?", ["Give us the candies", "Candies please!", "Happy Halloween", "Trick or Treat"], 4)
     test.addQuestion("Q6: What does OOP stand for in CS major?", ["Object Oriented Programming", "Out of Print", "Order of the Phoenix", "Over Optimization Penalty"], 1)
     test.addQuestion("Q7: What year did World War II end in?", ["1941", "1943", "1945", "1947"], 3)
     test.addQuestion("Q8: What is the name of Simba's dad?", ["Mufasa", "Mastiff", "Marshal", "Marucs"], 1)
     test.addQuestion("Q9: Which song is a duet?", ["I Won't Say (I'm In Love)", "Part of Your World", "I See the Light", "Never Knew I Needed"], 3)
     test.addQuestion("Q10: Where is Lilo and Stitch set in?", ["California", "Ohio", "Indonesia", "Hawaii"], 4)
     test.addQuestion("Q11: How many movies does The Little Mermaid have?", ["1", "2", "3", "4"], 3)
     test.addQuestion("Q12: How many years was the genie in Aladdin stuck in the lamp?", ["1,000","10,000","5,000","2,000"], 2)
     test.addQuestion("Q13: Who played the role of Maui in Moana?", ["Jack Black", "Dwayne 'The Rock' Johnson", "John Cena", "Ryan Reynolds"], 2)
     test.addQuestion("Q14: What Pokemon is Yellow?", ["Gyrados", "Pikachu", "Charmander", "Bulbasaur"], 2)
     test.addQuestion("Q15: What Pokemon is fire type?", ["Alakazam", "Snivy", "Bidoof", "Charmander"], 4)
     test.addQuestion("Q16: Who is the main character in the Pokemon TV series?", ["Ash Ketchup", "Ash Ketchum","Ash Mustard", "Ashe Katchoo"], 2)
     test.addQuestion("Q17: What type is Gengar?", ["Ghost", "Fire", "Water","Grass"], 1)
     test.addQuestion("Q18: What type is Gyrados?", ["Electric", "Fire", "Dark", "Water"], 4)
     test.addQuestion("Q19: Which is the main Legendary Pokemon in Pokemon Platinum?", ["Girantina", "Dialga","Palkia","Lugia"], 1)
     test.addQuestion("Q20: How many Pokemon are there in Generation 1?", ["132","164","151","142"], 3)
     s1 = Student()
     while True:
          selection = input("Welcome to the random multiple choice\n"\
          "Would you like to take / retake the test? [Y/N]: \n")
          if selection == 'Y' or selection == 'y':
               print("\n")
               print("Begin Test")
               try:
                    name = input("Student name: ")
                    s1.setStudent(name, input("Student email: "))
               except ValueError:
                    print("Invalid ID entered. ID has been set to 1234")
               test.takeTest(s1,5)
          elif selection == 'N' or selection == 'n':
               print("That's okay, see you later! \n")
               break
          else:
               print("Invalid input. \n")
main()
          
          
          
          
          
          
          
          
          
          
          
          
#Task 2
class Pair:
     x=0
     y=0
     def __init__(self, x, y):
          self.x=x
          self.y=y
    
    
        
     def __add__(self,o):
          return Pair(self.x+o.x,self.y+o.y)

     def __mul__(self,o):
          return Pair(self.x*o.x,self.y*o.y)

     def __truediv__(self,o):
          return Pair(self.x*self.y-o.x*o.y,self.x*o.x-self.y*o.y)
     
     def __str__(self):
          return "<"+str(self.x)+','+str(self.y)+">\n"
        
def main():
     p1=Pair(3,2)
     p2=Pair(1,5)
     p3=Pair(4,3)


     print(p1+p2)
     print(p1*p2)
     print(p1/p2)
     print(p1+p2*p3)
     print(p1*p2/p3+p1)



     #Test 1
     p1=Pair(5,7)
     p2=Pair(6,3)
     p3=Pair(9,0)


     print(p1+p2)
     print(p1*p2)
     print(p1/p2)
     print(p1+p2*p3)
     print(p1*p2/p3+p1)


     #Test 2
     p1=Pair(1,4)
     p2=Pair(3,2)
     p3=Pair(7,8)


     print(p1+p2)
     print(p1*p2)
     print(p1/p2)
     print(p1+p2*p3)
     print(p1*p2/p3+p1)

main()