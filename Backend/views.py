from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.
def home(request):
    con = [ ]
    task = models.tasks.objects.all()
    for i in task:
        obj = {
            'id': i.id,
            'time': i.Time,
            'description':  i.Description,
            'comp': i.Completed,
            'marked': i.Marked
        }
        con.append(obj)
        
    return render(request,'home.html', {'obj': con})
def delete(request, id):
    models.tasks.objects.filter(id= id).delete()
    return redirect('/')
def add(request): 
    return render(request, 'add.html')
def pro(request):
    
    des = request.POST["Des"]
    Time = request.POST["begin"]
    try:
        check = request.POST["check"]
    except:
        check=False
    if check =='on':
        check = True
    print(check)
    mod = models.tasks(Description=des, Time=Time, Completed=check)
    mod.save()
 
    return redirect('/')
def edit(request, id):
    mod = models.tasks.objects.filter(id=id)
    print(mod)
    for i in mod:
        print(i)
        a = str(i.Time)
        print(a)
        id2 = i.id
        des = i.Description
        comp = i.Completed
        mark = i.Marked
        if comp == True:
            comp = True
        else:
            comp= False
        if mark == True:
            mark = True
        else:
            mark= False
    return render(request, 'edit.html', {'time':a, 'des':des,'comp':comp, 'id':id2, 'mark': mark})
def pro2(request, id):
    mod = models.tasks.objects.get(id=id)
    
    des = request.POST["Des"]
    Time = request.POST["begin"]
    try:
        check = request.POST["check"]
        if check == 'on':
            check = True
    except:
        check=False
    try:
        mark= request.POST["marked"] 
        if mark == 'on':
            mark = True
        
    except:
            mark = False
    mod.Time = Time
    mod.Description =des
    mod.Completed = check
    mod.Marked = mark
    mod.save()
    return redirect('/')