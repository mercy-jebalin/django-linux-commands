from django.shortcuts import render
from .models import Contact
import subprocess


def run_win_cmd(comd):
    result = []
    process = subprocess.Popen(comd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # print(process,process.stdout)
    for line in process.stdout:
        try:
            result.append(line.decode('utf-8'))
        except:
            return "error"
    errcode = process.returncode
    # for line in result:
    #    print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', comd)
    if result==[]:
        return "invalid command"
    else:
        return result


def home(request):
    return render(request, 'users/home.html')

l=[]


def sec(request):
    global l
    a = request.POST.get('cmd')
    n = run_win_cmd(a)
    l.append(a)
    l.append(n)
    return render(request, 'users/sec.html', {'l': l})


def help(request):
    return render(request, 'users/help.html', {'title': 'Help'})


def about(request):
    return render(request, 'users/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'users/contact.html', {'title': 'Contact'})

def db(request):
    a=request.POST.get('u')
    b=request.POST.get('e')
    c=request.POST.get('f')
    p=Contact(name=a,emailID=b,feedback=c)
    p.save()
    return render(request, 'users/thank.html')
