# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.
# Any code taken from other sources is referenced within my code solution.

#variable declaration
prg=0
trai = 0
ret=0
exl=0
tot2 = 0
ans='y'
c_pass=0
c_defer=0
c_fail=0
ans1='y'
totmarks=0
totcounts=0

def rangeError():
    print('Out of range..')

def totincorrect():
    print('Total incorrect')

 #asking for inputs from user   
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

        
        totmarks = c_pass + c_defer + c_fail
        
        if totmarks ==120:
            
            #checking the suitable progression outcome
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

    tot2 = prg + trai+ ret + exl#sum of total outcomes
    while True:
            print('\nWould you like to enter another set of data ?')

            ans = str(input('Enter y for yes or q to quit and view results '))#taking inputs from user

            if ans == 'y':
                    break

            elif ans=='q':
                totcounts = prg + trai + ret + exl

                totcount_list=[prg, trai, ret, exl]

                m=max(totcount_list)#get the maximun value
                
                print('-------------------------------------------------------------')
                print('Horizontal Histogram')
                print(' \nProgress ' ' Trailer ' ' Retriever '' Exclude ' '\n')

                #verticle histogram
                for total_count in range(0, m):
                    if prg > 0:
                        print('*', end="")
                        prg-=1
                    else:
                        print(' ', end="")

                    if trai > 0:
                        print('         *', end="")
                        trai-=1
                    else:
                        print('          ', end="")

                    if ret > 0:
                        print('            *', end="")
                        ret-=1
                    else:
                        print('             ', end="")

                    if exl > 0:
                        print('             *', end="")
                        exl-=1
                    else:
                        print('             ', end="")
                    print()

                
                
                #print the total outcomes
                print('\n\n',tot2,'outcomes in total')
                print('-------------------------------------------------------------')
                break

            else:
                print('invalid input')
