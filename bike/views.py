from django.shortcuts import render

# Create your views here.

def rx(request):
    return render(request,'rx.html')