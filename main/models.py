from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 멋사
class likelion_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# cafein
class cafein_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# ajax
class ajax_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# hola
class hola_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# odc
class odc_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# opus
class opus_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# drama
class drama_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# lotus
class lotus_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# cloud
class cloud_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# arirang
class arirang_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# eumsem
class eumsem_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# fearless
class fearless_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# yeoul
class yeoul_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# management
class management_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# economy
class economy_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# international
class international_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# politics
class politics_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# dna
class dna_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# dussa
class dussa_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# kcc
class kcc_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# mecs
class mecs_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# nsa
class nsa_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# marx
class marx_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# kusa
class kusa_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# rich
class rich_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# unsa
class unsa_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# frontier
class frontier_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# buddha
class buddha_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# elephente
class elephente_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# doomchit
class doomchit_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# enactus
class enactus_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# jam
class jam_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# qud
class qud_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# elf
class elf_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# rcy
class rcy_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# road
class road_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# hand
class hand_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# neighbor
class neighbor_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# painters
class painters_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# green
class green_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# korean
class korean_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]
# draw
class draw_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# literal
class literal_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# calligraphy
class calligraphy_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# circle
class circle_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# stone
class stone_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# cartoon
class cartoon_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# rush
class rush_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# dust
class dust_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# cave
class cave_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# action
class action_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# wind
class wind_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# mountatin
class mountain_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# water
class water_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# courtist
class courtist_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# dutc
class dutc_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# fctoto
class fctoto_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# lae
class lae_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]


# kendo
class kendo_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# baduk
class baduk_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# arrow
class arrow_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# taekwondo
class taekwondo_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

# tuskers
class tuskers_Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='post/',blank = True, null = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]
