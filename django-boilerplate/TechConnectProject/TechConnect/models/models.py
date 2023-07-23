from django.db import models
import uuid

class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_of_chapter = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_date = models.DateField()
    event_poster = models.CharField(max_length=255)
    event_description = models.TextField()

    def __str__(self):
        return self.name_of_chapter

    class Meta:
        db_table = 'createChapter'

class Opportunity(models.Model):
    title = models.CharField(max_length=100)
    key_details = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'opportunity'


class BlogSubmission(models.Model):
    name = models.CharField(max_length=100)
    year_of_education = models.CharField(max_length=50)
    blog_title = models.CharField(max_length=200)
    blog_material = models.TextField()

    def __str__(self):
        return self.blog_title
    
    class Meta:
        db_table = 'submitBlog'

class BlogPublication(models.Model):
    name = models.CharField(max_length=100)
    year_of_education = models.CharField(max_length=50)
    blog_title = models.CharField(max_length=200)
    blog_material = models.TextField()

    def __str__(self):
        return self.blog_title
    
    class Meta:
        db_table = 'publishBlog'

