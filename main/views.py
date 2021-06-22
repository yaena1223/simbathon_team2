from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def faq(request):
    return render(request, 'main/faq.html')

def contact(request):
    return render(request, 'main/contact.html')

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



# 멋사
def likelion(request):
    likelion_posts = likelion_Post.objects.all().order_by('-date')
    return render(request,'club/likelion.html',{'posts':likelion_posts})

def likelion_detail(request,id):
    likelion_post = get_object_or_404(likelion_Post, pk = id)
    return render(request,'main/likelion_detail.html',{'post':likelion_post})

def likelion_new(request):
    return render(request,'main/likelion_new.html')

def likelion_create(request):
    likelion_new_post = likelion_Post()
    likelion_new_post.title = request.POST['title']
    likelion_new_post.writer = request.user
    likelion_new_post.date = timezone.now()
    likelion_new_post.body = request.POST['body']
    likelion_new_post.image = request.FILES.get('image')
    likelion_new_post.save()
    return redirect('main:likelion_detail',likelion_new_post.id)

def likelion_edit(request,id):
    likelion_edit_post = likelion_Post.objects.get(id = id)
    return render(request, 'main/likelion_edit.html', {'post':likelion_edit_post})

def likelion_update(request,id):
    likelion_update_post = get_object_or_404(likelion_Post, id = id)
    likelion_update_post.title = request.POST['title']
    likelion_update_post.writer = request.user
    likelion_update_post.date = timezone.now()
    likelion_update_post.body = request.POST['body']
    likelion_update_post.image = request.FILES.get('image')
    likelion_update_post.save()
    return redirect('main:likelion_detail',likelion_update_post.id)

def likelion_delete(request,id):
    likelion_delete_post = likelion_Post.objects.get(id = id)
    likelion_delete_post.delete()
    return redirect('main:likelion')

#학술분과
# cafein

def cafein(request):
    posts = cafein_Post.objects.all().order_by('-date')
    return render(request,'club/cafein.html',{'posts':posts})

def cafein_detail(request,id):
    cafein_post = get_object_or_404(cafein_Post, pk = id)
    return render(request,'main/cafein_detail.html',{'post':cafein_post})

def cafein_new(request):
    return render(request,'main/cafein_new.html')

def cafein_create(request):
    cafein_new_post = cafein_Post()
    cafein_new_post.title = request.POST['title']
    cafein_new_post.writer = request.user
    cafein_new_post.date = timezone.now()
    cafein_new_post.body = request.POST['body']
    cafein_new_post.image = request.FILES.get('image')
    cafein_new_post.save()
    return redirect('main:cafein_detail',cafein_new_post.id)

def cafein_edit(request,id):
    cafein_edit_post = cafein_Post.objects.get(id = id)
    return render(request, 'main/cafein_edit.html', {'post':cafein_edit_post})

def cafein_update(request,id):
    cafein_update_post = get_object_or_404(cafein_Post, id = id)
    cafein_update_post.title = request.POST['title']
    cafein_update_post.writer = request.user
    cafein_update_post.date = timezone.now()
    cafein_update_post.body = request.POST['body']
    cafein_update_post.image = request.FILES.get('image')
    cafein_update_post.save()
    return redirect('main:cafein_detail',cafein_update_post.id)

def cafein_delete(request,id):
    cafein_delete_post = cafein_Post.objects.get(id = id)
    cafein_delete_post.delete()
    return redirect('main:cafein')

# dna
def dna(request):
    posts = dna_Post.objects.all()
    return render(request,'club/dna.html',{'posts':posts})

def dna_detail(request,id):
    dna_post = get_object_or_404(dna_Post, pk = id)
    return render(request,'main/dna_detail.html',{'post':dna_post})

def dna_new(request):
    return render(request,'main/dna_new.html')

def dna_create(request):
    dna_new_post = dna_Post()
    dna_new_post.title = request.POST['title']
    dna_new_post.writer = request.user
    dna_new_post.date = timezone.now()
    dna_new_post.body = request.POST['body']
    dna_new_post.image = request.FILES.get('image')
    dna_new_post.save()
    return redirect('main:dna_detail',dna_new_post.id)

def dna_edit(request,id):
    dna_edit_post = dna_Post.objects.get(id = id)
    return render(request, 'main/dna_edit.html', {'post':dna_edit_post})

def dna_update(request,id):
    dna_update_post = get_object_or_404(dna_Post, id = id)
    dna_update_post.title = request.POST['title']
    dna_update_post.writer = request.user
    dna_update_post.date = timezone.now()
    dna_update_post.body = request.POST['body']
    dna_update_post.image = request.FILES.get('image')
    dna_update_post.save()
    return redirect('main:dna_detail',dna_update_post.id)

def dna_delete(request,id):
    dna_delete_post = dna_Post.objects.get(id = id)
    dna_delete_post.delete()
    return redirect('main:dna')


# dussa
def dussa(request):
    posts = dussa_Post.objects.all()
    return render(request,'club/dussa.html',{'posts':posts})

def dussa_detail(request,id):
    dussa_post = get_object_or_404(dussa_Post, pk = id)
    return render(request,'main/dussa_detail.html',{'post':dussa_post})

def dussa_new(request):
    return render(request,'main/dussa_new.html')

def dussa_create(request):
    dussa_new_post = dussa_Post()
    dussa_new_post.title = request.POST['title']
    dussa_new_post.writer = request.user
    dussa_new_post.date = timezone.now()
    dussa_new_post.body = request.POST['body']
    dussa_new_post.image = request.FILES.get('image')
    dussa_new_post.save()
    return redirect('main:dussa_detail',dussa_new_post.id)

def dussa_edit(request,id):
    dussa_edit_post = dussa_Post.objects.get(id = id)
    return render(request, 'main/dussa_edit.html', {'post':dussa_edit_post})

def dussa_update(request,id):
    dussa_update_post = get_object_or_404(dussa_Post, id = id)
    dussa_update_post.title = request.POST['title']
    dussa_update_post.writer = request.user
    dussa_update_post.date = timezone.now()
    dussa_update_post.body = request.POST['body']
    dussa_update_post.image = request.FILES.get('image')
    dussa_update_post.save()
    return redirect('main:dussa_detail',dussa_update_post.id)

def dussa_delete(request,id):
    dussa_delete_post = dussa_Post.objects.get(id = id)
    dussa_delete_post.delete()
    return redirect('main:dussa')

# kcc
def kcc(request):
    posts = kcc_Post.objects.all()
    return render(request,'club/kcc.html',{'posts':posts})

def kcc_detail(request,id):
    kcc_post = get_object_or_404(kcc_Post, pk = id)
    return render(request,'main/kcc_detail.html',{'post':kcc_post})

def kcc_new(request):
    return render(request,'main/kcc_new.html')

