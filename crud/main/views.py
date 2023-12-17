from django.shortcuts import render, redirect
from .models import Test
from .forms import TestForm

def home(request):
    data = Test.objects.all()
    return render(request, "main/home.html", {"data": data})

def post(request):
    if request.method == "POST":
        data1 = request.POST["ad"]
        data2 = request.POST["soyad"]
        data = Test(ad=data1, soyad=data2)
        data.save()
    return redirect("home")

def update_view(request, pk): 
    instance = Test.objects.get(id=pk)  
    form = TestForm(request.POST or None, instance=instance)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "main/update.html", {"form": form, "instance": instance})

def delete(request, id):
    data = Test.objects.get(id=id)
    data.delete()
    return redirect("home")
