from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session

from exam.models import Solution,Question,Clock
from django.contrib.auth.models import User

# Create your views here.

def Exam(request):
    return render(request,'login.html')

def MCQ(request):
    current_user = request.user
    if current_user.is_staff==False:
        if request.method == 'GET':
            question = Question.objects.get(id=1)
            return render(request,'questions.html',{'question' : question})
        if request.method == 'POST':
            if request.POST['id']:
                id = int(request.POST['id'])
                questions = Question.objects.all()
                flag = 0
                for question in questions:
                    try:
                        answer = request.POST[question.question]
                        solution = [question.question,answer]
                        flag = 1
                        break
                    except Exception:
                        pass
                if flag==1:
                    submit = Solution.objects.filter(number=id,username=current_user.username)
                    if submit:
                        submit.update(questions=solution[0],solution=solution[1])
                    else:
                        user = Solution.objects.create(number=id,username=current_user.username,questions=solution[0],solution=solution[1])
                flag = 0
                try:
                    question = Question.objects.get(id=id+1)
                    flag = 1
                except Exception:
                    pass

                if flag==0:
                    submit = Solution.objects.filter(username=current_user.username)
                    user_info = User.objects.get(username=current_user.username)
                    correct = 0
                    incorrect = 0
                    for i in range(len(submit)):
                        for j in range(len(questions)):
                            if submit[i].number == questions[j].id:
                                if submit[i].solution == questions[j].correct_answer:
                                    correct+=1
                                else:
                                    incorrect+=1
        
                    return render(request,'result.html',{'username':user_info.username,
                        'email':user_info.email,'first_name':user_info.first_name,
                        'last_name':user_info.last_name,'correct':correct,
                        'incorrect':incorrect,'unsolve':len(questions)-correct-incorrect})
                return render(request,'questions.html',{'question' : question})
    else:
         return render(request,'login.html',{'message' : "Admin has made you out from Exam."})

def Result(request):
    current_user = request.user
    if current_user.is_staff == False:
        questions = Question.objects.all()
        submit = Solution.objects.filter(username=current_user.username)
        user_info = User.objects.get(username=current_user.username)
        correct = 0
        incorrect = 0
        for i in range(len(submit)):
            for j in range(len(questions)):
                if submit[i].number == questions[j].id:
                    if submit[i].solution == questions[j].correct_answer:
                        correct+=1
                    else:
                        incorrect+=1
        
        return render(request,'result.html',{'username':user_info.username,
                    'email':user_info.email,'first_name':user_info.first_name,
                    'last_name':user_info.last_name,'correct':correct,
                    'incorrect':incorrect,'unsolve':len(questions)-correct-incorrect})
    else:
        return render(request,'login.html',{'message':'Admin has disconnected you from exam!'})


def Submit(request):
    current_user = request.user
    if current_user.is_staff == False:
        questions = Question.objects.all()
        solution =[]
        for item in questions:
            try:
                value = request.POST[item.question]
                solution.append([item.question,value])
            except Exception :
                pass
        submit = Solution.objects.filter(id=current_user.username)
        if submit:
            submit.update(questions=solution)
        else:
            user = Solution.objects.create(id=current_user.username,questions=solution)
        solutions = Solution.objects.get(id=current_user.username)
        user_info = User.objects.get(username=current_user.username)
        solution = solutions.questions
        correct = 0
        incorrect = 0
        for i in range(len(solution)):
            for j in range(len(questions)):
                if solution[i][0] == questions[j].question:
                    if solution[i][1] == questions[j].correct_answer:
                        correct+=1
                    else:
                        incorrect+=1
        
        return render(request,'result.html',{'username':user_info.username,
                    'email':user_info.email,'first_name':user_info.first_name,
                    'last_name':user_info.last_name,'correct':correct,
                    'incorrect':incorrect,'unsolve':len(questions)-correct-incorrect})
    else:
        return render(request,'login.html',{'message':'Admin has disconnected you from exam!'})
    


             


