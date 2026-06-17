import select
from urllib import request
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import logout


from .models import examinfo, UserData , Result


# Create your views here.

                            # For Questions
def Home (request):
    return render(request ,'home.html')

def Give_Me_Questioncurd_Page(request):
    return render(request,'question/questioncurd.html')

def Give_Me_AddQuestion_Page(request):
    return render(request,'question/addquestion.html')

def Give_Me_ViewQuestion_Page(request):
    return render(request,'question/viewquestion.html')

def Give_Me_UpdateQuestion_Page(request):
    return render(request,'question/updatequestion.html')

def Give_Me_DeleteQuestion_Page(request):
    return render(request,'question/deletequestion.html')

def Give_Me_ShowAllQuestion_Page(request):
    qdata = examinfo.objects.all()
    return render(request,'question/showallquestion.html',{'qdata':qdata})




def AddQuestions(request):
    qno = request.GET['qno']
    qtext = request.GET['qtext']
    op1 =request.GET['op1']
    op2 =request.GET['op2']
    op3 =request.GET['op3']
    op4 =request.GET['op4']
    subject = request.GET['subject']
    answer = request.GET['answer']

    examinfo.objects.create(qno = qno , qtext = qtext ,op1 = op1, op2 = op2, op3 = op3 , op4 = op4 , subject = subject, ans = answer)
    return render (request,'question/addquestion.html' ,{'message' : 'Question add Successfully'})

def View_Question(request):
    qno = request.GET['qno']
    qdata = examinfo.objects.get(qno=qno)
    return render (request,'question/viewquestion.html' ,{'qdata' : qdata})

def View_Question_Update(request):
    qno = request.GET['qno']
    qdata = examinfo.objects.get(qno=qno)
    return render (request,'question/updatequestion.html' ,{'qdata' : qdata})

def UpdateQuestion(request):
    qno = request.GET['qno']
    qdata = examinfo.objects.filter(qno=qno)
    qdata.update(
        qtext = request.GET['qtext'],
        op1 =request.GET['op1'],
        op2 =request.GET['op2'],
        op4 =request.GET['op4'],
        subject = request.GET['subject'],
        ans = request.GET['answer']
    )
    return render (request,'question/updatequestion.html' ,{'message' : 'Question update Successfully'})

def View_Question_Delete(request):
    qno = request.GET['qno']
    qdata = examinfo.objects.get(qno=qno)
    return render (request,'question/deletequestion.html' ,{'qdata' : qdata})

def DeleteQuestion(request):
    qno = request.GET['qno']
    subject = request.GET['subject']

    examinfo.objects.filter(qno=qno, subject=subject).delete()
    return render (request,'question/deletequestion.html' ,{'message' : 'Question delete Successfully'})


                                # For Student 



# Create your views here.
def GiveMeRegisterPage(request):
    return render(request,'student/registration.html')

def Register(request):
    uname = request.GET['username']
    passwd = request.GET['password']


    UserData.objects.create(username = uname, password = passwd )
    return render(request,'student/login.html',{'msg': 'user register successfully'})

def GiveMeLoginPage(request):
    return render(request,'student/login.html')


def Login(request):
    uname = request.GET['username']
    passwd = request.GET['password']

    request.session['username'] = uname

    udata = UserData.objects.get(username = uname)

    if (udata.password == passwd):
        request.session['answer'] = {}
        request.session['score'] = 0
        request.session['qno'] = 0
        return render(request,'question/subject.html')
    else :
        return render(request,'student/login.html',{'msg':'invalid password'})

    
def GiveMeStudentCurdPage(request):
    return render(request,'student/studentcurd.html')

def GiveMeAddstudentpage(request):
    return render(request,'student/addstudent.html')

def GiveMeUpdatestudentpage(request):
    return render(request,'student/updatestudent.html')

def GiveMeViewstudentpage(request):
    return render(request,'student/viewstudent.html')

def GiveMeDeletestudentpage(request):
    return render(request,'student/deletestudent.html')

def GiveMeShowAllPage(request):
    udata = UserData.objects.all()
    return render(request,'student/showallstudent.html',{'udata':udata})


def AddUser(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    UserData.objects.create(username = username, password = password )
    return render(request,'student/addstudent.html',{'msg': 'user register successfully'})

def ShowUser(request):
    try : 
        username = request.GET.get('username')
        udata = UserData.objects.get(username = username)
        return render(request,'student/studentcurd.html',{'udata':udata})
    except :
        return render(request,'student/viewstudent.html')

def UpdateUser(request):
    username = request.GET.get('username')
    udata = UserData.objects.filter(username = username)
    udata.update(password = request.GET.get('password'))
    print(connection.queries)
    return render(request,'student/updatestudent.html',{'msg': 'user update successfully'})

def DeleteUser(request):
    username = request.GET.get('username')
    UserData.objects.filter(username = username).delete()
    return render(request,'student/deletestudent.html',{'msg': 'user delete successfully'})

def DeleteUserForShowAllPage(request):
    username = request.GET.get('username')  
    UserData.objects.filter(username = username).delete()
    udata = UserData.objects.all()
    return render(request,'student/showallstudent.html',{'udata':udata})


def StartTest(request):
    subject = request.GET['subject']

    request.session['subject'] = subject

    queryset = examinfo.objects.filter(subject = subject).values()

    #select * from questions where subject =  request.GET['subject'];

    listallquestions = list(queryset)

    request.session['listallquestions'] = listallquestions

    return render (request,'starttest.html',{"question":listallquestions[0:0:]})

def NextQuestion(request):
    allquestions =  request.session['listallquestions'] 
    questionindex = request.session['qno']

    if 'op' in request.GET:
        allanswer = request.session['answer']  # {}
        allanswer[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["op"],request.GET["answer"]]

        allanswer = {1: [1, 2+2, 4, 4]}

    try:
        if questionindex <= len(allquestions):
                request.session['qno']+=1
                question = allquestions[request.session['qno']]
    except:
            return render (request,'starttest.html',{"msg":"Go to previous question"}) 
    
    return render (request,'starttest.html',{"question":question})  

def PreviousQuestion(request):
    allquestions =  request.session['listallquestions'] 
    questionindex = request.session['qno']

    if 'op' in request.GET:
        allanswer = request.session['answer']  # {}
        allanswer[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["op"],request.GET["answer"]]

    try:
        if questionindex > 0 :
                request.session['qno']-=1
                question = allquestions[request.session['qno']]
    except:
            return render (request,'starttest.html',{"msg":"Go to next question"}) 
    
    return render (request,'starttest.html',{"question":question}) 

def End_Test(request):
    if 'op' in request.GET:
        allanswer = request.session.get('answer', {})  # {}
        allanswer[request.GET.get("qno")] = [request.GET.get("qno"),request.GET.get("qtext"),request.GET.get("op"),request.GET.get("answer")]
        request.session['answer']= allanswer

    response = request.session['answer']=allanswer

    allanswer = {1: [1, 2+2, 4, 4]}

    response=request.session['answer'].values()   #  [1, 2+2, 4, 4]

    for ans in response:
        if ans[2] == ans[3]:
            request.session['score']+=1

    finalscore = request.session['score']

    uname = request.session['username']

    userdb = UserData.objects.get(username = uname)

    Result.objects.create(
        username= userdb,
        subject = request.GET['subject'],
        marks = finalscore
    )
    return render(request,'result/score.html',{'response':response, 'finalscore':finalscore})


def GetAllResultPage(request):
    rdb= Result.objects.all()
    return render (request, 'result/allresult.html',{'rdb':rdb})

def LogoutUser(request):
    logout(request)
    return render(request,'student/login.html')