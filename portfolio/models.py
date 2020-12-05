from django.db import models
import datetime


ActivityGenre ={('info','Research'),('secondary','Product'),('light','Others')}

# Create your models here.
class BlogModel(models.Model):
    #タイトル
    title = models.CharField(max_length=100)
    #本文
    content = models.TextField()
    #画像
    images=models.ImageField(null=True,upload_to='images/')
    #日付
    date = models.DateField(null=False,default=datetime.date.today)
    def __str__(self):
        return self.title
        
class ActivityModel(models.Model):
    #タイトル
    title = models.CharField(max_length=100)
    #本文
    content = models.TextField()
    #画像
    images=models.ImageField(upload_to='images/')
    #リンク
    link = models.URLField(blank=True)
    #研究か
    genre = models.CharField(
    max_length=50,
    #choicesでタプル型の選択肢を作れる
    choices = ActivityGenre,
    default="Product"
    )
    
    def __str__(self):
        return self.title