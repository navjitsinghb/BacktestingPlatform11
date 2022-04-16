from django.shortcuts import render
from django.http import HttpResponse
from .models import Script
# Create your views here.
def build(request):
    context = {}
    return render(request, "build.html", context)

def myalgos(request):
    scripts = Script.objects.filter(owner=request.user)
    context = { "scripts": scripts }
    return render(request,"myalgos.html", context) 

def postalgo(request):

    if (request.method == "POST"):
        code = request.POST.get('output')
        title = request.POST.get('title')

        print(code)
        try: 
            Script.objects.create( owner = request.user,
    title = title,
    code = code)
        except Exception as e:
                    print('failed',e)
        print("hello")
    
    return HttpResponse(200, content_type='text/plain')

def useralgo(request):
    print("useralgos")

def editalgo(request,id):
    
    edits = Script.objects.filter(id=id)
    
    
    context = {"edits" : edits,
    "amount": 3}
    return render(request,"buildedit.html", context) 