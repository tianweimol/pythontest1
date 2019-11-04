from django.http import HttpResponse
from MolModels.Country import Country
from django.shortcuts import render

def AddCountry(request):
    country=Country(Code='VN',Name="越南",FlagPictureName=1)
    country.save()
    return HttpResponse('<script>alert("添加成功")</script>')

def ShowCountry(request):
    list=Country.objects.all()
    response=''
    # print (list)
    context={}
    context["models"]=list
    return render(request,"country.html",context)
    # for var in list:
    #     response += var.Name+'|'+var.Code + " "
    # return HttpResponse("<p>" + response + "</p>")

def UpdateCountry(request):
    list=Country.objects.all()
    print('begin')
    for var in list:
        var.FlagPictureName='http://dev.res.tiens.com/pocket/flags/32x32/'+var.Code.lower()+'.png'
        print(var.FlagPictureName)
        var.save()
    return HttpResponse('<script>alert("修改成功")</script>')