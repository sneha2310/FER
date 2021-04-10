from django.shortcuts import render

# Create your views here.
def abouts(request):
    context ={'about' : 'active'}
    return render(request, 'about/about.html', context)