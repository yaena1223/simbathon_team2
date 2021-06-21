from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def academic(request):
    return render(request, 'main/academic.html')

def art(request):
    return render(request, 'main/art.html')

def atheletic(request):
    return render(request, 'main/atheletic.html')

def fresh(request):
    return render(request, 'main/fresh.html')

def performance(request):
    return render(request, 'main/performance.html')

def research(request):
    return render(request, 'main/research.html')

def social(request):
    return render(request, 'main/social.html')

def volunteer(request):
    return render(request, 'main/volunteer.html')

def contact(request):
    return render(request, 'main/contact.html')

def likelion(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'main/likelion.html',{'posts':posts})

def detail(request,id):
    post = get_object_or_404(Post, pk = id)
    return render(request,'main/detail.html',{'post':post})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail',new_post.id)

def edit(request,id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post':edit_post})

def update(request,id):
    update_post = Post()
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail',update_post.id)

def delete(request,id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main:likelion')