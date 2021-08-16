from django.shortcuts import render

# Create your views here.
def urlmapping1(request):
    return render(request,'noohin.html',context={'name':'shaikpage'})




def urlmapping2(request):
    return render(request,'moni.html',context={'name':'monipage'})