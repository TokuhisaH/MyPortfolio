from django.db import models

# Create your models here.
class BlogModel(models.Model):
    #タイトル
    title = models.CharField(max_length=100)
    #本文
    content = models.TextField()
    #画像
<<<<<<< HEAD
    images=models.ImageField(upload_to='images/')
=======
    images=models.ImageField(null=True,upload_to='')
>>>>>>> origin/master
    #日付
    date = models.DateField()
    def __str__(self):
        return self.title