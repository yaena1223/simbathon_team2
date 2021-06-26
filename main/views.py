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
    posts = dna_Post.objects.all().order_by('-date')
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
    posts = dussa_Post.objects.all().order_by('-date')
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
    posts = kcc_Post.objects.all().order_by('-date')
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
    posts = mecs_Post.objects.all().order_by('-date')
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
    posts = nsa_Post.objects.all().order_by('-date')
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
    posts = marx_Post.objects.all().order_by('-date')
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

#elf   
def elf(request):
    posts = elf_Post.objects.all().order_by('-date')
    return render(request,'club/elf.html',{'posts':posts})

def elf_detail(request,id):
    elf_post = get_object_or_404(elf_Post, pk = id)
    return render(request,'main/elf_detail.html',{'post':elf_post})

def elf_new(request):
    return render(request,'main/elf_new.html')

def elf_create(request):
    elf_new_post = elf_Post()
    elf_new_post.title = request.POST['title']
    elf_new_post.writer = request.user
    elf_new_post.date = timezone.now()
    elf_new_post.body = request.POST['body']
    elf_new_post.image = request.FILES.get('image')
    elf_new_post.save()
    return redirect('main:elf_detail',elf_new_post.id)

def elf_edit(request,id):
    elf_edit_post = elf_Post.objects.get(id = id)
    return render(request, 'main/elf_edit.html', {'post':elf_edit_post})

def elf_update(request,id):
    elf_update_post = get_object_or_404(elf_Post, id = id)
    elf_update_post.title = request.POST['title']
    elf_update_post.writer = request.user
    elf_update_post.date = timezone.now()
    elf_update_post.body = request.POST['body']
    elf_update_post.image = request.FILES.get('image')
    elf_update_post.save()
    return redirect('main:elf_detail',elf_update_post.id)

def elf_delete(request,id):
    elf_delete_post = elf_Post.objects.get(id = id)
    elf_delete_post.delete()
    return redirect('main:elf')

#rcy
def rcy(request):
    posts = rcy_Post.objects.all().order_by('-date')
    return render(request,'club/rcy.html',{'posts':posts})

def rcy_detail(request,id):
    rcy_post = get_object_or_404(rcy_Post, pk = id)
    return render(request,'main/rcy_detail.html',{'post':rcy_post})

def rcy_new(request):
    return render(request,'main/rcy_new.html')

def rcy_create(request):
    rcy_new_post = rcy_Post()
    rcy_new_post.title = request.POST['title']
    rcy_new_post.writer = request.user
    rcy_new_post.date = timezone.now()
    rcy_new_post.body = request.POST['body']
    rcy_new_post.image = request.FILES.get('image')
    rcy_new_post.save()
    return redirect('main:rcy_detail',rcy_new_post.id)

def rcy_edit(request,id):
    rcy_edit_post = rcy_Post.objects.get(id = id)
    return render(request, 'main/rcy_edit.html', {'post':rcy_edit_post})

def rcy_update(request,id):
    rcy_update_post = get_object_or_404(rcy_Post, id = id)
    rcy_update_post.title = request.POST['title']
    rcy_update_post.writer = request.user
    rcy_update_post.date = timezone.now()
    rcy_update_post.body = request.POST['body']
    rcy_update_post.image = request.FILES.get('image')
    rcy_update_post.save()
    return redirect('main:rcy_detail',rcy_update_post.id)

def rcy_delete(request,id):
    rcy_delete_post = rcy_Post.objects.get(id = id)
    rcy_delete_post.delete()
    return redirect('main:rcy')

#road 
def road(request):
    posts = road_Post.objects.all().order_by('-date')
    return render(request,'club/road.html',{'posts':posts})

def road_detail(request,id):
    road_post = get_object_or_404(road_Post, pk = id)
    return render(request,'main/road_detail.html',{'post':road_post})

def road_new(request):
    return render(request,'main/road_new.html')

def road_create(request):
    road_new_post = road_Post()
    road_new_post.title = request.POST['title']
    road_new_post.writer = request.user
    road_new_post.date = timezone.now()
    road_new_post.body = request.POST['body']
    road_new_post.image = request.FILES.get('image')
    road_new_post.save()
    return redirect('main:road_detail',road_new_post.id)

def road_edit(request,id):
    road_edit_post = road_Post.objects.get(id = id)
    return render(request, 'main/road_edit.html', {'post':road_edit_post})

def road_update(request,id):
    road_update_post = get_object_or_404(road_Post, id = id)
    road_update_post.title = request.POST['title']
    road_update_post.writer = request.user
    road_update_post.date = timezone.now()
    road_update_post.body = request.POST['body']
    road_update_post.image = request.FILES.get('image')
    road_update_post.save()
    return redirect('main:road_detail',road_update_post.id)

def road_delete(request,id):
    road_delete_post = road_Post.objects.get(id = id)
    road_delete_post.delete()
    return redirect('main:road')

#hand 
def hand(request):
    posts = hand_Post.objects.all().order_by('-date')
    return render(request,'club/hand.html',{'posts':posts})

def hand_detail(request,id):
    hand_post = get_object_or_404(hand_Post, pk = id)
    return render(request,'main/hand_detail.html',{'post':hand_post})

def hand_new(request):
    return render(request,'main/hand_new.html')

def hand_create(request):
    hand_new_post = hand_Post()
    hand_new_post.title = request.POST['title']
    hand_new_post.writer = request.user
    hand_new_post.date = timezone.now()
    hand_new_post.body = request.POST['body']
    hand_new_post.image = request.FILES.get('image')
    hand_new_post.save()
    return redirect('main:hand_detail',hand_new_post.id)

def hand_edit(request,id):
    hand_edit_post = hand_Post.objects.get(id = id)
    return render(request, 'main/hand_edit.html', {'post':hand_edit_post})