def kcc_create(request):
    kcc_new_post = kcc_Post()
    kcc_new_post.title = request.POST['title']
    kcc_new_post.writer = request.user
    kcc_new_post.date = timezone.now()
    kcc_new_post.body = request.POST['body']
    kcc_new_post.image = request.FILES.get('image')
    kcc_new_post.save()
    return redirect('main:kcc_detail',kcc_new_post.id)

def kcc_edit(request,id):
    kcc_edit_post = kcc_Post.objects.get(id = id)
    return render(request, 'main/kcc_edit.html', {'post':kcc_edit_post})

def kcc_update(request,id):
    kcc_update_post = get_object_or_404(kcc_Post, id = id)
    kcc_update_post.title = request.POST['title']
    kcc_update_post.writer = request.user
    kcc_update_post.date = timezone.now()
    kcc_update_post.body = request.POST['body']
    kcc_update_post.image = request.FILES.get('image')
    kcc_update_post.save()
    return redirect('main:kcc_detail',kcc_update_post.id)

def kcc_delete(request,id):
    kcc_delete_post = kcc_Post.objects.get(id = id)
    kcc_delete_post.delete()
    return redirect('main:kcc')

# mecs
def mecs(request):
    posts = mecs_Post.objects.all()
    return render(request,'club/mecs.html',{'posts':posts})

def mecs_detail(request,id):
    mecs_post = get_object_or_404(mecs_Post, pk = id)
    return render(request,'main/mecs_detail.html',{'post':mecs_post})

def mecs_new(request):
    return render(request,'main/mecs_new.html')

def mecs_create(request):
    mecs_new_post = mecs_Post()
    mecs_new_post.title = request.POST['title']
    mecs_new_post.writer = request.user
    mecs_new_post.date = timezone.now()
    mecs_new_post.body = request.POST['body']
    mecs_new_post.image = request.FILES.get('image')
    mecs_new_post.save()
    return redirect('main:mecs_detail',mecs_new_post.id)

def mecs_edit(request,id):
    mecs_edit_post = mecs_Post.objects.get(id = id)
    return render(request, 'main/mecs_edit.html', {'post':mecs_edit_post})

def mecs_update(request,id):
    mecs_update_post = get_object_or_404(mecs_Post, id = id)
    mecs_update_post.title = request.POST['title']
    mecs_update_post.writer = request.user
    mecs_update_post.date = timezone.now()
    mecs_update_post.body = request.POST['body']
    mecs_update_post.image = request.FILES.get('image')
    mecs_update_post.save()
    return redirect('main:mecs_detail',mecs_update_post.id)

def mecs_delete(request,id):
    mecs_delete_post = mecs_Post.objects.get(id = id)
    mecs_delete_post.delete()
    return redirect('main:mecs')

# nsa
def nsa(request):
    posts = nsa_Post.objects.all()
    return render(request,'club/nsa.html',{'posts':posts})

def nsa_detail(request,id):
    nsa_post = get_object_or_404(nsa_Post, pk = id)
    return render(request,'main/nsa_detail.html',{'post':nsa_post})

def nsa_new(request):
    return render(request,'main/nsa_new.html')

def nsa_create(request):
    nsa_new_post = nsa_Post()
    nsa_new_post.title = request.POST['title']
    nsa_new_post.writer = request.user
    nsa_new_post.date = timezone.now()
    nsa_new_post.body = request.POST['body']
    nsa_new_post.image = request.FILES.get('image')
    nsa_new_post.save()
    return redirect('main:nsa_detail',nsa_new_post.id)

def nsa_edit(request,id):
    nsa_edit_post = nsa_Post.objects.get(id = id)
    return render(request, 'main/nsa_edit.html', {'post':nsa_edit_post})

def nsa_update(request,id):
    nsa_update_post = get_object_or_404(nsa_Post, id = id)
    nsa_update_post.title = request.POST['title']
    nsa_update_post.writer = request.user
    nsa_update_post.date = timezone.now()
    nsa_update_post.body = request.POST['body']
    nsa_update_post.image = request.FILES.get('image')
    nsa_update_post.save()
    return redirect('main:nsa_detail',nsa_update_post.id)

def nsa_delete(request,id):
    nsa_delete_post = nsa_Post.objects.get(id = id)
    nsa_delete_post.delete()
    return redirect('main:nsa')

# marx
def marx(request):
    posts = marx_Post.objects.all()
    return render(request,'club/marx.html',{'posts':posts})

def marx_detail(request,id):
    marx_post = get_object_or_404(marx_Post, pk = id)
    return render(request,'main/marx_detail.html',{'post':marx_post})

def marx_new(request):
    return render(request,'main/marx_new.html')

def marx_create(request):
    marx_new_post = marx_Post()
    marx_new_post.title = request.POST['title']
    marx_new_post.writer = request.user
    marx_new_post.date = timezone.now()
    marx_new_post.body = request.POST['body']
    marx_new_post.image = request.FILES.get('image')
    marx_new_post.save()
    return redirect('main:marx_detail',marx_new_post.id)

def marx_edit(request,id):
    marx_edit_post = marx_Post.objects.get(id = id)
    return render(request, 'main/marx_edit.html', {'post':marx_edit_post})

def marx_update(request,id):
    marx_update_post = get_object_or_404(marx_Post, id = id)
    marx_update_post.title = request.POST['title']
    marx_update_post.writer = request.user
    marx_update_post.date = timezone.now()
    marx_update_post.body = request.POST['body']
    marx_update_post.image = request.FILES.get('image')
    marx_update_post.save()
    return redirect('main:marx_detail',marx_update_post.id)

def marx_delete(request,id):
    marx_delete_post = marx_Post.objects.get(id = id)
    marx_delete_post.delete()
    return redirect('main:marx')

#연구분과

#management    
def management(request):
    posts = management_Post.objects.all().order_by('-date')
    return render(request,'club/management.html',{'posts':posts})

def management_detail(request,id):
    management_post = get_object_or_404(management_Post, pk = id)
    return render(request,'main/management_detail.html',{'post':management_post})

def management_new(request):
    return render(request,'main/management_new.html')

def management_create(request):
    management_new_post = management_Post()
    management_new_post.title = request.POST['title']
    management_new_post.writer = request.user
    management_new_post.date = timezone.now()
    management_new_post.body = request.POST['body']
    management_new_post.image = request.FILES.get('image')
    management_new_post.save()
    return redirect('main:management_detail',management_new_post.id)

def management_edit(request,id):
    management_edit_post = management_Post.objects.get(id = id)
    return render(request, 'main/management_edit.html', {'post':management_edit_post})

