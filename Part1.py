# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.
# Any code taken from other sources is referenced within my code solution.
prg=0
trai = 0
ret=0
exl=0
count =5
tot2 = 0
ans='y'
c_pass=0
ans1='y'
ans2 = True
totmarks=0
countX=0 
def rangeError():
    print('Out of range..')

def totincorrect():
    print('Total incorrect')
    
#askifg inputs from user
while ans =='y':
    
    try:
        while ans1=='y':
            c_pass=int(input('\nPlease enter your credits at pass:'))
            if (c_pass%20) !=0:
                rangeError()
            elif c_pass>120:
                totincorrect()
            else:
                break

        while ans1=='y':
            c_defer=int(input('Please enter your credits at defer:'))
            if (c_defer%20) !=0:
                rangeError()
            elif c_defer>120:
                totincorrect()
            else:
                break
        while ans1=='y':
            c_fail=int(input('Please enter your credits at fail:'))
            if (c_fail%20) !=0:
                rangeError()
            elif c_fail>120:
                totincorrect()
            else:
                break
        print()

        
        totmarks=c_pass+c_defer+c_fail
        
        #check the suitable outcome
        if totmarks ==120:
            

            if c_pass==120:   
                print('Progress')
                prg+=1

            elif c_pass==100:
                print('Progress (module trailer)')
                trai+=1

            elif c_fail <= 60:
                print('Do not Progress – module retriever')
                ret+=1

            elif c_fail >=80:
                print('Exclude')
                exl+=1

        else:
            print('Total incorrect')
            
      
    except ValueError:
        print('Integer required')

      

    except ValueError:
        print('Integer required')

    while True:
        #asking from user to enter data again
        print('\nWould you like to enter another set of data ?')

        ans = str(input('Enter y for yes or q to quit and view results '))

        if ans == 'y':
                break
        #print the horizontal histogram
        elif ans=='q':
            print('-------------------------------------------------------------')
            print('Horizontal Histogram')
            print('progress  ', prg,':',end='')
            for co in range(1, prg+1):
                print('*', end='')
                co+=1
            
            print('\nTrailer   ',trai,':',end='')
            for co in range(1, trai+1):
                print('*', end='')
                co+=1
            print('\nRetriever ',ret,':',end='')
            for co in range(1, ret+1):
                print('*', end='')
                co+=1
            print('\nExcluded  ',exl,':',end='')
            for co in range(1, exl+1):
                print('*', end='')
                co+=1        
            tot2 = prg + trai+ ret + exl

            print('\n\n',tot2,'outcomes in total')
            print('-------------------------------------------------------------')
            break

        else:
            print('invalid input')
