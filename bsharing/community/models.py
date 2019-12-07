from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from enum import Enum
import datetime


# Create your models here.

class community_header(models.Model):
    user_name = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    semantic_tag = models.CharField(max_length = 150)
    published_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)

    def get_absolute_url(self):
        return reverse('community:community_detail', kwargs={"pk" : self.pk})

    def __str__(self):
        return self.name + "--" + self.desc


class DataFieldTypes(Enum):
    Text = "Text"
    BOOL = "Boolean"
    IMG = "Image"
    Audio = "Audio"
    EM = "E-mail"
    Video = "Video"
    Date = "Date"
    Int = "Number"

class define_post_types(models.Model):
    
    post_type = models.ForeignKey(community_header, default="", on_delete=models.CASCADE)
    label_name = models.CharField(max_length=100)
    label_structure = models.CharField(max_length = 10, choices=[(tag.name, tag.value) for tag in DataFieldTypes])
    label_isrequired = models.BooleanField(default=False)

    def __str__(self):
      return self.label_name #+ '-' + self.label_structure + '-' + self.label_isrequired


class post_type_header(models.Model):
    post_community = models.ForeignKey(community_header, default="", on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    semantic_tag = models.CharField(max_length = 150)
    fields = JSONField(default = "")
    #fields_type = JSONField(default = "")

    def get_absolute_url(self):
        return reverse('community:community_detail', kwargs= {"pk" : self.pk})

    def __str__(self):
        return self.name + "--" + self.desc




   