def management_update(request,id):
    management_update_post = get_object_or_404(management_Post, id = id)
    management_update_post.title = request.POST['title']
    management_update_post.writer = request.user
    management_update_post.date = timezone.now()
    management_update_post.body = request.POST['body']
    management_update_post.image = request.FILES.get('image')
    management_update_post.save()
    return redirect('main:management_detail',management_update_post.id)

def management_delete(request,id):
    management_delete_post = management_Post.objects.get(id = id)
    management_delete_post.delete()
    return redirect('main:management')

#economy    
def economy(request):
    posts = economy_Post.objects.all().order_by('-date')
    return render(request,'club/economy.html',{'posts':posts})

def economy_detail(request,id):
    economy_post = get_object_or_404(economy_Post, pk = id)
    return render(request,'main/economy_detail.html',{'post':economy_post})

def economy_new(request):
    return render(request,'main/economy_new.html')

def economy_create(request):
    economy_new_post = economy_Post()
    economy_new_post.title = request.POST['title']
    economy_new_post.writer = request.user
    economy_new_post.date = timezone.now()
    economy_new_post.body = request.POST['body']
    economy_new_post.image = request.FILES.get('image')
    economy_new_post.save()
    return redirect('main:economy_detail',economy_new_post.id)

def economy_edit(request,id):
    economy_edit_post = economy_Post.objects.get(id = id)
    return render(request, 'main/economy_edit.html', {'post':economy_edit_post})

def economy_update(request,id):
    economy_update_post = get_object_or_404(economy_Post, id = id)
    economy_update_post.title = request.POST['title']
    economy_update_post.writer = request.user
    economy_update_post.date = timezone.now()
    economy_update_post.body = request.POST['body']
    economy_update_post.image = request.FILES.get('image')
    economy_update_post.save()
    return redirect('main:economy_detail',economy_update_post.id)

def economy_delete(request,id):
    economy_delete_post = economy_Post.objects.get(id = id)
    economy_delete_post.delete()
    return redirect('main:economy')

#international    
def international(request):
    posts = international_Post.objects.all().order_by('-date')
    return render(request,'club/international.html',{'posts':posts})

def international_detail(request,id):
    international_post = get_object_or_404(international_Post, pk = id)
    return render(request,'main/international_detail.html',{'post':international_post})

def international_new(request):
    return render(request,'main/international_new.html')

def international_create(request):
    international_new_post = international_Post()
    international_new_post.title = request.POST['title']
    international_new_post.writer = request.user
    international_new_post.date = timezone.now()
    international_new_post.body = request.POST['body']
    international_new_post.image = request.FILES.get('image')
    international_new_post.save()
    return redirect('main:international_detail',international_new_post.id)

def international_edit(request,id):
    international_edit_post = international_Post.objects.get(id = id)
    return render(request, 'main/international_edit.html', {'post':international_edit_post})

def international_update(request,id):
    international_update_post = get_object_or_404(international_Post, id = id)
    international_update_post.title = request.POST['title']
    international_update_post.writer = request.user
    international_update_post.date = timezone.now()
    international_update_post.body = request.POST['body']
    international_update_post.image = request.FILES.get('image')
    international_update_post.save()
    return redirect('main:international_detail',international_update_post.id)

def international_delete(request,id):
    international_delete_post = international_Post.objects.get(id = id)
    international_delete_post.delete()
    return redirect('main:international')


#politics    
def politics(request):
    posts = politics_Post.objects.all().order_by('-date')
    return render(request,'club/politics.html',{'posts':posts})

def politics_detail(request,id):
    politics_post = get_object_or_404(politics_Post, pk = id)
    return render(request,'main/politics_detail.html',{'post':politics_post})

def politics_new(request):
    return render(request,'main/politics_new.html')

def politics_create(request):
    politics_new_post = politics_Post()
    politics_new_post.title = request.POST['title']
    politics_new_post.writer = request.user
    politics_new_post.date = timezone.now()
    politics_new_post.body = request.POST['body']
    politics_new_post.image = request.FILES.get('image')
    politics_new_post.save()
    return redirect('main:politics_detail',politics_new_post.id)

def politics_edit(request,id):
    politics_edit_post = politics_Post.objects.get(id = id)
    return render(request, 'main/politics_edit.html', {'post':politics_edit_post})

def politics_update(request,id):
    politics_update_post = get_object_or_404(politics_Post, id = id)
    politics_update_post.title = request.POST['title']
    politics_update_post.writer = request.user
    politics_update_post.date = timezone.now()
    politics_update_post.body = request.POST['body']
    politics_update_post.image = request.FILES.get('image')
    politics_update_post.save()
    return redirect('main:politics_detail',politics_update_post.id)

def politics_delete(request,id):
    politics_delete_post = politics_Post.objects.get(id = id)
    politics_delete_post.delete()
    return redirect('main:politics')

#봉사분과

def elf(request):
    posts = Post.objects.all()
    return render(request,'club/elf.html',{'posts':posts})

def rcy(request):
    posts = Post.objects.all()
    return render(request,'club/rcy.html',{'posts':posts})


def road(request):
    posts = Post.objects.all()
    return render(request,'club/길.html',{'posts':posts})


def hand(request):
    posts = Post.objects.all()
    return render(request,'club/손짓사랑회.html',{'posts':posts})


def neighbor(request):
    posts = Post.objects.all()
    return render(request,'club/젊은새이웃.html',{'posts':posts})

def painters(request):
    posts = Post.objects.all()
    return render(request,'club/페인터즈.html',{'posts':posts})

def green(request):
    posts = Post.objects.all()
    return render(request,'club/푸름누리.html',{'posts':posts})

def korean(request):
    posts = Post.objects.all()
    return render(request,'club/한글학교하람.html',{'posts':posts})

# 사회분과
# kusa
def kusa(request):
    posts = kusa_Post.objects.all()
    return render(request,'club/kusa.html',{'posts':posts})

def kusa_detail(request,id):
    kusa_post = get_object_or_404(kusa_Post, pk = id)
    return render(request,'main/kusa_detail.html',{'post':kusa_post})

def kusa_new(request):
    return render(request,'main/kusa_new.html')

def kusa_create(request):
    kusa_new_post = kusa_Post()
    kusa_new_post.title = request.POST['title']
    kusa_new_post.writer = request.user
    kusa_new_post.date = timezone.now()
    kusa_new_post.body = request.POST['body']
    kusa_new_post.image = request.FILES.get('image')
    kusa_new_post.save()
    return redirect('main:kusa_detail',kusa_new_post.id)

def kusa_edit(request,id):
    kusa_edit_post = kusa_Post.objects.get(id = id)
    return render(request, 'main/kusa_edit.html', {'post':kusa_edit_post})

