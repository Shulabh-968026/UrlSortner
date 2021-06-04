
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import uuid
# Create your views here.
from .models import LinkUrl

def home(request):
    return render(request,"index.html")

def index(request):
    if request.method=="POST":
        link=request.POST["url"]
        obj1=LinkUrl.objects.filter(link=link)
        if obj1:
            return render(request,"index.html",{"context":"https://djangourlsortner.herokuapp.com/"+str(obj1[0].slug)})
        else:
            uid=str(uuid.uuid4())[:5]
            obj=LinkUrl(link=link,slug=uid)
            print(link)
            obj.save()
            return render(request,"index.html",{"context":"https://djangourlsortner.herokuapp.com/"+uid})
    else:
        return redirect("/home")
        
def sort_url(request,key):
    object=LinkUrl.objects.filter(slug=key)[0]
    return redirect(object.link)
