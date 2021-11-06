from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import art

print(art[0])

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# If still have a questions in QuestionBank ask to user while there is nothing to ask.

while quiz.still_has_questions():
    quiz.next_question()

if quiz.score != quiz.question_number:
    print(art[1])
else:
    print(art[2])
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")