def hand_update(request,id):
    hand_update_post = get_object_or_404(hand_Post, id = id)
    hand_update_post.title = request.POST['title']
    hand_update_post.writer = request.user
    hand_update_post.date = timezone.now()
    hand_update_post.body = request.POST['body']
    hand_update_post.image = request.FILES.get('image')
    hand_update_post.save()
    return redirect('main:hand_detail',hand_update_post.id)

def hand_delete(request,id):
    hand_delete_post = hand_Post.objects.get(id = id)
    hand_delete_post.delete()
    return redirect('main:hand')

#neighbor  
def neighbor(request):
    posts = neighbor_Post.objects.all().order_by('-date')
    return render(request,'club/neighbor.html',{'posts':posts})

def neighbor_detail(request,id):
    neighbor_post = get_object_or_404(neighbor_Post, pk = id)
    return render(request,'main/neighbor_detail.html',{'post':neighbor_post})

def neighbor_new(request):
    return render(request,'main/neighbor_new.html')

def neighbor_create(request):
    neighbor_new_post = neighbor_Post()
    neighbor_new_post.title = request.POST['title']
    neighbor_new_post.writer = request.user
    neighbor_new_post.date = timezone.now()
    neighbor_new_post.body = request.POST['body']
    neighbor_new_post.image = request.FILES.get('image')
    neighbor_new_post.save()
    return redirect('main:neighbor_detail',neighbor_new_post.id)

def neighbor_edit(request,id):
    neighbor_edit_post = neighbor_Post.objects.get(id = id)
    return render(request, 'main/neighbor_edit.html', {'post':neighbor_edit_post})

def neighbor_update(request,id):
    neighbor_update_post = get_object_or_404(neighbor_Post, id = id)
    neighbor_update_post.title = request.POST['title']
    neighbor_update_post.writer = request.user
    neighbor_update_post.date = timezone.now()
    neighbor_update_post.body = request.POST['body']
    neighbor_update_post.image = request.FILES.get('image')
    neighbor_update_post.save()
    return redirect('main:neighbor_detail',neighbor_update_post.id)

def neighbor_delete(request,id):
    neighbor_delete_post = neighbor_Post.objects.get(id = id)
    neighbor_delete_post.delete()
    return redirect('main:neighbor')

#painters   
def painters(request):
    posts = painters_Post.objects.all().order_by('-date')
    return render(request,'club/painters.html',{'posts':posts})

def painters_detail(request,id):
    painters_post = get_object_or_404(painters_Post, pk = id)
    return render(request,'main/painters_detail.html',{'post':painters_post})

def painters_new(request):
    return render(request,'main/painters_new.html')

def painters_create(request):
    painters_new_post = painters_Post()
    painters_new_post.title = request.POST['title']
    painters_new_post.writer = request.user
    painters_new_post.date = timezone.now()
    painters_new_post.body = request.POST['body']
    painters_new_post.image = request.FILES.get('image')
    painters_new_post.save()
    return redirect('main:painters_detail',painters_new_post.id)

def painters_edit(request,id):
    painters_edit_post = painters_Post.objects.get(id = id)
    return render(request, 'main/painters_edit.html', {'post':painters_edit_post})

def painters_update(request,id):
    painters_update_post = get_object_or_404(painters_Post, id = id)
    painters_update_post.title = request.POST['title']
    painters_update_post.writer = request.user
    painters_update_post.date = timezone.now()
    painters_update_post.body = request.POST['body']
    painters_update_post.image = request.FILES.get('image')
    painters_update_post.save()
    return redirect('main:painters_detail',painters_update_post.id)

def painters_delete(request,id):
    painters_delete_post = painters_Post.objects.get(id = id)
    painters_delete_post.delete()
    return redirect('main:painters')

#green   
def green(request):
    posts = green_Post.objects.all().order_by('-date')
    return render(request,'club/green.html',{'posts':posts})

def green_detail(request,id):
    green_post = get_object_or_404(green_Post, pk = id)
    return render(request,'main/green_detail.html',{'post':green_post})

def green_new(request):
    return render(request,'main/green_new.html')

def green_create(request):
    green_new_post = green_Post()
    green_new_post.title = request.POST['title']
    green_new_post.writer = request.user
    green_new_post.date = timezone.now()
    green_new_post.body = request.POST['body']
    green_new_post.image = request.FILES.get('image')
    green_new_post.save()
    return redirect('main:green_detail',green_new_post.id)

def green_edit(request,id):
    green_edit_post = green_Post.objects.get(id = id)
    return render(request, 'main/green_edit.html', {'post':green_edit_post})

def green_update(request,id):
    green_update_post = get_object_or_404(green_Post, id = id)
    green_update_post.title = request.POST['title']
    green_update_post.writer = request.user
    green_update_post.date = timezone.now()
    green_update_post.body = request.POST['body']
    green_update_post.image = request.FILES.get('image')
    green_update_post.save()
    return redirect('main:green_detail',green_update_post.id)

def green_delete(request,id):
    green_delete_post = green_Post.objects.get(id = id)
    green_delete_post.delete()
    return redirect('main:green')

#korean   
def korean(request):
    posts = korean_Post.objects.all().order_by('-date')
    return render(request,'club/korean.html',{'posts':posts})

def korean_detail(request,id):
    korean_post = get_object_or_404(korean_Post, pk = id)
    return render(request,'main/korean_detail.html',{'post':korean_post})

def korean_new(request):
    return render(request,'main/korean_new.html')

def korean_create(request):
    korean_new_post = korean_Post()
    korean_new_post.title = request.POST['title']
    korean_new_post.writer = request.user
    korean_new_post.date = timezone.now()
    korean_new_post.body = request.POST['body']
    korean_new_post.image = request.FILES.get('image')
    korean_new_post.save()
    return redirect('main:korean_detail',korean_new_post.id)

def korean_edit(request,id):
    korean_edit_post = korean_Post.objects.get(id = id)
    return render(request, 'main/korean_edit.html', {'post':korean_edit_post})

