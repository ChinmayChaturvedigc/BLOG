from django.shortcuts import render,HttpResponse
from myapp.models import Post

def blog(request):
    allPosts = Post.objects.all()
    context = {"allPost":allPosts}
    return render (request,"myapp/blog.html",context)

def blogPost (request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render (request, "myapp/blogPost.html",context)