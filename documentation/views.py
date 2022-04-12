from django.shortcuts import render

# Create your views here.
def documentation(request):
    context = {}
    return render(request, 'documentation.html',context)