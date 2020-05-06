from django.shortcuts import render
from .models import contact
# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        q=contact(name=name,email=email,message=message)
        q.save()
    return render(request,'index.html')
