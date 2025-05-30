def biologyeasy1() :
            sum = 0
            c=0
            
            #question one
            c=c+1
            print('1-ability to adjust to living with nature is ?')
            answer_1 = input('a)attempt \n b)adaption \n c)fighting \n :')
            if answer_1.lower() == 'b' or answer_1.lower() == 'adaption':
               print('correct')
               sum=sum + 1

            else:
               print('Incorrect')
               print('The correct answer is adaption')
               print("if you can’t make a mistake you can’t make anything")
     

            print()


            #question two
            c=c+1
            print('2-worms breathe through?')
            answer_2 = input('a)Gill \n b)lungs \n c)skin \n d)mouth \n:')
            if answer_2.lower() == 'c' or answer_2.lower() == 'skin':
                print('correct')
                sum=sum + 1

            else:
                print('Incorrect')
                print('The correct answer is skin')
                print('When you reach the end of your rope, tie a knot and hang out')

            print()

            #question Three
            c=c+1
            print('3- below is a ruminant animal is ?')
            answer_3 = input('a)cow \n b)cat \n c)dog \n:')
            if answer_3.lower() == 'a' or answer_3.lower() == 'cow':
                print('correct')
                sum=sum + 1


            else:
                print('Incorrect')
                print('The correct answer is cow')
                print('It is hard to fail, but it is worse never to have tried to succeed')


            print()

            #question four
            c=c+1
            print('4- below vertebrates is ?')
            answer_4 = input('a)stingrays \n b)snake \n c)all wrong \n:')
            if answer_4.lower() == 'b' or answer_4.lower() == 'snake':
                print('correct')
                sum=sum + 1

            else:
                print('Incorrect')
                print('The correct answer is snake')
                print('Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle')



            print()

            #question five
            c=c+1
            print('5- Incubating chicken eggs for 21 days ? ?')
            answer_5 = input('a)true\n b)false \n:')
            if answer_5.lower() == 'a' or answer_5.lower() == 'true':
                print('correct')
                sum=sum + 1

            else:
                print('incorrect')
                print('the correct answer is true')
                print('Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle')
            


            print()

            #question six
            c=c+1
            print('6- plants below are heterotrophs  is ?')
            answer_6 = input('a)Bladderworts\n b)cape sundew \n c)all of the above\n:')
            if answer_6.lower() == 'c' or answer_6.lower() == 'all of the above':
                print('correct')
                sum=sum + 1

            else:
                print('Incorrect')
                print('The correct answer is all of the above')
                print('The only limit to our realization of tomorrow will be our doubts of today')



            print()

            #question seven
            c=c+1
            print("7- plants below are heterotrophs  is ?")
            answer_7 = input('a)lettuce \n b)spinach \n c)fungi\n:')
            if answer_7.lower() == 'c' or answer_7.lower() == 'fungi':
                print('correct')
                sum=sum + 1

            else:
                print('Incorrect')
                print('The correct answer is fungi')
                print('Perfection is not attainable, but if we chase perfection we can catch excellence')



            print()

            #question eight
            c=c+1
            print("8-who is the inventor of the theory of evolution?")
            answer_8 = input('a)Charles darwin\n b)stalin\n c)lenin\n:')
            if answer_8.lower() == 'a' or answer_8.lower() == 'charles darwin':
                print('correct')
                sum=sum + 1

            else:
                print('Incorrect')
                print('The correct answer is charles darwin')
                print('Out of difficulties grow miracles')



            print()

            #question nine
            c=c+1
            print('9- what is a sea cucumber?')
            answer_9= input('a)a fish\n b)a marine invertebrate \n c)a seaweed\n:')
            if answer_9.lower() == 'b' or answer_9.lower() == 'a marine invertebrate':
                print('correct')
                sum=sum + 1

            else:
                print('Incorrect')
                print('The correct answer is a marine invertebrate')
                print('Ever tried. Ever failed. No matter. Try again. Fail again. Fail better.')




            print()

            #question ten
            c=c+1
            print('10- which of the following is a protein ?')
            answer_10= input('a)wool\n b)starch\n c)natural rubber :')
            if answer_10.lower() == 'c' or answer_10.lower() == 'natural rubber':
                print('correct')
                sum=sum + 1

            else:
                print('Incorrect')
                print('The correct answer is natural rubber ')
                print('Success is not final, failure is not fatal: it is the courage to continue that counts.')


            print()
            print('your score is :',sum)
            import percentagecalculator
            percentage=percentagecalculator.percentagecalculator1(sum,c)
            print('your percentage is :',percentage)
            import gpacalculator
            gpacalculator.gpa_calculator(percentage)
            return