def korean_update(request,id):
    korean_update_post = get_object_or_404(korean_Post, id = id)
    korean_update_post.title = request.POST['title']
    korean_update_post.writer = request.user
    korean_update_post.date = timezone.now()
    korean_update_post.body = request.POST['body']
    korean_update_post.image = request.FILES.get('image')
    korean_update_post.save()
    return redirect('main:korean_detail',korean_update_post.id)

def korean_delete(request,id):
    korean_delete_post = korean_Post.objects.get(id = id)
    korean_delete_post.delete()
    return redirect('main:korean')


# 사회분과
# kusa
def kusa(request):
    posts = kusa_Post.objects.all().order_by('-date')
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
    posts = rich_Post.objects.all().order_by('-date')
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
    posts = unsa_Post.objects.all().order_by('-date')
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
    posts = frontier_Post.objects.all().order_by('-date')
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
    posts = buddha_Post.objects.all().order_by('-date')
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


# 공연분과
# ajax
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

# hola
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

# odc
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

# opus
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

# drama
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

#draw

def draw(request):
    posts = draw_Post.objects.all().order_by('-date')
    return render(request,'club/draw.html',{'posts':posts})

def draw_detail(request,id):
    draw_post = get_object_or_404(draw_Post, pk = id)
    return render(request,'main/draw_detail.html',{'post':draw_post})

def draw_new(request):
    return render(request,'main/draw_new.html')

def draw_create(request):
    draw_new_post = draw_Post()
    draw_new_post.title = request.POST['title']
    draw_new_post.writer = request.user
    draw_new_post.date = timezone.now()
    draw_new_post.body = request.POST['body']
    draw_new_post.image = request.FILES.get('image')
    draw_new_post.save()
    return redirect('main:draw_detail',draw_new_post.id)

def draw_edit(request,id):
    draw_edit_post = draw_Post.objects.get(id = id)
    return render(request, 'main/draw_edit.html', {'post':draw_edit_post})

def draw_update(request,id):
    draw_update_post = get_object_or_404(draw_Post, id = id)
    draw_update_post.title = request.POST['title']
    draw_update_post.writer = request.user
    draw_update_post.date = timezone.now()
    draw_update_post.body = request.POST['body']
    draw_update_post.image = request.FILES.get('image')
    draw_update_post.save()
    return redirect('main:draw_detail',draw_update_post.id)

def draw_delete(request,id):
    draw_delete_post = draw_Post.objects.get(id = id)
    draw_delete_post.delete()
    return redirect('main:draw')

#literal

def literal(request):
    posts = literal_Post.objects.all().order_by('-date')
    return render(request,'club/literal.html',{'posts':posts})

def literal_detail(request,id):
    literal_post = get_object_or_404(literal_Post, pk = id)
    return render(request,'main/literal_detail.html',{'post':literal_post})

def literal_new(request):
    return render(request,'main/literal_new.html')

def literal_create(request):
    literal_new_post = literal_Post()
    literal_new_post.title = request.POST['title']
    literal_new_post.writer = request.user
    literal_new_post.date = timezone.now()
    literal_new_post.body = request.POST['body']
    literal_new_post.image = request.FILES.get('image')
    literal_new_post.save()
    return redirect('main:literal_detail',literal_new_post.id)

def literal_edit(request,id):
    literal_edit_post = literal_Post.objects.get(id = id)
    return render(request, 'main/literal_edit.html', {'post':literal_edit_post})

def literal_update(request,id):
    literal_update_post = get_object_or_404(literal_Post, id = id)
    literal_update_post.title = request.POST['title']
    literal_update_post.writer = request.user
    literal_update_post.date = timezone.now()
    literal_update_post.body = request.POST['body']
    literal_update_post.image = request.FILES.get('image')
    literal_update_post.save()
    return redirect('main:literal_detail',literal_update_post.id)

def literal_delete(request,id):
    literal_delete_post = literal_Post.objects.get(id = id)
    literal_delete_post.delete()
    return redirect('main:literal')


#calligraphy

def calligraphy(request):
    posts = calligraphy_Post.objects.all().order_by('-date')
    return render(request,'club/calligraphy.html',{'posts':posts})

def calligraphy_detail(request,id):
    calligraphy_post = get_object_or_404(calligraphy_Post, pk = id)
    return render(request,'main/calligraphy_detail.html',{'post':calligraphy_post})

def calligraphy_new(request):
    return render(request,'main/calligraphy_new.html')

def calligraphy_create(request):
    calligraphy_new_post = calligraphy_Post()
    calligraphy_new_post.title = request.POST['title']
    calligraphy_new_post.writer = request.user
    calligraphy_new_post.date = timezone.now()
    calligraphy_new_post.body = request.POST['body']
    calligraphy_new_post.image = request.FILES.get('image')
    calligraphy_new_post.save()
    return redirect('main:calligraphy_detail',calligraphy_new_post.id)

def calligraphy_edit(request,id):
    calligraphy_edit_post = calligraphy_Post.objects.get(id = id)
    return render(request, 'main/calligraphy_edit.html', {'post':calligraphy_edit_post})

def calligraphy_update(request,id):
    calligraphy_update_post = get_object_or_404(calligraphy_Post, id = id)
    calligraphy_update_post.title = request.POST['title']
    calligraphy_update_post.writer = request.user
    calligraphy_update_post.date = timezone.now()
    calligraphy_update_post.body = request.POST['body']
    calligraphy_update_post.image = request.FILES.get('image')
    calligraphy_update_post.save()
    return redirect('main:calligraphy_detail',calligraphy_update_post.id)

def calligraphy_delete(request,id):
    calligraphy_delete_post = calligraphy_Post.objects.get(id = id)
    calligraphy_delete_post.delete()
    return redirect('main:calligraphy')


#circle

def circle(request):
    posts = circle_Post.objects.all().order_by('-date')
    return render(request,'club/circle.html',{'posts':posts})

