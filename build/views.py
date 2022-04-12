from django.shortcuts import render

# Create your views here.
def build(request):
    context = {}
    return render(request, "build.html", context)

def myalgos(request):
    context = {}
    return render(request,"myalgos.html", context) 

def postalgo(request):
    if (request.method == "POST"):
        print("hello")

def useralgo(request):
    print("useralgos")
    