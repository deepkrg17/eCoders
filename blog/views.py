from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from blog.models import Contact, Post
# Create your views here.

def home(request):
    first_six = Post.objects.all()[:6]
    return render(request, 'blog/home.html', {'posts':first_six})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    
    if request.method=="POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            content = request.POST['content']
            contact = Contact(name=name, email=email, content=content)
            contact.save()
            messages.success(request, 'Successfully sent.')
        except Exception as e:
            messages.error(request, e)
    
    return render(request, 'blog/contact.html')

def blogpost(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post.html', {'post':post})

def search(request):
    query = request.GET['q']
    if len(query)>80:
        results = Post.objects.none()
        messages.warning(request, "Your query is too large.")
    else:
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'blog/search.html', context)