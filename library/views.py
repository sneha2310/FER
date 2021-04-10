from django.shortcuts import render

# Create your views here.
def tech(request):
    context ={'technology': 'active'}
    return render(request, 'library/main.html', context)