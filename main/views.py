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
def management(request):
    posts = Post.objects.all()
    return render(request,'club/경영학연구회.html',{'posts':posts})

def economy(request):
    posts = Post.objects.all()
    return render(request,'club/경제학연구회.html',{'posts':posts})


def international(request):
    posts = Post.objects.all()
    return render(request,'club/국제통상학연구회.html',{'posts':posts})

def politics(request):
    posts = Post.objects.all()
    return render(request,'club/정치학연구회.html',{'posts':posts})

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
    posts = Post.objects.all()
    return render(request,'club/ajax.html',{'posts':posts})

def hola(request):
    posts = Post.objects.all()
    return render(request,'club/hola.html',{'posts':posts})

def odc(request):
    posts = Post.objects.all()
    return render(request,'club/odc.html',{'posts':posts})

def opus(request):
    posts = Post.objects.all()
    return render(request,'club/opus.html',{'posts':posts})

def drama(request):
    posts = Post.objects.all()
    return render(request,'club/극예술연구회.html',{'posts':posts})

def lotus(request):
    posts = Post.objects.all()
    return render(request,'club/로터스.html',{'posts':posts})

def cloud(request):
    posts = Post.objects.all()
    return render(request,'club/뭉게구름.html',{'posts':posts})

def arirang(request):
    posts = Post.objects.all()
    return render(request,'club/아리랑.html',{'posts':posts})

def eumsem(request):
    posts = Post.objects.all()
    return render(request,'club/음샘.html',{'posts':posts})

def fearless(request):
    posts = Post.objects.all()
    return render(request,'club/피어리스던.html',{'posts':posts})

def yeoul(request):
    posts = Post.objects.all()
    return render(request,'club/현여울.html',{'posts':posts})

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

