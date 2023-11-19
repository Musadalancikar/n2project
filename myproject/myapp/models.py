from django.db import models

# Create your models here.

class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=255)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        db_table = 'my_custom_user_table'


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

class Albums(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)

class Photos(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=255)
    url = models.URLField()
    thumbnailUrl = models.URLField()

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
