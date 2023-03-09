from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskData

def inserttask(req):
    return render(req,"insert.html")
def savedata(req):
    ob=TaskData()
    ob.task=req.POST.get("task")
    ob.date=req.POST.get("date")
    ob.dec=req.POST.get("dec")
    ob.save()
    return HttpResponse("data save")

def tasklist(req):
    data=TaskData.objects.all().values()
    return render(req,"show.html",{"data":data})
def update(req):
    data_id=req.GET.get("id")
    data=TaskData.objects.filter(id=data_id).values()
    return render(req,"update.html",{"data":data})
def updatetask(req):
    uid=req.POST.get("id")
    print(uid)
    ob=TaskData.objects.get(id=uid)
    ob.task=req.POST.get("task")
    ob.date=req.POST.get("date")
    ob.dec=req.POST.get("dec")
    ob.save()
    data=TaskData.objects.all().values()
    return render(req,"show.html",{"data":data})
def deletetask(req):
    data_id=req.GET.get("id")
    TaskData.objects.get(id=data_id).delete()
    data=TaskData.objects.all().values()
    return render(req,"show.html",{"data":data})