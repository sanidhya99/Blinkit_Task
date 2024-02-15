from django.shortcuts import render,redirect
from .models import *
from .forms import *
from register.models import CustomUser
from datetime import datetime
from django.contrib import messages
#------------------------------------------------------------------------------------------
def feed(response):
    show=Post_image.objects.filter(author=response.user.id).order_by('-id')
    print(show[0].photo)
    person=response.user
    return render(response,'feed/profile.html',{"feeds":show,"person":person})
#------------------------------------------------------------------------------------------
def input(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        
        if form.is_valid():
            print("form is valid")
            image = form.cleaned_data["photo"]
            print(image)
            notes = form.cleaned_data["notes"]  # Corrected field name
            time = datetime.now().time()
            date = datetime.now().date()
            pt = Post_image.objects.create(author=request.user, photo=image, notes=notes, time=time, date=date)
            pt.save()
        else:
            print("Form errors:", form.errors)
    else:
        form = PostForm()
    return render(request, 'feed/input.html', {"form": form})

#------------------------------------------------------------------------------------------
