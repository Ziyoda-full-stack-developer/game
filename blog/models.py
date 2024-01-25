from django.db import models

# Create your models here.

class Header(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='header/')
    def __str__(self):
        return self.name

class Footer(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='footer/')
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    numbers = models.IntegerField()
    massage = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='list/')

    def __str__(self):
        return self.name

class You(models.Model):
    name = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    image = models.ImageField(upload_to='you/')

    def __str__(self):
        return self.name

class Pric(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pric/')
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Text(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='text/')
    bio = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    img = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name

class Gamepad(models.Model):
    name = models.CharField(max_length=200)
    bio  = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gamepad/')

    def __str__(self):
        return self.name

class Uchdi(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uchdi/')

    def __str__(self):
        return self.name

class Face(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='face/')

class Feature(models.Model):
    name = models.CharField(max_length=400)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='feature/')
    status = models.CharField(max_length=300)
    slug = models.SlugField(max_length=400)
    def __str__(self):
        return self.name