def circle_detail(request,id):
    circle_post = get_object_or_404(circle_Post, pk = id)
    return render(request,'main/circle_detail.html',{'post':circle_post})

def circle_new(request):
    return render(request,'main/circle_new.html')

def circle_create(request):
    circle_new_post = circle_Post()
    circle_new_post.title = request.POST['title']
    circle_new_post.writer = request.user
    circle_new_post.date = timezone.now()
    circle_new_post.body = request.POST['body']
    circle_new_post.image = request.FILES.get('image')
    circle_new_post.save()
    return redirect('main:circle_detail',circle_new_post.id)

def circle_edit(request,id):
    circle_edit_post = circle_Post.objects.get(id = id)
    return render(request, 'main/circle_edit.html', {'post':circle_edit_post})

def circle_update(request,id):
    circle_update_post = get_object_or_404(circle_Post, id = id)
    circle_update_post.title = request.POST['title']
    circle_update_post.writer = request.user
    circle_update_post.date = timezone.now()
    circle_update_post.body = request.POST['body']
    circle_update_post.image = request.FILES.get('image')
    circle_update_post.save()
    return redirect('main:circle_detail',circle_update_post.id)

def circle_delete(request,id):
    circle_delete_post = circle_Post.objects.get(id = id)
    circle_delete_post.delete()
    return redirect('main:circle')


#stone

def stone(request):
    posts = stone_Post.objects.all().order_by('-date')
    return render(request,'club/stone.html',{'posts':posts})

def stone_detail(request,id):
    stone_post = get_object_or_404(stone_Post, pk = id)
    return render(request,'main/stone_detail.html',{'post':stone_post})

def stone_new(request):
    return render(request,'main/stone_new.html')

def stone_create(request):
    stone_new_post = stone_Post()
    stone_new_post.title = request.POST['title']
    stone_new_post.writer = request.user
    stone_new_post.date = timezone.now()
    stone_new_post.body = request.POST['body']
    stone_new_post.image = request.FILES.get('image')
    stone_new_post.save()
    return redirect('main:stone_detail',stone_new_post.id)

def stone_edit(request,id):
    stone_edit_post = stone_Post.objects.get(id = id)
    return render(request, 'main/stone_edit.html', {'post':stone_edit_post})

def stone_update(request,id):
    stone_update_post = get_object_or_404(stone_Post, id = id)
    stone_update_post.title = request.POST['title']
    stone_update_post.writer = request.user
    stone_update_post.date = timezone.now()
    stone_update_post.body = request.POST['body']
    stone_update_post.image = request.FILES.get('image')
    stone_update_post.save()
    return redirect('main:stone_detail',stone_update_post.id)

def stone_delete(request,id):
    stone_delete_post = stone_Post.objects.get(id = id)
    stone_delete_post.delete()
    return redirect('main:stone')


#cartoon

def cartoon(request):
    posts = cartoon_Post.objects.all().order_by('-date')
    return render(request,'club/cartoon.html',{'posts':posts})

def cartoon_detail(request,id):
    cartoon_post = get_object_or_404(cartoon_Post, pk = id)
    return render(request,'main/cartoon_detail.html',{'post':cartoon_post})

def cartoon_new(request):
    return render(request,'main/cartoon_new.html')

def cartoon_create(request):
    cartoon_new_post = cartoon_Post()
    cartoon_new_post.title = request.POST['title']
    cartoon_new_post.writer = request.user
    cartoon_new_post.date = timezone.now()
    cartoon_new_post.body = request.POST['body']
    cartoon_new_post.image = request.FILES.get('image')
    cartoon_new_post.save()
    return redirect('main:cartoon_detail',cartoon_new_post.id)

def cartoon_edit(request,id):
    cartoon_edit_post = cartoon_Post.objects.get(id = id)
    return render(request, 'main/cartoon_edit.html', {'post':cartoon_edit_post})

def cartoon_update(request,id):
    cartoon_update_post = get_object_or_404(cartoon_Post, id = id)
    cartoon_update_post.title = request.POST['title']
    cartoon_update_post.writer = request.user
    cartoon_update_post.date = timezone.now()
    cartoon_update_post.body = request.POST['body']
    cartoon_update_post.image = request.FILES.get('image')
    cartoon_update_post.save()
    return redirect('main:cartoon_detail',cartoon_update_post.id)

def cartoon_delete(request,id):
    cartoon_delete_post = cartoon_Post.objects.get(id = id)
    cartoon_delete_post.delete()
    return redirect('main:cartoon')


#rush

def rush(request):
    posts = rush_Post.objects.all().order_by('-date')
    return render(request,'club/rush.html',{'posts':posts})

def rush_detail(request,id):
    rush_post = get_object_or_404(rush_Post, pk = id)
    return render(request,'main/rush_detail.html',{'post':rush_post})

def rush_new(request):
    return render(request,'main/rush_new.html')

def rush_create(request):
    rush_new_post = rush_Post()
    rush_new_post.title = request.POST['title']
    rush_new_post.writer = request.user
    rush_new_post.date = timezone.now()
    rush_new_post.body = request.POST['body']
    rush_new_post.image = request.FILES.get('image')
    rush_new_post.save()
    return redirect('main:rush_detail',rush_new_post.id)

def rush_edit(request,id):
    rush_edit_post = rush_Post.objects.get(id = id)
    return render(request, 'main/rush_edit.html', {'post':rush_edit_post})

def rush_update(request,id):
    rush_update_post = get_object_or_404(rush_Post, id = id)
    rush_update_post.title = request.POST['title']
    rush_update_post.writer = request.user
    rush_update_post.date = timezone.now()
    rush_update_post.body = request.POST['body']
    rush_update_post.image = request.FILES.get('image')
    rush_update_post.save()
    return redirect('main:rush_detail',rush_update_post.id)

def rush_delete(request,id):
    rush_delete_post = rush_Post.objects.get(id = id)
    rush_delete_post.delete()
    return redirect('main:rush')


