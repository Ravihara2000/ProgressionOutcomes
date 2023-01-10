# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.
# Any code taken from other sources is referenced within my code solution.

#variable declaration
prg=0
trai = 0
ret=0
exl=0
tot2 = 0
ans='y'
cp=0
cd=0
cf=0
ans1='y'
totmarks=0
totcounts=0
credit_level=[]
marks=[]
count=0



def rangeError():
    print('Out of range..')

def totincorrect():
    print('Total incorrect')

Prog_Outcome={
    "progress": [],
    "module_trailer": [],
    "module_retriever": [],
    "exclude": [],
    
    }

def tot_check(t_pass,t_defer,t_fail):
    totmarks =t_pass + t_defer + t_fail
    
    if totmarks == 120:
        Vol_credit(t_pass,t_defer,t_fail)
    else:
        print('total incorrect')
        
def Vol_credit(_pass,_defer,_fail):
    global Prog_Outcome
    global count
    mark = {
        "pass": _pass,
        "defer":_defer,
        "fail": _fail
    }
    #check the suitable Progression Outcome   
    if _pass==120:
            print('progress')
            Prog_Outcome['progress'].append(mark)
            count+=1

    elif _pass==100:
            print('module_trailer')
            Prog_Outcome['module_trailer'].append(mark)
            count+=1

    elif _fail <= 60:
            print('module_retriever')
            Prog_Outcome['module_retriever'].append(mark)
            count+=1

    elif _fail >=80:
            print('exclude')
            Prog_Outcome['exclude'].append(mark)
            count+=1

def histogram_final():
    print("--------------------histogram------------------------")
#show the histogram
    print("Progress : ", end=" ")
    for co in Prog_Outcome["progress"]:
        print(str(co["pass"]) + "," + str(co["defer"]) + "," + str(co["fail"]))

    print("Progress (module trailer) : ", end=" ")
    for co in Prog_Outcome["module_trailer"]:
        print(str(co["pass"]) + "," + str(co["defer"]) + "," + str(co["fail"]))

    print("Module retriever : ", end=" ")
    for co in Prog_Outcome["module_retriever"]:
        print(str(co["pass"]) + "," + str(co["defer"]) + "," + str(co["fail"]))

    print("Exclude : ", end=" ")
    for co in Prog_Outcome["exclude"]:
        print(str(co["pass"]) + "," + str(co["defer"]) + "," + str(co["fail"]))

    
def file_read():#write the outputs in a text file
    with open('markssheet.txt', 'w') as f:
     f.write(str(Prog_Outcome))
     f.close()
    
    
    

 #asking for inputs from user   
while ans =='y':
    
    try:
        while ans1=='y':
            cp=int(input('\nPlease enter your credits at pass:'))
            if (cp%20) !=0:
                rangeError()
            elif cp>120:
                totincorrect()
            else:
                break

        while ans1=='y':
            cd=int(input('Please enter your credits at defer:'))
            if (cd%20) !=0:
                rangeError()
            elif cd>120:
                totincorrect()
            else:
                break
        while ans1=='y':
            cf=int(input('Please enter your credits at fail:'))
            if (cf%20) !=0:
                rangeError()
            elif cf>120:
                totincorrect()
            else:
               
                tot_check(cp,cd,cf)
                break
            
    except ValueError:
        print('Integer required')


    tot2 = prg + trai+ ret + exl #store the sum of inputs
    while True:
            print('\nWould you like to enter another set of data ?')

            ans = str(input('Enter y for yes or q to quit and view results ')) #taking inputs from user

            if ans == 'y':
                    break

            elif ans=='q':
                #function calling
                histogram_final()
                file_read()
                
                

                print('\n\n',count,'outcomes in total')#show the total outputs
                print('-------------------------------------------------------------')
                break

            else:
                print('invalid input')
