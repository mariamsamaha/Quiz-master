def biologymedium1():
   c=0
   sum=0

   #question one
   c=c+1
   print('1-which is the largest cell?')
   answer_1 = input('a)plant cell \n b)animal cell \n c)nerve cell \n :')
   if answer_1.lower() == 'b' or answer_1.lower() == 'animal cell':
    print('correct')
    sum=sum + 1
   else:
    print('Incorrect')
    print('The correct answer is animal cell')
    print("if you can’t make a mistake you can’t make anything")
     
                

    print()
                            
    #question two
    c=c+1
    print('2-characters are transmitted from parents to offspring which of the following is the unit of inheritance?')
    answer_2 = input('a)dna \n b)genes \n c)rna \n :')
    if answer_2.lower() == 'b' or answer_2.lower() == 'genes':
     print('correct')
     sum=sum + 1
    else:
     print('Incorrect')
     print('The correct answer is genes')
     print('When you reach the end of your rope, tie a knot and hang out')

     print()
                    
     #question Three
     c=c+1
     print('3-photosynthesis mostly occur in which part of the plants ?')
     answer_3 = input('a)leaves \n b)barks \n c)roots \n:')
     if answer_3.lower() == 'a' or answer_3.lower() == 'leaves':
      print('correct')
      sum=sum + 1
                
                
     else:
      print('Incorrect')
      print('The correct answer is leaves')
      print("If today you are a little bit better than you were yesterday, then that’s enough.")


      print()

     #question four
     c=c+1
     print('4-the element that is present in all organic molecules is?')
     answer_4 = input('a)hydrogen \n b)carbon \n c)oxygen \n:')
     if answer_4.lower() == 'b' or answer_4.lower() == 'carbon':
       print('correct')
       sum=sum + 1
                
     else:
       print('Incorrect')
       print('The correct answer is carbon')
       print("The two most important days in your life are the day you’re born and the day you find out why")

     print()

     #question five
     c=c+1
     print('5-which of the following is the only part that cannot repair itself?')
     answer_5 = input('a)teeth\n b)liver \n c)brain:')
     if answer_5.lower() == 'a' or answer_5.lower() == 'teeth':
         print('correct')
         sum=sum + 1
    
     else:
         print('incorrect')
         print('the correct answer is teeth')
         print('Opportunity does not knock, it presents itself when you beat down the door.')

     print()

     #question six
     c=c+1
     print('6-which four letters in the english alphabet are used to denote the genetic code?')
     answer_6 = input('a)a n d c\n b)r m o e\n c)a t c g\n')
     if answer_6.lower() == 'c' or answer_6.lower() == 'a t c g':
        print('correct')
        sum=sum + 1
    
     else:
        print('Incorrect')
        print('The correct answer is a t c g')
        print('Done is better than perfect.')



     print()

     #question seven
     c=c+1
     print("7-plants receive their nutrients mainly from?")
     answer_7 = input('a)soil \n b)atmosphere \n c)light\n:')
     if answer_7.lower() == 'a' or answer_7.lower() == 'soil':
        print('correct')
        sum=sum + 1
    
     else:
        print('Incorrect')
        print('The correct answer is soil')
        print('A winner is a dreamer who never gives up')

            

     print()

     #question eight
     c=c+1
     print("8-Phloem is a tissue found in?")
     answer_8 = input('a)mammals\n b)plants\n c)reproductive organs\n:')
     if answer_8.lower() == 'b' or answer_8.lower() == 'plants':
        print('correct')
        sum=sum + 1
    
     else:
         print('Incorrect')
         print('The correct answer is plants ')
         print('You can do anything you set your mind to.')

    

     print()


     #question nine
     c=c+1
     print('9- Pigmentation of skin is due to?')
     answer_9= input('a)lymphocytes\n b)monocytes\n c)melanocytes\n:')
     if answer_9.lower() == 'c' or answer_9.lower() == 'melanocytes':
          print('correct')
          sum=sum + 1
    
     else:
        print('Incorrect')
        print('The correct answer is melanocytes')
        print('This is a reminder to you to create your own rule book, and live your life the way you want it')

                

     print()

     #question ten
     c=c+1
     print('10-Movement of cell against concentration gradient is called?')
     answer_10= input('a)osmosis\n b)diffusion\n c)active transport d)passive transport :')
     if answer_10.lower() == 'c' or answer_10.lower() == 'active transport':
        print('correct')
        sum=sum + 1
    
     else:
        print('Incorrect')
        print('The correct answer is active transport')
        print('Today is your opportunity to build the tomorrow you want.')

    
   print()
   print('your score is :',sum)
   import percentagecalculator
   percentage=percentagecalculator.percentagecalculator1(sum,c)
   print('your percentage is :',percentage)
   import gpacalculator
   gpacalculator.gpa_calculator(percentage)
   return
   





