from django.db import models

# Create your models here.



class Article(models.Model) :

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "{} {}".format(self.title,self.author)

    