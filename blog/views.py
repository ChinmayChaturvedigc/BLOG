import email
from email import message
from django.contrib import messages
from importlib.resources import contents
from django.shortcuts import render,HttpResponse
from blog.models import Contact
from myapp.models import Post


def home(request):
    return render (request,"blog/home.html")

def contact(request):
   
    if request.method =="POST":
        name = request.POST ["name"]
        email = request.POST ["email"]
        content = request.POST ["content"]

        if len(name)<2 or len(email)<2 or len(content)<4:
            messages.error(request, 'Please fill form correctly')
        else:
            contact = Contact(name=name , email=email , content=content)
            contact.save()
            messages.success(request, 'Form filled successfully')
    return render (request,"blog/contact.html")

def about(request):
    messages.success(request, 'this is about page')
    return render (request,"blog/about.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else: 
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPost': allPosts, 'query': query}
    #allPosts= Post.objects.filter(title__icontains=query)
    #params={'allPost': allPosts , 'query':query}
    return render(request, 'blog/search.html', params)