from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def login_(request):
    if request.method=='POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            context = {}
            context['name']=username
            return render(request,'index.html',context)
        else:
            msg = '用户名或密码错误！'
            return render(request,'login_.html',locals())
    return render(request,'login_.html')

def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('Password')
        password2 = request.POST.get('Passwordrepeat')
        if password != password2:
            msg = '两次输入密码不同！'
            return render(request,'login_.html',locals())
        elif username == '':
            msg = '用户名不能为空！'
            return render(request,'login_.html',locals())
        else :
            User.objects.create_user(username=username,email=email,password=password).save()
            context = {}
            context['name']=username
            return render(request,'index.html',context)
    '''return render(request,'login_.html')'''


def index(request):
    return render(request,'index.html')

def web1(request):
    return render(request,'1.html')

def web2(request):
    return render(request,'2.html')

def web3(request):
    return render(request,'3.html')

def web4(request):
    return render(request,'4.html')

def web5(request):
    return render(request,'5.html')

def web6(request):
    return render(request,'6.html')



