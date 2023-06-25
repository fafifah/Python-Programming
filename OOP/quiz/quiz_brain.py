class QuizBrain():
  def __init__(self,question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    current_question = self.question_list[self.question_number]
    current_answer = current_question.answer
    self.question_number += 1
    usr_response = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(usr_response,current_answer)
    

  
  
  def check_answer(self,response,answer):
    if response.lower() == answer.lower():
      self.score += 1
      print("You've got it right!")
    else:
      print("That's wrong.")
      
    print(f"The answer to the question was {answer}")
    print(f"Your score is: {self.score}/{self.question_number}")
    print("\n")
    
