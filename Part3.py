# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.
# Any code taken from other sources is referenced within my code solution.

#declare variables
prg=0
trai = 0
ret=0
exl=0
tot2 = 0
ans='y'
c_pass=0
w1=0
w2=0
w3=0
w4=0
c_defer=0
c_fail=0
ans1='y'
totmarks=0
totcounts=0
list1=[]
list2=[]
list3=[]
list4=[]
def rangeError():
    print('Out of range..')

def totincorrect():
    print('Total incorrect')
    
#asking inputs from user
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
         #check the siutable outcome and append the marks into the list   

            if c_pass==120:   
                print('Progress')
                list1.append(c_pass)
                list1.append(c_defer)
                list1.append(c_fail)
                prg+=1

            elif c_pass==100:
                print('Progress (module trailer)')
                list2.append(c_pass)
                list2.append(c_defer)
                list2.append(c_fail)
                trai+=1

            elif c_fail <= 60:
                print('Do not Progress – module retriever')
                list3.append(c_pass)
                list3.append(c_defer)
                list3.append(c_fail)
                ret+=1

            elif c_fail >=80:
                list4.append(c_pass)
                list4.append(c_defer)
                list4.append(c_fail)
                print('Exclude')
                exl+=1

        else:
            print('Total incorrect')
            
      
    except ValueError:
        print('Integer required')

      

    except ValueError:
        print('Integer required')

    tot2 = prg + trai+ ret + exl
    while True:
            print('\nWould you like to enter another set of data ?')

            ans = str(input('Enter y for yes or q to quit and view results '))

            if ans == 'y':
                    break

            elif ans=='q':
                totcounts = prg + trai + ret + exl #get the total outcome


                
                print('-------------------------------------------------------------')

                #check the siutable outcome and print the marks and outcomes
                for total_count in range(0, totcounts):
                    if prg > 0:
                        print('\nprogress - ',end='')
                        for x in range(0,3):
                            print(list1[w1],',' ,end='')
                            w1+=1
                        prg-=1
                  
                    elif trai > 0:
                        print('\nProgress (module trailer) - ', end="")
                        for x in range(0,3):
                            print(list2[w2],',' ,end='')
                            w2+=1
                        trai-=1


                    elif ret > 0:
                        print('\nDo not progress – module retriever - ', end="")
                        for x in range(0,3):
                            print(list3[w3],',' ,end='')
                            w3+=1
                        ret-=1


                    elif exl > 0:
                        print('\nExclude - ', end="")
                        for x in range(0,3):
                            print(list4[w4],',' ,end='')
                            w4+=1
                        exl-=1

                    #print()

                
                

                print('\n\n',tot2,'outcomes in total')
                print('-------------------------------------------------------------')
                break

            else:
                print('invalid input')
