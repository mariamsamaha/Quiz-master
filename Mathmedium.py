def mathmedium1() :
   sum = 0
   c=0
   #question one
   c=c+1
   print('Find x, when x/9 = 18')
   answer_2 = input('a)152 \n b)162 \n c)142 \n d)172 \n:')
   if answer_2.lower() == 'b' or answer_2.lower() == '162':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is 162')
        print('Failure will never overtake me if my determination to succeed is strong enough')

   print()

   #question two
   c=c+1
   print('What is the 12th term of the sequence -2,-4,-6,...........-100?')
   answer_2 = input('a)-28 \n b)-26 \n c)-24 \n d)-20 \n:')
   if answer_2.lower() == 'c' or answer_2.lower() == '-24':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is -24')
        print('Most great people have attained their greatest success just one step beyond their greatest failure')

   print()

   #question three
   c=c+1
   print('Solve for x: 4x + 9 = 12')
   answer_2 = input('a)1/2 \n b)4 \n c)3 \n d)3/4 \n:')
   if answer_2.lower() == 'd' or answer_2.lower() == '3/4':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is 3/4')
        print('Failure is a detour; not a dead-end street')
   print()

   #question four
   c=c+1
   print('If x is any number, then x × ∞ is equal to?')
   answer_2 = input('a)0 \n b)1 \n c)∞ \n d)-∞ \n:')
   if answer_2.lower() == 'c' or answer_2.lower() == '∞':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is ∞')
        print('Even a failure feels like a success. At least you had the courage to try')
   print()

   #question five
   c=c+1
   print('If y = 6x + 4 is a line equation, then the intercept is:')
   answer_2 = input('a)1 \n b)4 \n c)6 \n d)None of these \n:')
   if answer_2.lower() == 'b' or answer_2.lower() == '4':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is 4')
        print('Failure should be our teacher, not our undertaker')
   print()

   #question six
   c=c+1
   print('The probability of getting number 10 in a throw of a dice is ____')
   answer_2 = input('a)0 \n b)1 \n c)0.5 \n d)0.75 \n:')
   if answer_2.lower() == 'a' or answer_2.lower() == '0':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is 0')
        print('You always pass failure on your way to success')

   print()

   #question seven
   c=c+1
   print('Combine terms: 12a + 26b -4b – 16a')
   answer_2 = input('a)4a + 22b \n b)-28a + 30b \n c)-4a + 22b \n d)28a + 30b \n:')
   if answer_2.lower() == 'c' or answer_2.lower() == '-4a + 22b':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is -4a + 22b')
        print('Mistakes are the portals of discovery')
   print()

   #question eight
   c=c+1
   print('What is the radius of a circle that has a circumference of 3.14 meters?')
   answer_2 = input('a)0.5 \n b)5/4 \n c)10 \n d)85 \n:')
   if answer_2.lower() == 'a' or answer_2.lower() == '0.5':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is 0.5')
        print('Our greatest glory is not in never failing, but in rising every time we fail')
   print()

   #question nine
   c=c+1
   print('Find the value of a, if a/2 = 15')
   answer_2 = input('a)15 \n b)14 \n c)30 \n d)25 \n:')
   if answer_2.lower() == 'c' or answer_2.lower() == '30':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is 30')
        print('Those who dare to fail miserably can achieve greatly')
   print()

   #question ten
   c=c+1
   print('If 72 x 96 = 6927, 58 x 87 = 7885, then 79 x 86 = ?')
   answer_2 = input('a)5620 \n b)2896 \n c)6897 \n d)2589 \n:')
   if answer_2.lower() == 'c' or answer_2.lower() == '6897':
        print('correct')
        sum= sum+1

   else:
        print('Incorrect')
        print('The correct answer is 6897')
        print('Failure does not mean you are a failure, it just means you haven’t succeeded yet')

   print()
   print('your score is :',sum)
   import percentagecalculator
   percentage=percentagecalculator.percentagecalculator1(sum,c)
   print('your percentage is :',percentage)
   import gpacalculator
   gpacalculator.gpa_calculator(percentage)
   return

