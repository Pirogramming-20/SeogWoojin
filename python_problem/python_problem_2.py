#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(data_list):
    data_list[1]=int(data_list[1])
    data_list[2]=int(data_list[2])
    student_info.append(data_list)
    return
    #사전에 학생 정보 저장하는 코딩 

##############  menu 2
def Menu2():
    #학점 부여 하는 코딩
    for i in range(len(student_info)):
        student=student_info[i]
        if len(student)==3:
            mid=student[1]
            fin=student[2]
            ave=(mid+fin)/2
            
            if ave>=90:
                student.append('A')
            elif ave>=80:
                student.append('B')
            elif ave>=70:
                student.append('C')
            else:
                student.append('D')
    return

##############  menu 3
def Menu3():
    #출력 코딩
    print("----------------------------")
    print("name   mid   final   grade")
    print("----------------------------")
    for student in student_info:
        print(f"{student[0]}    {student[1]}   {student[2]}   {student[3]}")
        
    return
    

##############  menu 4
def Menu4(i):
    student_info.pop(i)
    return
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
student_info=[]

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        data=input("Enter name mid-score final-score : ")
        data_list=data.split()
        name_in=False
        for student in student_info:
            if data_list[0]==student[0]:
                name_in=True
        
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        if(len(data_list)!=3):
            print("Num of data is not 3!")
        elif name_in:
            print("Already exist name!")
        elif not(str.isdigit(data_list[1])) or not(str.isdigit(data_list[1])) or int(data_list[1])<=0 or int(data_list[2])<=0:
            print("Score is not positive integer")
        else:
            Menu1(data_list) 
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        
        
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if len(student_info)==0:
            print("No student data!")
        #예외사항이 아닌 경우 2번 함수 호출
        else:
            Menu2()
            print("Grading to all students.")
            #"Grading to all students." 출력
            
    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)        
        if len(student_info)==0:
            print("No student data!")        
                
        else:
            grade_all=True
            for student in student_info:
                if len(student)==3:
                    grade_all=False
                    break
            
            if not(grade_all):
                print("There is a student who didn't get grade.")
            #예외사항이 아닌 경우 3번 함수 호출
            else:
                Menu3()
            

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if len(student_info)==0:
            print("No student data!")
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        else:
            name=input("Enter the name to delete : ")
            #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
            exist=False
            for i in range(len(student_info)):
                student=student_info[i]
                if name==student[0]:
                    exist=True
                    break

            if not(exist):
                print("Not exist name!")
            #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
            else:
                Menu4(i)
                print(name,"student information is deleted.")
        
        
    elif choice == "5" :
        #프로그램 종료 메세지 출력
        print("Exit Program!")
        #반복문 종료
        break

    else :
        print("Wrong number. Choose again.")
        #"Wrong number. Choose again." 출력