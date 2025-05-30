def gpa_calculator(percentage):
    z=percentage
    if percentage >= 90 :
               print('excellent,keep going')
    elif 90 >= percentage >= 80:
               print('very good')
    elif 80 >= percentage >= 70:
               print('good')
    elif 70 >= percentage >= 60:
               print('fair,practise more')
    else :
               print('sorry you did not succeed, practise more')
