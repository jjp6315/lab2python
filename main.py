# Author: Ji Woong Park jjp6315@psu.edu
# Collaborator: Mary Meier mrm6632@psu.edu
# Collaborator: Greg Dorazio gmd5474@psu.edu
# Collaborator: Alex Podlucky app5775@psu.edu
# Section: 005R (Sec 01-12)
# Breakout: 9
def getLetterGrade(grade):

  if grade >= 93.0:
    return "A"
  elif grade >= 90.0:
    return "A-"
  elif grade >= 87.0:
    return "B+"
  elif grade >= 83.0:
    return "B"
  elif grade >= 80.0:
    return "B-"
  elif grade >= 77.0:
    return "C+"
  elif grade >= 70.0:
    return "C"
  elif grade >= 60.0:
    return "D"
  else:
    return "F"

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade (grade)}.")

if __name__ == "__main__":
  run()