# 신규분과
# elephente
def elephente(request):
    posts = elephente_Post.objects.all().order_by('-date')
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
    posts = doomchit_Post.objects.all().order_by('-date')
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

# likelion
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

# enactus
def enactus(request):
    posts = enactus_Post.objects.all().order_by('-date')
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
    posts = jam_Post.objects.all().order_by('-date')
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
    posts = qud_Post.objects.all().order_by('-date')
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

# 체육분과
# dust
def dust(request):
    posts = dust_Post.objects.all().order_by('-date')
    return render(request,'club/dust.html',{'posts':posts})

def dust_detail(request,id):
    dust_post = get_object_or_404(dust_Post, pk = id)
    return render(request,'main/dust_detail.html',{'post':dust_post})

def dust_new(request):
    return render(request,'main/dust_new.html')

def dust_create(request):
    dust_new_post = dust_Post()
    dust_new_post.title = request.POST['title']
    dust_new_post.writer = request.user
    dust_new_post.date = timezone.now()
    dust_new_post.body = request.POST['body']
    dust_new_post.image = request.FILES.get('image')
    dust_new_post.save()
    return redirect('main:dust_detail',dust_new_post.id)

def dust_edit(request,id):
    dust_edit_post = dust_Post.objects.get(id = id)
    return render(request, 'main/dust_edit.html', {'post':dust_edit_post})

def dust_update(request,id):
    dust_update_post = get_object_or_404(dust_Post, id = id)
    dust_update_post.title = request.POST['title']
    dust_update_post.writer = request.user
    dust_update_post.date = timezone.now()
    dust_update_post.body = request.POST['body']
    dust_update_post.image = request.FILES.get('image')
    dust_update_post.save()
    return redirect('main:dust_detail',dust_update_post.id)

def dust_delete(request,id):
    dust_delete_post = dust_Post.objects.get(id = id)
    dust_delete_post.delete()
    return redirect('main:dust')


# cave
def cave(request):
    posts = cave_Post.objects.all().order_by('-date')
    return render(request,'club/cave.html',{'posts':posts})

def cave_detail(request,id):
    cave_post = get_object_or_404(cave_Post, pk = id)
    return render(request,'main/cave_detail.html',{'post':cave_post})

def cave_new(request):
    return render(request,'main/cave_new.html')

def cave_create(request):
    cave_new_post = cave_Post()
    cave_new_post.title = request.POST['title']
    cave_new_post.writer = request.user
    cave_new_post.date = timezone.now()
    cave_new_post.body = request.POST['body']
    cave_new_post.image = request.FILES.get('image')
    cave_new_post.save()
    return redirect('main:cave_detail',cave_new_post.id)

def cave_edit(request,id):
    cave_edit_post = cave_Post.objects.get(id = id)
    return render(request, 'main/cave_edit.html', {'post':cave_edit_post})

def cave_update(request,id):
    cave_update_post = get_object_or_404(cave_Post, id = id)
    cave_update_post.title = request.POST['title']
    cave_update_post.writer = request.user
    cave_update_post.date = timezone.now()
    cave_update_post.body = request.POST['body']
    cave_update_post.image = request.FILES.get('image')
    cave_update_post.save()
    return redirect('main:cave_detail',cave_update_post.id)

def cave_delete(request,id):
    cave_delete_post = cave_Post.objects.get(id = id)
    cave_delete_post.delete()
    return redirect('main:cave')


# action
def action(request):
    posts = action_Post.objects.all().order_by('-date')
    return render(request,'club/action.html',{'posts':posts})

def action_detail(request,id):
    action_post = get_object_or_404(action_Post, pk = id)
    return render(request,'main/action_detail.html',{'post':action_post})

def action_new(request):
    return render(request,'main/action_new.html')

def action_create(request):
    action_new_post = action_Post()
    action_new_post.title = request.POST['title']
    action_new_post.writer = request.user
    action_new_post.date = timezone.now()
    action_new_post.body = request.POST['body']
    action_new_post.image = request.FILES.get('image')
    action_new_post.save()
    return redirect('main:action_detail',action_new_post.id)

def action_edit(request,id):
    action_edit_post = action_Post.objects.get(id = id)
    return render(request, 'main/action_edit.html', {'post':action_edit_post})

def action_update(request,id):
    action_update_post = get_object_or_404(action_Post, id = id)
    action_update_post.title = request.POST['title']
    action_update_post.writer = request.user
    action_update_post.date = timezone.now()
    action_update_post.body = request.POST['body']
    action_update_post.image = request.FILES.get('image')
    action_update_post.save()
    return redirect('main:action_detail',action_update_post.id)

def action_delete(request,id):
    action_delete_post = action_Post.objects.get(id = id)
    action_delete_post.delete()
    return redirect('main:action')


# wind
def wind(request):
    posts = wind_Post.objects.all().order_by('-date')
    return render(request,'club/wind.html',{'posts':posts})

def wind_detail(request,id):
    wind_post = get_object_or_404(wind_Post, pk = id)
    return render(request,'main/wind_detail.html',{'post':wind_post})

def wind_new(request):
    return render(request,'main/wind_new.html')

def wind_create(request):
    wind_new_post = wind_Post()
    wind_new_post.title = request.POST['title']
    wind_new_post.writer = request.user
    wind_new_post.date = timezone.now()
    wind_new_post.body = request.POST['body']
    wind_new_post.image = request.FILES.get('image')
    wind_new_post.save()
    return redirect('main:wind_detail',wind_new_post.id)

def wind_edit(request,id):
    wind_edit_post = wind_Post.objects.get(id = id)
    return render(request, 'main/wind_edit.html', {'post':wind_edit_post})

def wind_update(request,id):
    wind_update_post = get_object_or_404(wind_Post, id = id)
    wind_update_post.title = request.POST['title']
    wind_update_post.writer = request.user
    wind_update_post.date = timezone.now()
    wind_update_post.body = request.POST['body']
    wind_update_post.image = request.FILES.get('image')
    wind_update_post.save()
    return redirect('main:wind_detail',wind_update_post.id)

