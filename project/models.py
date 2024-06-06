from django.db import models
import uuid
# Create your models here.
class kelvin(models.Model):
     title=models.CharField(max_length=200,null=True,blank=True)
     image=models.ImageField(null=True,blank=True,default="default_image.jpg")
     description=models.TextField(null=True,blank=True)
     demo_link=models.CharField(max_length=2000,null=True,blank=True)
     source_link=models.CharField(max_length=2000,null=True,blank=True)
     Tags=models.ManyToManyField('Tag',blank=True)
     Vote_total=models.IntegerField(default=0,null=True,blank=True)
     Vote_ratio=models.IntegerField(default=0,null=True,blank=True)
     created=models.DateTimeField(auto_now_add=True)
     id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
     
     def __str__(self):
          return self.title
     
class Review(models.Model):
          Vote_Type=(
               ('up','up vote'),
               ('down','down vote')
          )
          project=models.ForeignKey(kelvin,on_delete=models.CASCADE)
          user=models.TextField(null=True,blank=True)
          value=models.CharField(max_length=200,choices=Vote_Type)
          created=models.DateTimeField(auto_now_add=True)
          id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
          
          def __str__(self):
               return self.value
     
          
class Tag(models.Model):
     name=models.CharField(max_length=300)
     created=models.DateTimeField(auto_now_add=True)
     id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
     
     def __str__(self):
         return self.name
