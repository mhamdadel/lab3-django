from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('funny', 'Funny'),
        ('science_fiction', 'Science Fiction'),
    ]
    
    name = models.CharField(max_length=255 , null=True , blank = True)
    desc = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)
    pageNumbers = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    iscompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_desc(self):
        return self.desc[:50]