def kusa_update(request,id):
    kusa_update_post = get_object_or_404(kusa_Post, id = id)
    kusa_update_post.title = request.POST['title']
    kusa_update_post.writer = request.user
    kusa_update_post.date = timezone.now()
    kusa_update_post.body = request.POST['body']
    kusa_update_post.image = request.FILES.get('image')
    kusa_update_post.save()
    return redirect('main:kusa_detail',kusa_update_post.id)

def kusa_delete(request,id):
    kusa_delete_post = kusa_Post.objects.get(id = id)
    kusa_delete_post.delete()
    return redirect('main:kusa')

# rich
def rich(request):
    posts = rich_Post.objects.all()
    return render(request,'club/rich.html',{'posts':posts})

def rich_detail(request,id):
    rich_post = get_object_or_404(rich_Post, pk = id)
    return render(request,'main/rich_detail.html',{'post':rich_post})

def rich_new(request):
    return render(request,'main/rich_new.html')

def rich_create(request):
    rich_new_post = rich_Post()
    rich_new_post.title = request.POST['title']
    rich_new_post.writer = request.user
    rich_new_post.date = timezone.now()
    rich_new_post.body = request.POST['body']
    rich_new_post.image = request.FILES.get('image')
    rich_new_post.save()
    return redirect('main:rich_detail',rich_new_post.id)

def rich_edit(request,id):
    rich_edit_post = rich_Post.objects.get(id = id)
    return render(request, 'main/rich_edit.html', {'post':rich_edit_post})

def rich_update(request,id):
    rich_update_post = get_object_or_404(rich_Post, id = id)
    rich_update_post.title = request.POST['title']
    rich_update_post.writer = request.user
    rich_update_post.date = timezone.now()
    rich_update_post.body = request.POST['body']
    rich_update_post.image = request.FILES.get('image')
    rich_update_post.save()
    return redirect('main:rich_detail',rich_update_post.id)

def rich_delete(request,id):
    rich_delete_post = rich_Post.objects.get(id = id)
    rich_delete_post.delete()
    return redirect('main:rich')

# unsa
def unsa(request):
    posts = unsa_Post.objects.all()
    return render(request,'club/unsa.html',{'posts':posts})

def unsa_detail(request,id):
    unsa_post = get_object_or_404(unsa_Post, pk = id)
    return render(request,'main/unsa_detail.html',{'post':unsa_post})

def unsa_new(request):
    return render(request,'main/unsa_new.html')

def unsa_create(request):
    unsa_new_post = unsa_Post()
    unsa_new_post.title = request.POST['title']
    unsa_new_post.writer = request.user
    unsa_new_post.date = timezone.now()
    unsa_new_post.body = request.POST['body']
    unsa_new_post.image = request.FILES.get('image')
    unsa_new_post.save()
    return redirect('main:unsa_detail',unsa_new_post.id)

def unsa_edit(request,id):
    unsa_edit_post = unsa_Post.objects.get(id = id)
    return render(request, 'main/unsa_edit.html', {'post':unsa_edit_post})

def unsa_update(request,id):
    unsa_update_post = get_object_or_404(unsa_Post, id = id)
    unsa_update_post.title = request.POST['title']
    unsa_update_post.writer = request.user
    unsa_update_post.date = timezone.now()
    unsa_update_post.body = request.POST['body']
    unsa_update_post.image = request.FILES.get('image')
    unsa_update_post.save()
    return redirect('main:unsa_detail',unsa_update_post.id)

def unsa_delete(request,id):
    unsa_delete_post = unsa_Post.objects.get(id = id)
    unsa_delete_post.delete()
    return redirect('main:unsa')

# frontier
def frontier(request):
    posts = frontier_Post.objects.all()
    return render(request,'club/frontier.html',{'posts':posts})

def frontier_detail(request,id):
    frontier_post = get_object_or_404(frontier_Post, pk = id)
    return render(request,'main/frontier_detail.html',{'post':frontier_post})

def frontier_new(request):
    return render(request,'main/frontier_new.html')

def frontier_create(request):
    frontier_new_post = frontier_Post()
    frontier_new_post.title = request.POST['title']
    frontier_new_post.writer = request.user
    frontier_new_post.date = timezone.now()
    frontier_new_post.body = request.POST['body']
    frontier_new_post.image = request.FILES.get('image')
    frontier_new_post.save()
    return redirect('main:frontier_detail',frontier_new_post.id)

def frontier_edit(request,id):
    frontier_edit_post = frontier_Post.objects.get(id = id)
    return render(request, 'main/frontier_edit.html', {'post':frontier_edit_post})

def frontier_update(request,id):
    frontier_update_post = get_object_or_404(frontier_Post, id = id)
    frontier_update_post.title = request.POST['title']
    frontier_update_post.writer = request.user
    frontier_update_post.date = timezone.now()
    frontier_update_post.body = request.POST['body']
    frontier_update_post.image = request.FILES.get('image')
    frontier_update_post.save()
    return redirect('main:frontier_detail',frontier_update_post.id)

def frontier_delete(request,id):
    frontier_delete_post = frontier_Post.objects.get(id = id)
    frontier_delete_post.delete()
    return redirect('main:frontier')

# buddha
def buddha(request):
    posts = buddha_Post.objects.all()
    return render(request,'club/buddha.html',{'posts':posts})

def buddha_detail(request,id):
    buddha_post = get_object_or_404(buddha_Post, pk = id)
    return render(request,'main/buddha_detail.html',{'post':buddha_post})

def buddha_new(request):
    return render(request,'main/buddha_new.html')

def buddha_create(request):
    buddha_new_post = buddha_Post()
    buddha_new_post.title = request.POST['title']
    buddha_new_post.writer = request.user
    buddha_new_post.date = timezone.now()
    buddha_new_post.body = request.POST['body']
    buddha_new_post.image = request.FILES.get('image')
    buddha_new_post.save()
    return redirect('main:buddha_detail',buddha_new_post.id)

def buddha_edit(request,id):
    buddha_edit_post = buddha_Post.objects.get(id = id)
    return render(request, 'main/buddha_edit.html', {'post':buddha_edit_post})

def buddha_update(request,id):
    buddha_update_post = get_object_or_404(buddha_Post, id = id)
    buddha_update_post.title = request.POST['title']
    buddha_update_post.writer = request.user
    buddha_update_post.date = timezone.now()
    buddha_update_post.body = request.POST['body']
    buddha_update_post.image = request.FILES.get('image')
    buddha_update_post.save()
    return redirect('main:buddha_detail',buddha_update_post.id)

def buddha_delete(request,id):
    buddha_delete_post = buddha_Post.objects.get(id = id)
    buddha_delete_post.delete()
    return redirect('main:buddha')

# 체육분과
def dust(request):
    posts = Post.objects.all()
    return render(request,'club/dust.html',{'posts':posts})

def cave(request):
    posts = Post.objects.all()
    return render(request,'club/동굴탐험연구회.html',{'posts':posts})

