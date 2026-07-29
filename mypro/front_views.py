from django.shortcuts import render,redirect
from api.models import Home
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
     if request.method == "POST":
          name=request.POST["name"]
          amount=request.POST["amount"]
          interest_rate=request.POST["interest_rate"]
          Home.objects.create(
               name=name,
               amount=amount,
               interest_rate=interest_rate
          )
         
     return render(request,'home.html')
def navbar(request):
     return render(request,'navbar.html')
def recode(request):  
     records=Home.objects.all()    
     # search = request.GET.get("search", "")
     # if search:
     #      data = Home.objects.filter(name__icontains=search)
     # else:
     #      data = Home.objects.all()
     # context = {
     #      "data": data,
     #      "search": search,
     # }
    
     return render(request,'recode.html',{'records':records})
def search_record(request):
    search = request.GET.get("search", "")

    if search:
        records = Home.objects.filter(name__icontains=search)
    else:
        records = Home.objects.all()

    context = {
        "records": records,
        "search": search,
    }
    return render(request, 'recode.html', context)

def edit(request, id):
    record = get_object_or_404(Home, id=id)

    if request.method == "POST":
        record.name = request.POST["name"]
        record.amount = request.POST["amount"]
        record.interest_rate = request.POST["interest_rate"]
        record.save()
        return redirect('recode')

    return render(request, 'edit.html', {'record': record})
def delete(request,id):
     record = get_object_or_404(Home, id=id)
     record.delete()
     return redirect('recode')
     #  return render(request, 'recode.html')


def calculate(request):
     return render(request,'calculate.html')
