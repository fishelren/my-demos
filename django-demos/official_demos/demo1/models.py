from django.db import models

# Create your models here.

class Reporter(models.Model):
    full_name=models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date=models.DateField()
    headLine=models.CharField(max_length=200)
    content=models.TextField()
    Reporter=models.ForeignKey("Reporter",on_delete=models.CASCADE)

    def __str__(self):
        return self.headLine