def action(request):
    posts = Post.objects.all()
    return render(request,'club/무법.html',{'posts':posts})

def wind(request):
    posts = Post.objects.all()
    return render(request,'club/바람소리.html',{'posts':posts})

def mountain(request):
    posts = Post.objects.all()
    return render(request,'club/산악부.html',{'posts':posts})

def water(request):
    posts = Post.objects.all()
    return render(request,'club/수중탐구연구회.html',{'posts':posts})

def courtist(request):
    posts = Post.objects.all()
    return render(request,'club/courtist.html',{'posts':posts})

def dutc(request):
    posts = Post.objects.all()
    return render(request,'club/dutc.html',{'posts':posts})

def fctoto(request):
    posts = Post.objects.all()
    return render(request,'club/fctoto.html',{'posts':posts})

def lae(request):
    posts = Post.objects.all()
    return render(request,'club/lae.html',{'posts':posts})

def kendo(request):
    posts = Post.objects.all()
    return render(request,'club/검도부.html',{'posts':posts})

def baduk(request):
    posts = Post.objects.all()
    return render(request,'club/기우회.html',{'posts':posts})

def arrow(request):
    posts = Post.objects.all()
    return render(request,'club/명궁.html',{'posts':posts})

def taekwondo(request):
    posts = Post.objects.all()
    return render(request,'club/선무부.html',{'posts':posts})

def tuskers(request):
    posts = Post.objects.all()
    return render(request,'club/터스커스.html',{'posts':posts})

# 공연분과
def ajax(request):
    posts = ajax_Post.objects.all().order_by('-date')
    return render(request,'club/ajax.html',{'posts':posts})

def ajax_detail(request,id):
    ajax_post = get_object_or_404(ajax_Post, pk = id)
    return render(request,'main/ajax_detail.html',{'post':ajax_post})

def ajax_new(request):
    return render(request,'main/ajax_new.html')

def ajax_create(request):
    ajax_new_post = ajax_Post()
    ajax_new_post.title = request.POST['title']
    ajax_new_post.writer = request.user
    ajax_new_post.date = timezone.now()
    ajax_new_post.body = request.POST['body']
    ajax_new_post.image = request.FILES.get('image')
    ajax_new_post.save()
    return redirect('main:ajax_detail',ajax_new_post.id)

def ajax_edit(request,id):
    ajax_edit_post = ajax_Post.objects.get(id = id)
    return render(request, 'main/ajax_edit.html', {'post':ajax_edit_post})

def ajax_update(request,id):
    ajax_update_post = get_object_or_404(ajax_Post, id = id)
    ajax_update_post.title = request.POST['title']
    ajax_update_post.writer = request.user
    ajax_update_post.date = timezone.now()
    ajax_update_post.body = request.POST['body']
    ajax_update_post.image = request.FILES.get('image')
    ajax_update_post.save()
    return redirect('main:ajax_detail',ajax_update_post.id)

def ajax_delete(request,id):
    ajax_delete_post = ajax_Post.objects.get(id = id)
    ajax_delete_post.delete()
    return redirect('main:ajax')

#hola
def hola(request):
    posts = hola_Post.objects.all().order_by('-date')
    return render(request,'club/hola.html',{'posts':posts})

def hola_detail(request,id):
    hola_post = get_object_or_404(hola_Post, pk = id)
    return render(request,'main/hola_detail.html',{'post':hola_post})

def hola_new(request):
    return render(request,'main/hola_new.html')

def hola_create(request):
    hola_new_post = hola_Post()
    hola_new_post.title = request.POST['title']
    hola_new_post.writer = request.user
    hola_new_post.date = timezone.now()
    hola_new_post.body = request.POST['body']
    hola_new_post.image = request.FILES.get('image')
    hola_new_post.save()
    return redirect('main:hola_detail',hola_new_post.id)

def hola_edit(request,id):
    hola_edit_post = hola_Post.objects.get(id = id)
    return render(request, 'main/hola_edit.html', {'post':hola_edit_post})

def hola_update(request,id):
    hola_update_post = get_object_or_404(hola_Post, id = id)
    hola_update_post.title = request.POST['title']
    hola_update_post.writer = request.user
    hola_update_post.date = timezone.now()
    hola_update_post.body = request.POST['body']
    hola_update_post.image = request.FILES.get('image')
    hola_update_post.save()
    return redirect('main:hola_detail',hola_update_post.id)

def hola_delete(request,id):
    hola_delete_post = hola_Post.objects.get(id = id)
    hola_delete_post.delete()
    return redirect('main:hola')


def odc(request):
    posts = odc_Post.objects.all().order_by('-date')
    return render(request,'club/odc.html',{'posts':posts})

def odc_detail(request,id):
    odc_post = get_object_or_404(odc_Post, pk = id)
    return render(request,'main/odc_detail.html',{'post':odc_post})

def odc_new(request):
    return render(request,'main/odc_new.html')

def odc_create(request):
    odc_new_post = odc_Post()
    odc_new_post.title = request.POST['title']
    odc_new_post.writer = request.user
    odc_new_post.date = timezone.now()
    odc_new_post.body = request.POST['body']
    odc_new_post.image = request.FILES.get('image')
    odc_new_post.save()
    return redirect('main:odc_detail',odc_new_post.id)

def odc_edit(request,id):
    odc_edit_post = odc_Post.objects.get(id = id)
    return render(request, 'main/odc_edit.html', {'post':odc_edit_post})

def odc_update(request,id):
    odc_update_post = get_object_or_404(odc_Post, id = id)
    odc_update_post.title = request.POST['title']
    odc_update_post.writer = request.user
    odc_update_post.date = timezone.now()
    odc_update_post.body = request.POST['body']
    odc_update_post.image = request.FILES.get('image')
    odc_update_post.save()
    return redirect('main:odc_detail',odc_update_post.id)

def odc_delete(request,id):
    odc_delete_post = odc_Post.objects.get(id = id)
    odc_delete_post.delete()
    return redirect('main:odc')


def opus(request):
    posts = opus_Post.objects.all().order_by('-date')
    return render(request,'club/opus.html',{'posts':posts})

def opus_detail(request,id):
    opus_post = get_object_or_404(opus_Post, pk = id)
    return render(request,'main/opus_detail.html',{'post':opus_post})

def opus_new(request):
    return render(request,'main/opus_new.html')

def opus_create(request):
    opus_new_post = opus_Post()
    opus_new_post.title = request.POST['title']
    opus_new_post.writer = request.user
    opus_new_post.date = timezone.now()
    opus_new_post.body = request.POST['body']
    opus_new_post.image = request.FILES.get('image')
    opus_new_post.save()
    return redirect('main:opus_detail',opus_new_post.id)

