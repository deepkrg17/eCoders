from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return "Message from " + self.name


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=30)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateField(auto_now_add=True)
    content=models.TextField()

    def __str__(self):
        return self.title[:20] + " by " + self.author.split(' ')[0]