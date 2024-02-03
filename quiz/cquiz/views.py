from django.shortcuts import render
from .models import questions,details
from .forms import questionform,detailsform
# Create your views here.
def showindex(r):
    return render(r,'index.html')
def showabout(r):
    if r.POST:
        x=detailsform(r.POST)
        print(r.POST)
        x.save()
    x=detailsform()
    return render(r,'About.html',{'values':x})
        
def showquiz(r):
    mylist=[]
    x=[]
    q=0
    c=0
    if r.POST:
        ans=r.POST['selected']
        if 'selected' in r.session:
            mylist=r.session['selected']
            mylist.append(ans)
        else:
            mylist=[ans]
        r.session['selected']=mylist
    else:
        if 'current' in r.session:
            del r.session['current']
            if 'selected' in r.session:
                del r.session['selected']
    if q<=3:
        if 'current' in r.session:
            q=r.session['current']+1
        else:
            q=1
    r.session['current']=q
    row=questions.objects.filter(qno=q)
    cy=questions.objects.values('qno')
    for i in cy:
        c+=1
    if q>c:
        s=0
        row=questions.objects.values('anschoiceno')
        for i in row:
            x.append(i['anschoiceno']) 
        for i,j in enumerate(mylist):
            if j == x[i]:
                s+=1
        return render(r,'result.html',{'values':s})
    return render(r,'quiz.html',{'values':row})
def showupdate(r):
    if r.POST:
        print(r)
        x=questionform(r.POST)
        x.save()
    x=questionform()
    return render(r,'update.html',{'values':x})
def submit(r):
    answer=questions.objects.anschoiceno()
    print(answer)