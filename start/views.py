from django.shortcuts import render

# Create your views here.

# Create your views here.
def start(request):
    context={'start':'active'}
    return render(request, 'start/start.html',context)