def opus_edit(request,id):
    opus_edit_post = opus_Post.objects.get(id = id)
    return render(request, 'main/opus_edit.html', {'post':opus_edit_post})

def opus_update(request,id):
    opus_update_post = get_object_or_404(opus_Post, id = id)
    opus_update_post.title = request.POST['title']
    opus_update_post.writer = request.user
    opus_update_post.date = timezone.now()
    opus_update_post.body = request.POST['body']
    opus_update_post.image = request.FILES.get('image')
    opus_update_post.save()
    return redirect('main:opus_detail',opus_update_post.id)

def opus_delete(request,id):
    opus_delete_post = opus_Post.objects.get(id = id)
    opus_delete_post.delete()
    return redirect('main:opus')

def drama(request):
    posts = drama_Post.objects.all().order_by('-date')
    return render(request,'club/drama.html',{'posts':posts})

def drama_detail(request,id):
    drama_post = get_object_or_404(drama_Post, pk = id)
    return render(request,'main/drama_detail.html',{'post':drama_post})

def drama_new(request):
    return render(request,'main/drama_new.html')

def drama_create(request):
    drama_new_post = drama_Post()
    drama_new_post.title = request.POST['title']
    drama_new_post.writer = request.user
    drama_new_post.date = timezone.now()
    drama_new_post.body = request.POST['body']
    drama_new_post.image = request.FILES.get('image')
    drama_new_post.save()
    return redirect('main:drama_detail',drama_new_post.id)

def drama_edit(request,id):
    drama_edit_post = drama_Post.objects.get(id = id)
    return render(request, 'main/drama_edit.html', {'post':drama_edit_post})

def drama_update(request,id):
    drama_update_post = get_object_or_404(drama_Post, id = id)
    drama_update_post.title = request.POST['title']
    drama_update_post.writer = request.user
    drama_update_post.date = timezone.now()
    drama_update_post.body = request.POST['body']
    drama_update_post.image = request.FILES.get('image')
    drama_update_post.save()
    return redirect('main:drama_detail',drama_update_post.id)

def drama_delete(request,id):
    drama_delete_post = drama_Post.objects.get(id = id)
    drama_delete_post.delete()
    return redirect('main:drama')

#lotus

def lotus(request):
    posts = lotus_Post.objects.all().order_by('-date')
    return render(request,'club/lotus.html',{'posts':posts})

def lotus_detail(request,id):
    lotus_post = get_object_or_404(lotus_Post, pk = id)
    return render(request,'main/lotus_detail.html',{'post':lotus_post})

def lotus_new(request):
    return render(request,'main/lotus_new.html')

def lotus_create(request):
    lotus_new_post = lotus_Post()
    lotus_new_post.title = request.POST['title']
    lotus_new_post.writer = request.user
    lotus_new_post.date = timezone.now()
    lotus_new_post.body = request.POST['body']
    lotus_new_post.image = request.FILES.get('image')
    lotus_new_post.save()
    return redirect('main:lotus_detail',lotus_new_post.id)

def lotus_edit(request,id):
    lotus_edit_post = lotus_Post.objects.get(id = id)
    return render(request, 'main/lotus_edit.html', {'post':lotus_edit_post})

def lotus_update(request,id):
    lotus_update_post = get_object_or_404(lotus_Post, id = id)
    lotus_update_post.title = request.POST['title']
    lotus_update_post.writer = request.user
    lotus_update_post.date = timezone.now()
    lotus_update_post.body = request.POST['body']
    lotus_update_post.image = request.FILES.get('image')
    lotus_update_post.save()
    return redirect('main:lotus_detail',lotus_update_post.id)

def lotus_delete(request,id):
    lotus_delete_post = lotus_Post.objects.get(id = id)
    lotus_delete_post.delete()
    return redirect('main:lotus')

#cloud

def cloud(request):
    posts = cloud_Post.objects.all().order_by('-date')
    return render(request,'club/cloud.html',{'posts':posts})

def cloud_detail(request,id):
    cloud_post = get_object_or_404(cloud_Post, pk = id)
    return render(request,'main/cloud_detail.html',{'post':cloud_post})

def cloud_new(request):
    return render(request,'main/cloud_new.html')

def cloud_create(request):
    cloud_new_post = cloud_Post()
    cloud_new_post.title = request.POST['title']
    cloud_new_post.writer = request.user
    cloud_new_post.date = timezone.now()
    cloud_new_post.body = request.POST['body']
    cloud_new_post.image = request.FILES.get('image')
    cloud_new_post.save()
    return redirect('main:cloud_detail',cloud_new_post.id)

def cloud_edit(request,id):
    cloud_edit_post = cloud_Post.objects.get(id = id)
    return render(request, 'main/cloud_edit.html', {'post':cloud_edit_post})

def cloud_update(request,id):
    cloud_update_post = get_object_or_404(cloud_Post, id = id)
    cloud_update_post.title = request.POST['title']
    cloud_update_post.writer = request.user
    cloud_update_post.date = timezone.now()
    cloud_update_post.body = request.POST['body']
    cloud_update_post.image = request.FILES.get('image')
    cloud_update_post.save()
    return redirect('main:cloud_detail',cloud_update_post.id)

def cloud_delete(request,id):
    cloud_delete_post = cloud_Post.objects.get(id = id)
    cloud_delete_post.delete()
    return redirect('main:cloud')

#arirang

def arirang(request):
    posts = arirang_Post.objects.all().order_by('-date')
    return render(request,'club/arirang.html',{'posts':posts})

def arirang_detail(request,id):
    arirang_post = get_object_or_404(arirang_Post, pk = id)
    return render(request,'main/arirang_detail.html',{'post':arirang_post})

def arirang_new(request):
    return render(request,'main/arirang_new.html')

def arirang_create(request):
    arirang_new_post = arirang_Post()
    arirang_new_post.title = request.POST['title']
    arirang_new_post.writer = request.user
    arirang_new_post.date = timezone.now()
    arirang_new_post.body = request.POST['body']
    arirang_new_post.image = request.FILES.get('image')
    arirang_new_post.save()
    return redirect('main:arirang_detail',arirang_new_post.id)

def arirang_edit(request,id):
    arirang_edit_post = arirang_Post.objects.get(id = id)
    return render(request, 'main/arirang_edit.html', {'post':arirang_edit_post})

def arirang_update(request,id):
    arirang_update_post = get_object_or_404(arirang_Post, id = id)
    arirang_update_post.title = request.POST['title']
    arirang_update_post.writer = request.user
    arirang_update_post.date = timezone.now()
    arirang_update_post.body = request.POST['body']
    arirang_update_post.image = request.FILES.get('image')
    arirang_update_post.save()
    return redirect('main:arirang_detail',arirang_update_post.id)

def arirang_delete(request,id):
    arirang_delete_post = arirang_Post.objects.get(id = id)
    arirang_delete_post.delete()
    return redirect('main:arirang')