def wind_delete(request,id):
    wind_delete_post = wind_Post.objects.get(id = id)
    wind_delete_post.delete()
    return redirect('main:wind')


# mountain
def mountain(request):
    posts = mountain_Post.objects.all().order_by('-date')
    return render(request,'club/mountain.html',{'posts':posts})

def mountain_detail(request,id):
    mountain_post = get_object_or_404(mountain_Post, pk = id)
    return render(request,'main/mountain_detail.html',{'post':mountain_post})

def mountain_new(request):
    return render(request,'main/mountain_new.html')

def mountain_create(request):
    mountain_new_post = mountain_Post()
    mountain_new_post.title = request.POST['title']
    mountain_new_post.writer = request.user
    mountain_new_post.date = timezone.now()
    mountain_new_post.body = request.POST['body']
    mountain_new_post.image = request.FILES.get('image')
    mountain_new_post.save()
    return redirect('main:mountain_detail',mountain_new_post.id)

def mountain_edit(request,id):
    mountain_edit_post = mountain_Post.objects.get(id = id)
    return render(request, 'main/mountain_edit.html', {'post':mountain_edit_post})

def mountain_update(request,id):
    mountain_update_post = get_object_or_404(mountain_Post, id = id)
    mountain_update_post.title = request.POST['title']
    mountain_update_post.writer = request.user
    mountain_update_post.date = timezone.now()
    mountain_update_post.body = request.POST['body']
    mountain_update_post.image = request.FILES.get('image')
    mountain_update_post.save()
    return redirect('main:mountain_detail',mountain_update_post.id)

def mountain_delete(request,id):
    mountain_delete_post = mountain_Post.objects.get(id = id)
    mountain_delete_post.delete()
    return redirect('main:mountain')


# water
def water(request):
    posts = water_Post.objects.all().order_by('-date')
    return render(request,'club/water.html',{'posts':posts})

def water_detail(request,id):
    water_post = get_object_or_404(water_Post, pk = id)
    return render(request,'main/water_detail.html',{'post':water_post})

def water_new(request):
    return render(request,'main/water_new.html')

def water_create(request):
    water_new_post = water_Post()
    water_new_post.title = request.POST['title']
    water_new_post.writer = request.user
    water_new_post.date = timezone.now()
    water_new_post.body = request.POST['body']
    water_new_post.image = request.FILES.get('image')
    water_new_post.save()
    return redirect('main:water_detail',water_new_post.id)

def water_edit(request,id):
    water_edit_post = water_Post.objects.get(id = id)
    return render(request, 'main/water_edit.html', {'post':water_edit_post})

def water_update(request,id):
    water_update_post = get_object_or_404(water_Post, id = id)
    water_update_post.title = request.POST['title']
    water_update_post.writer = request.user
    water_update_post.date = timezone.now()
    water_update_post.body = request.POST['body']
    water_update_post.image = request.FILES.get('image')
    water_update_post.save()
    return redirect('main:water_detail',water_update_post.id)

def water_delete(request,id):
    water_delete_post = water_Post.objects.get(id = id)
    water_delete_post.delete()
    return redirect('main:water')


# courtist
def courtist(request):
    posts = courtist_Post.objects.all().order_by('-date')
    return render(request,'club/courtist.html',{'posts':posts})

def courtist_detail(request,id):
    courtist_post = get_object_or_404(courtist_Post, pk = id)
    return render(request,'main/courtist_detail.html',{'post':courtist_post})

def courtist_new(request):
    return render(request,'main/courtist_new.html')

def courtist_create(request):
    courtist_new_post = courtist_Post()
    courtist_new_post.title = request.POST['title']
    courtist_new_post.writer = request.user
    courtist_new_post.date = timezone.now()
    courtist_new_post.body = request.POST['body']
    courtist_new_post.image = request.FILES.get('image')
    courtist_new_post.save()
    return redirect('main:courtist_detail',courtist_new_post.id)

def courtist_edit(request,id):
    courtist_edit_post = courtist_Post.objects.get(id = id)
    return render(request, 'main/courtist_edit.html', {'post':courtist_edit_post})

def courtist_update(request,id):
    courtist_update_post = get_object_or_404(courtist_Post, id = id)
    courtist_update_post.title = request.POST['title']
    courtist_update_post.writer = request.user
    courtist_update_post.date = timezone.now()
    courtist_update_post.body = request.POST['body']
    courtist_update_post.image = request.FILES.get('image')
    courtist_update_post.save()
    return redirect('main:courtist_detail',courtist_update_post.id)

def courtist_delete(request,id):
    courtist_delete_post = courtist_Post.objects.get(id = id)
    courtist_delete_post.delete()
    return redirect('main:courtist')


# dutc
def dutc(request):
    posts = dutc_Post.objects.all().order_by('-date')
    return render(request,'club/dutc.html',{'posts':posts})

def dutc_detail(request,id):
    dutc_post = get_object_or_404(dutc_Post, pk = id)
    return render(request,'main/dutc_detail.html',{'post':dutc_post})

def dutc_new(request):
    return render(request,'main/dutc_new.html')

def dutc_create(request):
    dutc_new_post = dutc_Post()
    dutc_new_post.title = request.POST['title']
    dutc_new_post.writer = request.user
    dutc_new_post.date = timezone.now()
    dutc_new_post.body = request.POST['body']
    dutc_new_post.image = request.FILES.get('image')
    dutc_new_post.save()
    return redirect('main:dutc_detail',dutc_new_post.id)

def dutc_edit(request,id):
    dutc_edit_post = dutc_Post.objects.get(id = id)
    return render(request, 'main/dutc_edit.html', {'post':dutc_edit_post})

