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