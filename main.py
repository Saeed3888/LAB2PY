# Author: Saeed Alyami ssa5468@psu.edu
# Collaborator: Dominic Veneziale dbv5102@psu.edu
# Collaborator: Alsou Umarova afu5048@psu.edu 
# Collaborator: Michael Li mz15907@psu.edu
# Section: 3
#Breakout: 1

def getLetterGrade(grade):
  letter = " "
  if grade >= 93 and grade <= 100:
    letter = "A"
  elif grade >= 90 and grade < 93:
    letter = "A-"
  elif grade >= 87 and grade < 90:
    letter = "B+"
  elif grade >= 83 and grade < 87:
    letter = "B"
  elif grade >= 80 and grade < 83:
    letter = "B-"
  elif grade >= 77 and grade < 80:
    letter = "C+"
  elif grade >= 70 and grade < 77:
    letter = "C"
  elif grade >= 60 and grade < 70:
    letter = "D"
  elif grade < 60:
    letter = "F"
  return letter 

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")
  

if __name__== "__main__":
  run() 
