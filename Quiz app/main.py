from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating the question bank to store the question-answer pairs
question_bank = []

# looping through all the data in the question list and appending them to the question bank
for item in question_data:
    question_text = item['text']
    question_answer = item['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