#eumsem

def eumsem(request):
    posts = eumsem_Post.objects.all().order_by('-date')
    return render(request,'club/eumsem.html',{'posts':posts})

def eumsem_detail(request,id):
    eumsem_post = get_object_or_404(eumsem_Post, pk = id)
    return render(request,'main/eumsem_detail.html',{'post':eumsem_post})

def eumsem_new(request):
    return render(request,'main/eumsem_new.html')

def eumsem_create(request):
    eumsem_new_post = eumsem_Post()
    eumsem_new_post.title = request.POST['title']
    eumsem_new_post.writer = request.user
    eumsem_new_post.date = timezone.now()
    eumsem_new_post.body = request.POST['body']
    eumsem_new_post.image = request.FILES.get('image')
    eumsem_new_post.save()
    return redirect('main:eumsem_detail',eumsem_new_post.id)

def eumsem_edit(request,id):
    eumsem_edit_post = eumsem_Post.objects.get(id = id)
    return render(request, 'main/eumsem_edit.html', {'post':eumsem_edit_post})

def eumsem_update(request,id):
    eumsem_update_post = get_object_or_404(eumsem_Post, id = id)
    eumsem_update_post.title = request.POST['title']
    eumsem_update_post.writer = request.user
    eumsem_update_post.date = timezone.now()
    eumsem_update_post.body = request.POST['body']
    eumsem_update_post.image = request.FILES.get('image')
    eumsem_update_post.save()
    return redirect('main:eumsem_detail',eumsem_update_post.id)

def eumsem_delete(request,id):
    eumsem_delete_post = eumsem_Post.objects.get(id = id)
    eumsem_delete_post.delete()
    return redirect('main:eumsem')

#fearless

def fearless(request):
    posts = fearless_Post.objects.all().order_by('-date')
    return render(request,'club/fearless.html',{'posts':posts})

def fearless_detail(request,id):
    fearless_post = get_object_or_404(fearless_Post, pk = id)
    return render(request,'main/fearless_detail.html',{'post':fearless_post})

def fearless_new(request):
    return render(request,'main/fearless_new.html')

def fearless_create(request):
    fearless_new_post = fearless_Post()
    fearless_new_post.title = request.POST['title']
    fearless_new_post.writer = request.user
    fearless_new_post.date = timezone.now()
    fearless_new_post.body = request.POST['body']
    fearless_new_post.image = request.FILES.get('image')
    fearless_new_post.save()
    return redirect('main:fearless_detail',fearless_new_post.id)

def fearless_edit(request,id):
    fearless_edit_post = fearless_Post.objects.get(id = id)
    return render(request, 'main/fearless_edit.html', {'post':fearless_edit_post})

def fearless_update(request,id):
    fearless_update_post = get_object_or_404(fearless_Post, id = id)
    fearless_update_post.title = request.POST['title']
    fearless_update_post.writer = request.user
    fearless_update_post.date = timezone.now()
    fearless_update_post.body = request.POST['body']
    fearless_update_post.image = request.FILES.get('image')
    fearless_update_post.save()
    return redirect('main:fearless_detail',fearless_update_post.id)

def fearless_delete(request,id):
    fearless_delete_post = fearless_Post.objects.get(id = id)
    fearless_delete_post.delete()
    return redirect('main:fearless')

#yeoul

def yeoul(request):
    posts = yeoul_Post.objects.all().order_by('-date')
    return render(request,'club/yeoul.html',{'posts':posts})

def yeoul_detail(request,id):
    yeoul_post = get_object_or_404(yeoul_Post, pk = id)
    return render(request,'main/yeoul_detail.html',{'post':yeoul_post})

def yeoul_new(request):
    return render(request,'main/yeoul_new.html')

def yeoul_create(request):
    yeoul_new_post = yeoul_Post()
    yeoul_new_post.title = request.POST['title']
    yeoul_new_post.writer = request.user
    yeoul_new_post.date = timezone.now()
    yeoul_new_post.body = request.POST['body']
    yeoul_new_post.image = request.FILES.get('image')
    yeoul_new_post.save()
    return redirect('main:yeoul_detail',yeoul_new_post.id)

def yeoul_edit(request,id):
    yeoul_edit_post = yeoul_Post.objects.get(id = id)
    return render(request, 'main/yeoul_edit.html', {'post':yeoul_edit_post})

def yeoul_update(request,id):
    yeoul_update_post = get_object_or_404(yeoul_Post, id = id)
    yeoul_update_post.title = request.POST['title']
    yeoul_update_post.writer = request.user
    yeoul_update_post.date = timezone.now()
    yeoul_update_post.body = request.POST['body']
    yeoul_update_post.image = request.FILES.get('image')
    yeoul_update_post.save()
    return redirect('main:yeoul_detail',yeoul_update_post.id)

def yeoul_delete(request,id):
    yeoul_delete_post = yeoul_Post.objects.get(id = id)
    yeoul_delete_post.delete()
    return redirect('main:yeoul')

# 예창분과
def draw(request):
    posts = Post.objects.all()
    return render(request,'club/그리고그림.html',{'posts':posts})

def literal(request):
    posts = Post.objects.all()
    return render(request,'club/동국문학회.html',{'posts':posts})

def calligraphy(request):
    posts = Post.objects.all()
    return render(request,'club/동국서도회.html',{'posts':posts})

def circle(request):
    posts = Post.objects.all()
    return render(request,'club/동그라미.html',{'posts':posts})

def stone(request):
    posts = Post.objects.all()
    return render(request,'club/디딤돌.html',{'posts':posts})

def cartoon(request):
    posts = Post.objects.all()
    return render(request,'club/만화얼.html',{'posts':posts})

def rush(request):
    posts = Post.objects.all()
    return render(request,'club/애드러쉬.html',{'posts':posts})

# 신규분과
# elephente
def elephente(request):
    posts = elephente_Post.objects.all()
    return render(request,'club/elephente.html',{'posts':posts})

def elephente_detail(request,id):
    elephente_post = get_object_or_404(elephente_Post, pk = id)
    return render(request,'main/elephente_detail.html',{'post':elephente_post})

def elephente_new(request):
    return render(request,'main/elephente_new.html')

def elephente_create(request):
    elephente_new_post = elephente_Post()
    elephente_new_post.title = request.POST['title']
    elephente_new_post.writer = request.user
    elephente_new_post.date = timezone.now()
    elephente_new_post.body = request.POST['body']
    elephente_new_post.image = request.FILES.get('image')
    elephente_new_post.save()
    return redirect('main:elephente_detail',elephente_new_post.id)

def elephente_edit(request,id):
    elephente_edit_post = elephente_Post.objects.get(id = id)
    return render(request, 'main/elephente_edit.html', {'post':elephente_edit_post})

