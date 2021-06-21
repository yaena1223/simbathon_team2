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




def dna(request):
    posts = Post.objects.all()
    return render(request,'club/dna.html',{'posts':posts})

def dussa(request):
    posts = Post.objects.all()
    return render(request,'club/dussa.html',{'posts':posts})

def kcc(request):
    posts = Post.objects.all()
    return render(request,'club/kcc.html',{'posts':posts})

def mecs(request):
    posts = Post.objects.all()
    return render(request,'club/mecs.html',{'posts':posts})

def nsa(request):
    posts = Post.objects.all()
    return render(request,'club/nsa.html',{'posts':posts})


def marx(request):
    posts = Post.objects.all()
    return render(request,'club/맑스철학연구회.html',{'posts':posts})

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
def kusa(request):
    posts = Post.objects.all()
    return render(request,'club/kusa.html',{'posts':posts})

def rich(request):
    posts = Post.objects.all()
    return render(request,'club/rich.html',{'posts':posts})

def unsa(request):
    posts = Post.objects.all()
    return render(request,'club/unsa.html',{'posts':posts})

def frontier(request):
    posts = Post.objects.all()
    return render(request,'club/프론티어.html',{'posts':posts})

def buddha(request):
    posts = Post.objects.all()
    return render(request,'club/동국불교학생회.html',{'posts':posts})

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
def elephente(request):
    posts = Post.objects.all()
    return render(request,'club/fc엘레펜테.html',{'posts':posts})

def doomchit(request):
    posts = Post.objects.all()
    return render(request,'club/두둠칫.html',{'posts':posts})

def enactus(request):
    posts = Post.objects.all()
    return render(request,'club/인액터스.html',{'posts':posts})

def jam(request):
    posts = Post.objects.all()
    return render(request,'club/잼잼.html',{'posts':posts})

def qud(request):
    posts = Post.objects.all()
    return render(request,'club/qud.html',{'posts':posts})

