from django.shortcuts import render

def hello(request):
    context={}
    context["msg"]="我爱你们！"
    return render(request,"hello.html",context)