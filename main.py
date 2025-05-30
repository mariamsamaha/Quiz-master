import Input
answer=Input.takeInput()
if answer.lower() == 'a' or answer.lower() == 'math':
    answerr=Input.takeInput2()
    if answerr.lower() == 'a' or answerr.lower() == 'easy':
        import matheasy
        matheasy.matheasy1()
        print('thanks for filling the quiz')
    else:
        import Mathmedium
        Mathmedium.mathmedium1()
        print('thanks for filling the quiz')

else:
    answerr=Input.takeInput2()
    if answerr.lower() == 'a' or answerr.lower() == 'easy':
        import biologyeasy
        biologyeasy.biologyeasy1()
        print('thanks for filling the quiz')
    else:
        import biologymedium
        biologymedium.biologymedium1()
        print('thanks for filling the quiz')


surveyquestion = input('what is your opinion in our app? and from your point of view how can we make it better?')
print('end of the questions!thanks for answering the quiz.hope to see you again')
