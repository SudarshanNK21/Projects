from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question['text']
    q_ans = question['answer']
    questions = Question(q_text,q_ans)
    question_bank.append(questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
