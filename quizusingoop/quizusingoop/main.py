import question_model
from data import question_data
import quiz_brain

qbank=[]
for i in question_data:
    qbank.append(question_model.question(i['question'],i['correct_answer']))

qbrain=quiz_brain.Brain(qbank)
qbrain.nextques()