def elephente_update(request,id):
    elephente_update_post = get_object_or_404(elephente_Post, id = id)
    elephente_update_post.title = request.POST['title']
    elephente_update_post.writer = request.user
    elephente_update_post.date = timezone.now()
    elephente_update_post.body = request.POST['body']
    elephente_update_post.image = request.FILES.get('image')
    elephente_update_post.save()
    return redirect('main:elephente_detail',elephente_update_post.id)

def elephente_delete(request,id):
    elephente_delete_post = elephente_Post.objects.get(id = id)
    elephente_delete_post.delete()
    return redirect('main:elephente')

# doomchit
def doomchit(request):
    posts = doomchit_Post.objects.all()
    return render(request,'club/doomchit.html',{'posts':posts})

def doomchit_detail(request,id):
    doomchit_post = get_object_or_404(doomchit_Post, pk = id)
    return render(request,'main/doomchit_detail.html',{'post':doomchit_post})

def doomchit_new(request):
    return render(request,'main/doomchit_new.html')

def doomchit_create(request):
    doomchit_new_post = doomchit_Post()
    doomchit_new_post.title = request.POST['title']
    doomchit_new_post.writer = request.user
    doomchit_new_post.date = timezone.now()
    doomchit_new_post.body = request.POST['body']
    doomchit_new_post.image = request.FILES.get('image')
    doomchit_new_post.save()
    return redirect('main:doomchit_detail',doomchit_new_post.id)

def doomchit_edit(request,id):
    doomchit_edit_post = doomchit_Post.objects.get(id = id)
    return render(request, 'main/doomchit_edit.html', {'post':doomchit_edit_post})

def doomchit_update(request,id):
    doomchit_update_post = get_object_or_404(doomchit_Post, id = id)
    doomchit_update_post.title = request.POST['title']
    doomchit_update_post.writer = request.user
    doomchit_update_post.date = timezone.now()
    doomchit_update_post.body = request.POST['body']
    doomchit_update_post.image = request.FILES.get('image')
    doomchit_update_post.save()
    return redirect('main:doomchit_detail',doomchit_update_post.id)

def doomchit_delete(request,id):
    doomchit_delete_post = doomchit_Post.objects.get(id = id)
    doomchit_delete_post.delete()
    return redirect('main:doomchit')

# enactus
def enactus(request):
    posts = enactus_Post.objects.all()
    return render(request,'club/enactus.html',{'posts':posts})

def enactus_detail(request,id):
    enactus_post = get_object_or_404(enactus_Post, pk = id)
    return render(request,'main/enactus_detail.html',{'post':enactus_post})

def enactus_new(request):
    return render(request,'main/enactus_new.html')

def enactus_create(request):
    enactus_new_post = enactus_Post()
    enactus_new_post.title = request.POST['title']
    enactus_new_post.writer = request.user
    enactus_new_post.date = timezone.now()
    enactus_new_post.body = request.POST['body']
    enactus_new_post.image = request.FILES.get('image')
    enactus_new_post.save()
    return redirect('main:enactus_detail',enactus_new_post.id)

def enactus_edit(request,id):
    enactus_edit_post = enactus_Post.objects.get(id = id)
    return render(request, 'main/enactus_edit.html', {'post':enactus_edit_post})

def enactus_update(request,id):
    enactus_update_post = get_object_or_404(enactus_Post, id = id)
    enactus_update_post.title = request.POST['title']
    enactus_update_post.writer = request.user
    enactus_update_post.date = timezone.now()
    enactus_update_post.body = request.POST['body']
    enactus_update_post.image = request.FILES.get('image')
    enactus_update_post.save()
    return redirect('main:enactus_detail',enactus_update_post.id)

def enactus_delete(request,id):
    enactus_delete_post = enactus_Post.objects.get(id = id)
    enactus_delete_post.delete()
    return redirect('main:enactus')

# jam
def jam(request):
    posts = jam_Post.objects.all()
    return render(request,'club/jam.html',{'posts':posts})

def jam_detail(request,id):
    jam_post = get_object_or_404(jam_Post, pk = id)
    return render(request,'main/jam_detail.html',{'post':jam_post})

def jam_new(request):
    return render(request,'main/jam_new.html')

def jam_create(request):
    jam_new_post = jam_Post()
    jam_new_post.title = request.POST['title']
    jam_new_post.writer = request.user
    jam_new_post.date = timezone.now()
    jam_new_post.body = request.POST['body']
    jam_new_post.image = request.FILES.get('image')
    jam_new_post.save()
    return redirect('main:jam_detail',jam_new_post.id)

def jam_edit(request,id):
    jam_edit_post = jam_Post.objects.get(id = id)
    return render(request, 'main/jam_edit.html', {'post':jam_edit_post})

def jam_update(request,id):
    jam_update_post = get_object_or_404(jam_Post, id = id)
    jam_update_post.title = request.POST['title']
    jam_update_post.writer = request.user
    jam_update_post.date = timezone.now()
    jam_update_post.body = request.POST['body']
    jam_update_post.image = request.FILES.get('image')
    jam_update_post.save()
    return redirect('main:jam_detail',jam_update_post.id)

def jam_delete(request,id):
    jam_delete_post = jam_Post.objects.get(id = id)
    jam_delete_post.delete()
    return redirect('main:jam')

# qud
def qud(request):
    posts = qud_Post.objects.all()
    return render(request,'club/qud.html',{'posts':posts})

def qud_detail(request,id):
    qud_post = get_object_or_404(qud_Post, pk = id)
    return render(request,'main/qud_detail.html',{'post':qud_post})

def qud_new(request):
    return render(request,'main/qud_new.html')

def qud_create(request):
    qud_new_post = qud_Post()
    qud_new_post.title = request.POST['title']
    qud_new_post.writer = request.user
    qud_new_post.date = timezone.now()
    qud_new_post.body = request.POST['body']
    qud_new_post.image = request.FILES.get('image')
    qud_new_post.save()
    return redirect('main:qud_detail',qud_new_post.id)

def qud_edit(request,id):
    qud_edit_post = qud_Post.objects.get(id = id)
    return render(request, 'main/qud_edit.html', {'post':qud_edit_post})

def qud_update(request,id):
    qud_update_post = get_object_or_404(qud_Post, id = id)
    qud_update_post.title = request.POST['title']
    qud_update_post.writer = request.user
    qud_update_post.date = timezone.now()
    qud_update_post.body = request.POST['body']
    qud_update_post.image = request.FILES.get('image')
    qud_update_post.save()
    return redirect('main:qud_detail',qud_update_post.id)

def qud_delete(request,id):
    qud_delete_post = qud_Post.objects.get(id = id)
    qud_delete_post.delete()
    return redirect('main:qud')

