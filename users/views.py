from django.shortcuts import render
from main.models import *
from django.contrib.auth.models import User
# Create your views here.

# 학술분과    
def cafein_mypage(request):
    user = request.user
    cafein_posts = cafein_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'cafein_posts':cafein_posts})

def dna_mypage(request):
    user = request.user
    dna_posts = dna_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'dna_posts':dna_posts})

def dussa_mypage(request):
    user = request.user
    posts = dussa_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def kcc_mypage(request):
    user = request.user
    posts = kcc_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def mecs_mypage(request):
    user = request.user
    posts = mecs_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def nsa_mypage(request):
    user = request.user
    posts = nsa_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def marx_mypage(request):
    user = request.user
    posts = marx_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

# 연구분과
def management_mypage(request):
    user = request.user
    posts = management_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def economy_mypage(request):
    user = request.user
    posts = economy_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def international_mypage(request):
    user = request.user
    posts = international_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def politics_mypage(request):
    user = request.user
    posts = politics_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

# 봉사분과
def elf_mypage(request):
    user = request.user
    posts = elf_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def rcy_mypage(request):
    user = request.user
    posts = rcy_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def road_mypage(request):
    user = request.user
    posts = road_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def hand_mypage(request):
    user = request.user
    posts = hand_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def neighbor_mypage(request):
    user = request.user
    posts = neighbor_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def painters_mypage(request):
    user = request.user
    posts = painters_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def green_mypage(request):
    user = request.user
    posts = green_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def korean_mypage(request):
    user = request.user
    posts = korean_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

# 사회분과
def kusa_mypage(request):
    user = request.user
    posts = kusa_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def rich_mypage(request):
    user = request.user
    posts = rich_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def unsa_mypage(request):
    user = request.user
    posts = unsa_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def frontier_mypage(request):
    user = request.user
    posts = frontier_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def buddha_mypage(request):
    user = request.user
    posts = buddha_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

# 체육분과
def dust_mypage(request):
    user = request.user
    posts = dust_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def cave_mypage(request):
    user = request.user
    posts = cave_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def action_mypage(request):
    user = request.user
    posts = action_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def wind_mypage(request):
    user = request.user
    posts = wind_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def mountain_mypage(request):
    user = request.user
    posts = mountain_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def water_mypage(request):
    user = request.user
    posts = water_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def courtist_mypage(request):
    user = request.user
    posts = courtist_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def dutc_mypage(request):
    user = request.user
    posts = dutc_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def fctoto_mypage(request):
    user = request.user
    posts = fctoto_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def lae_mypage(request):
    user = request.user
    posts = lae_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def kendo_mypage(request):
    user = request.user
    posts = kendo_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def baduk_mypage(request):
    user = request.user
    posts = baduk_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def arrow_mypage(request):
    user = request.user
    posts = arrow_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def taekwondo_mypage(request):
    user = request.user
    posts = taekwondo_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def tuskers_mypage(request):
    user = request.user
    posts = tuskers_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

# 공연분과
def ajax_mypage(request):
    user = request.user
    posts = ajax_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def hola_mypage(request):
    user = request.user
    posts = hola_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def odc_mypage(request):
    user = request.user
    posts = odc_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def opus_mypage(request):
    user = request.user
    posts = opus_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def drama_mypage(request):
    user = request.user
    posts = drama_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def lotus_mypage(request):
    user = request.user
    posts = lotus_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def cloud_mypage(request):
    user = request.user
    posts = cloud_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def arirang_mypage(request):
    user = request.user
    posts = arirang_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def eumsem_mypage(request):
    user = request.user
    posts = eumsem_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def fearless_mypage(request):
    user = request.user
    posts = fearless_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def yeoul_mypage(request):
    user = request.user
    posts = yeoul_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

# 예창분과
def draw_mypage(request):
    user = request.user
    posts = draw_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def literal_mypage(request):
    user = request.user
    posts = literal_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def calligraphy_mypage(request):
    user = request.user
    posts = calligraphy_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def circle_mypage(request):
    user = request.user
    posts = circle_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def stone_mypage(request):
    user = request.user
    posts = stone_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def cartoon_mypage(request):
    user = request.user
    posts = cartoon_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def rush_mypage(request):
    user = request.user
    posts = rush_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

# 신규분과
def elephente_mypage(request):
    user = request.user
    posts = elephente_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def doomchit_mypage(request):
    user = request.user
    posts = doomchit_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def likelion_mypage(request):
    user = request.user
    posts = likelion_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def enactus_mypage(request):
    user = request.user
    posts = enactus_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def jam_mypage(request):
    user = request.user
    posts = jam_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def qud_mypage(request):
    user = request.user
    posts = qud_Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})