def dutc_update(request,id):
    dutc_update_post = get_object_or_404(dutc_Post, id = id)
    dutc_update_post.title = request.POST['title']
    dutc_update_post.writer = request.user
    dutc_update_post.date = timezone.now()
    dutc_update_post.body = request.POST['body']
    dutc_update_post.image = request.FILES.get('image')
    dutc_update_post.save()
    return redirect('main:dutc_detail',dutc_update_post.id)

def dutc_delete(request,id):
    dutc_delete_post = dutc_Post.objects.get(id = id)
    dutc_delete_post.delete()
    return redirect('main:dutc')


# fctoto
def fctoto(request):
    posts = fctoto_Post.objects.all().order_by('-date')
    return render(request,'club/fctoto.html',{'posts':posts})

def fctoto_detail(request,id):
    fctoto_post = get_object_or_404(fctoto_Post, pk = id)
    return render(request,'main/fctoto_detail.html',{'post':fctoto_post})

def fctoto_new(request):
    return render(request,'main/fctoto_new.html')

def fctoto_create(request):
    fctoto_new_post = fctoto_Post()
    fctoto_new_post.title = request.POST['title']
    fctoto_new_post.writer = request.user
    fctoto_new_post.date = timezone.now()
    fctoto_new_post.body = request.POST['body']
    fctoto_new_post.image = request.FILES.get('image')
    fctoto_new_post.save()
    return redirect('main:fctoto_detail',fctoto_new_post.id)

def fctoto_edit(request,id):
    fctoto_edit_post = fctoto_Post.objects.get(id = id)
    return render(request, 'main/fctoto_edit.html', {'post':fctoto_edit_post})

def fctoto_update(request,id):
    fctoto_update_post = get_object_or_404(fctoto_Post, id = id)
    fctoto_update_post.title = request.POST['title']
    fctoto_update_post.writer = request.user
    fctoto_update_post.date = timezone.now()
    fctoto_update_post.body = request.POST['body']
    fctoto_update_post.image = request.FILES.get('image')
    fctoto_update_post.save()
    return redirect('main:fctoto_detail',fctoto_update_post.id)

def fctoto_delete(request,id):
    fctoto_delete_post = fctoto_Post.objects.get(id = id)
    fctoto_delete_post.delete()
    return redirect('main:fctoto')

# lae
def lae(request):
    posts = lae_Post.objects.all().order_by('-date')
    return render(request,'club/lae.html',{'posts':posts})

def lae_detail(request,id):
    lae_post = get_object_or_404(lae_Post, pk = id)
    return render(request,'main/lae_detail.html',{'post':lae_post})

def lae_new(request):
    return render(request,'main/lae_new.html')

def lae_create(request):
    lae_new_post = lae_Post()
    lae_new_post.title = request.POST['title']
    lae_new_post.writer = request.user
    lae_new_post.date = timezone.now()
    lae_new_post.body = request.POST['body']
    lae_new_post.image = request.FILES.get('image')
    lae_new_post.save()
    return redirect('main:lae_detail',lae_new_post.id)

def lae_edit(request,id):
    lae_edit_post = lae_Post.objects.get(id = id)
    return render(request, 'main/lae_edit.html', {'post':lae_edit_post})

def lae_update(request,id):
    lae_update_post = get_object_or_404(lae_Post, id = id)
    lae_update_post.title = request.POST['title']
    lae_update_post.writer = request.user
    lae_update_post.date = timezone.now()
    lae_update_post.body = request.POST['body']
    lae_update_post.image = request.FILES.get('image')
    lae_update_post.save()
    return redirect('main:lae_detail',lae_update_post.id)

def lae_delete(request,id):
    lae_delete_post = lae_Post.objects.get(id = id)
    lae_delete_post.delete()
    return redirect('main:lae')

# kendo
def kendo(request):
    posts = kendo_Post.objects.all().order_by('-date')
    return render(request,'club/kendo.html',{'posts':posts})

def kendo_detail(request,id):
    kendo_post = get_object_or_404(kendo_Post, pk = id)
    return render(request,'main/kendo_detail.html',{'post':kendo_post})

def kendo_new(request):
    return render(request,'main/kendo_new.html')

def kendo_create(request):
    kendo_new_post = kendo_Post()
    kendo_new_post.title = request.POST['title']
    kendo_new_post.writer = request.user
    kendo_new_post.date = timezone.now()
    kendo_new_post.body = request.POST['body']
    kendo_new_post.image = request.FILES.get('image')
    kendo_new_post.save()
    return redirect('main:kendo_detail',kendo_new_post.id)

def kendo_edit(request,id):
    kendo_edit_post = kendo_Post.objects.get(id = id)
    return render(request, 'main/kendo_edit.html', {'post':kendo_edit_post})

def kendo_update(request,id):
    kendo_update_post = get_object_or_404(kendo_Post, id = id)
    kendo_update_post.title = request.POST['title']
    kendo_update_post.writer = request.user
    kendo_update_post.date = timezone.now()
    kendo_update_post.body = request.POST['body']
    kendo_update_post.image = request.FILES.get('image')
    kendo_update_post.save()
    return redirect('main:kendo_detail',kendo_update_post.id)

def kendo_delete(request,id):
    kendo_delete_post = kendo_Post.objects.get(id = id)
    kendo_delete_post.delete()
    return redirect('main:kendo')

# baduk
def baduk(request):
    posts = baduk_Post.objects.all().order_by('-date')
    return render(request,'club/baduk.html',{'posts':posts})

def baduk_detail(request,id):
    baduk_post = get_object_or_404(baduk_Post, pk = id)
    return render(request,'main/baduk_detail.html',{'post':baduk_post})

def baduk_new(request):
    return render(request,'main/baduk_new.html')

def baduk_create(request):
    baduk_new_post = baduk_Post()
    baduk_new_post.title = request.POST['title']
    baduk_new_post.writer = request.user
    baduk_new_post.date = timezone.now()
    baduk_new_post.body = request.POST['body']
    baduk_new_post.image = request.FILES.get('image')
    baduk_new_post.save()
    return redirect('main:baduk_detail',baduk_new_post.id)

