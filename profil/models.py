from django.db import models

class About(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=200)
    date_birth = models.DateField()
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=7)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def _str_(self):
        return self.name

class Resume(models.Model):
    start_years = models.CharField(max_length=4)
    end_years = models.CharField(max_length=4)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    experience = models.TextField()

    def _str_(self):
        return self.university

class Service(models.Model):
    css_icon = models.CharField(max_length=50)
    link = models.TextField()
    title = models.CharField(max_length=30)

    def _str_(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    progress = models.IntegerField()

    def _str_(self):
        return self.name

class Blog(models.Model):
    image = models.ImageField(upload_to='')
    publish_date = models.DateField()
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def _str_(self):
        return self.title

class Contact(models.Model):
    css_icon = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)

    def _str_(self):
        return self.title
