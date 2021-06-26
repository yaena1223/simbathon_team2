from django.shortcuts import render
from main.models import *
from django.contrib.auth.models import User
# Create your views here.

def all_mypage(request):
    user = request.user
    cafein_posts = cafein_Post.objects.filter(writer=user).order_by('-date')
    dna_posts = dna_Post.objects.filter(writer=user).order_by('-date')
    dussa_posts = dussa_Post.objects.filter(writer=user).order_by('-date')
    kcc_posts = kcc_Post.objects.filter(writer=user).order_by('-date')
    mecs_posts = mecs_Post.objects.filter(writer=user).order_by('-date')
    nsa_posts = nsa_Post.objects.filter(writer=user).order_by('-date')

    marx_posts = marx_Post.objects.filter(writer=user).order_by('-date')
    
    management_posts = management_Post.objects.filter(writer=user).order_by('-date')
    
    economy_posts = economy_Post.objects.filter(writer=user).order_by('-date')
    
    international_posts = international_Post.objects.filter(writer=user).order_by('-date')
    
    politics_posts = politics_Post.objects.filter(writer=user).order_by('-date')
    
    elf_posts = elf_Post.objects.filter(writer=user).order_by('-date')
    
    rcy_posts = rcy_Post.objects.filter(writer=user).order_by('-date')
    
    road_posts = road_Post.objects.filter(writer=user).order_by('-date')
    
    hand_posts = hand_Post.objects.filter(writer=user).order_by('-date')
    
    neighbor_posts = neighbor_Post.objects.filter(writer=user).order_by('-date')
    
    painters_posts = painters_Post.objects.filter(writer=user).order_by('-date')
    
    green_posts = green_Post.objects.filter(writer=user).order_by('-date')
    
    korean_posts = korean_Post.objects.filter(writer=user).order_by('-date')
    
    kusa_posts = kusa_Post.objects.filter(writer=user).order_by('-date')
    
    rich_posts = rich_Post.objects.filter(writer=user).order_by('-date')
    
    unsa_posts = unsa_Post.objects.filter(writer=user).order_by('-date')
    
    frontier_posts = frontier_Post.objects.filter(writer=user).order_by('-date')
    
    buddha_posts = buddha_Post.objects.filter(writer=user).order_by('-date')
    
    dust_posts = dust_Post.objects.filter(writer=user).order_by('-date')
    
    cave_posts = cave_Post.objects.filter(writer=user).order_by('-date')
    
    action_posts = action_Post.objects.filter(writer=user).order_by('-date')
    
    wind_posts = wind_Post.objects.filter(writer=user).order_by('-date')
    
    mountain_posts = mountain_Post.objects.filter(writer=user).order_by('-date')
    
    water_posts = water_Post.objects.filter(writer=user).order_by('-date')
    
    courtist_posts = courtist_Post.objects.filter(writer=user).order_by('-date')
    
    dutc_posts = dutc_Post.objects.filter(writer=user).order_by('-date')
    
    fctoto_posts = fctoto_Post.objects.filter(writer=user).order_by('-date')
    
    lae_posts = lae_Post.objects.filter(writer=user).order_by('-date')
    
    kendo_posts = kendo_Post.objects.filter(writer=user).order_by('-date')
    
    baduk_posts = baduk_Post.objects.filter(writer=user).order_by('-date')
    
    arrow_posts = arrow_Post.objects.filter(writer=user).order_by('-date')
    
    taekwondo_posts = taekwondo_Post.objects.filter(writer=user).order_by('-date')
    
    tuskers_posts = tuskers_Post.objects.filter(writer=user).order_by('-date')
    
    ajax_posts = ajax_Post.objects.filter(writer=user).order_by('-date')
    hola_posts = hola_Post.objects.filter(writer=user).order_by('-date')
    odc_posts = odc_Post.objects.filter(writer=user).order_by('-date')
    opus_posts = opus_Post.objects.filter(writer=user).order_by('-date')
    drama_posts = drama_Post.objects.filter(writer=user).order_by('-date')
    lotus_posts = lotus_Post.objects.filter(writer=user).order_by('-date')
    cloud_posts = cloud_Post.objects.filter(writer=user).order_by('-date')
    arirang_posts = arirang_Post.objects.filter(writer=user).order_by('-date')
    eumsem_posts = eumsem_Post.objects.filter(writer=user).order_by('-date')
    fearless_posts = fearless_Post.objects.filter(writer=user).order_by('-date')
    yeoul_posts = yeoul_Post.objects.filter(writer=user).order_by('-date')
    draw_posts = draw_Post.objects.filter(writer=user).order_by('-date')
    literal_posts = literal_Post.objects.filter(writer=user).order_by('-date')
    calligraphy_posts = calligraphy_Post.objects.filter(writer=user).order_by('-date')
    circle_posts = circle_Post.objects.filter(writer=user).order_by('-date')
    stone_posts = stone_Post.objects.filter(writer=user).order_by('-date')
    cartoon_posts = cartoon_Post.objects.filter(writer=user).order_by('-date')
    rush_posts = rush_Post.objects.filter(writer=user).order_by('-date')
    elephente_posts = elephente_Post.objects.filter(writer=user).order_by('-date')
    doomchit_posts = doomchit_Post.objects.filter(writer=user).order_by('-date')
    likelion_posts = likelion_Post.objects.filter(writer=user).order_by('-date')
    enactus_posts = enactus_Post.objects.filter(writer=user).order_by('-date')
    jam_posts = jam_Post.objects.filter(writer=user).order_by('-date')
    qud_posts = qud_Post.objects.filter(writer=user).order_by('-date')

    return render(request,'users/mypage.html',{'cafein_posts':cafein_posts, 'dna_posts':dna_posts, 'dussa_posts': dussa_posts, 'kcc_posts':kcc_posts,'mecs_posts':mecs_posts,'nsa_posts':nsa_posts,'marx_posts':marx_posts,'management_posts':management_posts,'economy_posts':economy_posts,'international_posts':international_posts,'politics_posts':politics_posts,'elf_posts':elf_posts,'rcy_posts':rcy_posts,'road_posts':road_posts,'hand_posts':hand_posts,'neighbor_posts':neighbor_posts,'painters_posts':painters_posts,'green_posts':green_posts,'korean_posts':korean_posts,'kusa_posts':kusa_posts,'rich_posts':rich_posts,'unsa_posts':unsa_posts,'frontier_posts':frontier_posts,'buddha_posts':buddha_posts,'dust_posts':dust_posts,'cave_posts':cave_posts,'action_posts':action_posts,'wind_posts':wind_posts,'mountain_posts':mountain_posts,'water_posts':water_posts,'courtist_posts':courtist_posts,'dutc_posts':dutc_posts,'fctoto_posts':fctoto_posts,'lae_posts':lae_posts,'kendo_posts':kendo_posts,'baduk_posts':baduk_posts,'arrow_posts':arrow_posts,'taekwondo_posts':taekwondo_posts,'tuskers_posts':tuskers_posts,'ajax_posts':ajax_posts,'hola_posts':hola_posts,'yeoul_posts':yeoul_posts,'fearless_posts':fearless_posts,'eumsem_posts':eumsem_posts,'arirang_posts':arirang_posts,'cloud_posts':cloud_posts,'lotus_posts':lotus_posts,'drama_posts':drama_posts,'opus_posts':opus_posts,'odc_posts':odc_posts,'qud_posts':qud_posts,'jam_posts':cafein_posts,'enactus_posts':enactus_posts,'doomchit_posts':doomchit_posts,'fcelephente_posts':elephente_posts,'draw_posts':draw_posts,'calligraphy_posts':calligraphy_posts,'rush_posts':rush_posts,'cartoon_posts':cartoon_posts,'stone_posts':stone_posts,'circle_posts':circle_posts,'literal_posts':literal_posts,'likelion_posts':likelion_posts})