def baduk_edit(request,id):
    baduk_edit_post = baduk_Post.objects.get(id = id)
    return render(request, 'main/baduk_edit.html', {'post':baduk_edit_post})

def baduk_update(request,id):
    baduk_update_post = get_object_or_404(baduk_Post, id = id)
    baduk_update_post.title = request.POST['title']
    baduk_update_post.writer = request.user
    baduk_update_post.date = timezone.now()
    baduk_update_post.body = request.POST['body']
    baduk_update_post.image = request.FILES.get('image')
    baduk_update_post.save()
    return redirect('main:baduk_detail',baduk_update_post.id)

def baduk_delete(request,id):
    baduk_delete_post = baduk_Post.objects.get(id = id)
    baduk_delete_post.delete()
    return redirect('main:baduk')

# arrow
def arrow(request):
    posts = arrow_Post.objects.all().order_by('-date')
    return render(request,'club/arrow.html',{'posts':posts})

def arrow_detail(request,id):
    arrow_post = get_object_or_404(arrow_Post, pk = id)
    return render(request,'main/arrow_detail.html',{'post':arrow_post})

def arrow_new(request):
    return render(request,'main/arrow_new.html')

def arrow_create(request):
    arrow_new_post = arrow_Post()
    arrow_new_post.title = request.POST['title']
    arrow_new_post.writer = request.user
    arrow_new_post.date = timezone.now()
    arrow_new_post.body = request.POST['body']
    arrow_new_post.image = request.FILES.get('image')
    arrow_new_post.save()
    return redirect('main:arrow_detail',arrow_new_post.id)

def arrow_edit(request,id):
    arrow_edit_post = arrow_Post.objects.get(id = id)
    return render(request, 'main/arrow_edit.html', {'post':arrow_edit_post})

def arrow_update(request,id):
    arrow_update_post = get_object_or_404(arrow_Post, id = id)
    arrow_update_post.title = request.POST['title']
    arrow_update_post.writer = request.user
    arrow_update_post.date = timezone.now()
    arrow_update_post.body = request.POST['body']
    arrow_update_post.image = request.FILES.get('image')
    arrow_update_post.save()
    return redirect('main:arrow_detail',arrow_update_post.id)

def arrow_delete(request,id):
    arrow_delete_post = arrow_Post.objects.get(id = id)
    arrow_delete_post.delete()
    return redirect('main:arrow')

# taekwondo
def taekwondo(request):
    posts = taekwondo_Post.objects.all().order_by('-date')
    return render(request,'club/taekwondo.html',{'posts':posts})

def taekwondo_detail(request,id):
    taekwondo_post = get_object_or_404(taekwondo_Post, pk = id)
    return render(request,'main/taekwondo_detail.html',{'post':taekwondo_post})

def taekwondo_new(request):
    return render(request,'main/taekwondo_new.html')

def taekwondo_create(request):
    taekwondo_new_post = taekwondo_Post()
    taekwondo_new_post.title = request.POST['title']
    taekwondo_new_post.writer = request.user
    taekwondo_new_post.date = timezone.now()
    taekwondo_new_post.body = request.POST['body']
    taekwondo_new_post.image = request.FILES.get('image')
    taekwondo_new_post.save()
    return redirect('main:taekwondo_detail',taekwondo_new_post.id)

def taekwondo_edit(request,id):
    taekwondo_edit_post = taekwondo_Post.objects.get(id = id)
    return render(request, 'main/taekwondo_edit.html', {'post':taekwondo_edit_post})

def taekwondo_update(request,id):
    taekwondo_update_post = get_object_or_404(taekwondo_Post, id = id)
    taekwondo_update_post.title = request.POST['title']
    taekwondo_update_post.writer = request.user
    taekwondo_update_post.date = timezone.now()
    taekwondo_update_post.body = request.POST['body']
    taekwondo_update_post.image = request.FILES.get('image')
    taekwondo_update_post.save()
    return redirect('main:taekwondo_detail',taekwondo_update_post.id)

def taekwondo_delete(request,id):
    taekwondo_delete_post = taekwondo_Post.objects.get(id = id)
    taekwondo_delete_post.delete()
    return redirect('main:taekwondo')

# tuskers
def tuskers(request):
    posts = tuskers_Post.objects.all().order_by('-date')
    return render(request,'club/tuskers.html',{'posts':posts})

def tuskers_detail(request,id):
    tuskers_post = get_object_or_404(tuskers_Post, pk = id)
    return render(request,'main/tuskers_detail.html',{'post':tuskers_post})

def tuskers_new(request):
    return render(request,'main/tuskers_new.html')

def tuskers_create(request):
    tuskers_new_post = tuskers_Post()
    tuskers_new_post.title = request.POST['title']
    tuskers_new_post.writer = request.user
    tuskers_new_post.date = timezone.now()
    tuskers_new_post.body = request.POST['body']
    tuskers_new_post.image = request.FILES.get('image')
    tuskers_new_post.save()
    return redirect('main:tuskers_detail',tuskers_new_post.id)

def tuskers_edit(request,id):
    tuskers_edit_post = tuskers_Post.objects.get(id = id)
    return render(request, 'main/tuskers_edit.html', {'post':tuskers_edit_post})

def tuskers_update(request,id):
    tuskers_update_post = get_object_or_404(tuskers_Post, id = id)
    tuskers_update_post.title = request.POST['title']
    tuskers_update_post.writer = request.user
    tuskers_update_post.date = timezone.now()
    tuskers_update_post.body = request.POST['body']
    tuskers_update_post.image = request.FILES.get('image')
    tuskers_update_post.save()
    return redirect('main:tuskers_detail',tuskers_update_post.id)

def tuskers_delete(request,id):
    tuskers_delete_post = tuskers_Post.objects.get(id = id)
    tuskers_delete_post.delete()
    return redirect('main:tuskers')
