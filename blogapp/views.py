from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def addBlog(request):
    if(request.method=="POST"):
        title=request.POST.get("title")
        description=request.POST.get("description")
        image=request.FILES.get("image")
        blog=Blog(title=title,description=description,user=request.user,image=image)
        blog.save()
        return redirect("/home")
    return render(request,"addblog.html")

def allBlogs(request):
    srch=request.GET.get("srch")
    if(srch):
         blogs=Blog.objects.filter(description__contains=srch)
         return render(request,"allBlogs.html",{"blogs":blogs})
    blogs=Blog.objects.all()
    return render(request,"allBlogs.html",{"blogs":blogs})

def myblogs(request):
    srch=request.GET.get("srch")
    if(srch):
         blogs=Blog.objects.filter(user=request.user,description__contains=srch)
         return render(request,"myblogs.html",{"blogs":blogs})
    blogs=Blog.objects.filter(user=request.user)
    return render(request,"myblogs.html",{"blogs":blogs})