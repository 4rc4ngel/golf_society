from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

# Players Model

class Players(models.Model):
  name = models.ForeignKey('auth.User')
  nickname = models.CharField(max_length=30, blank=True, null=True)
  handicap = models.IntegerField(max_length=2)
  current.score = models.IntegerField(max_length=2)
  total_score = models.IntegerField(max_length=4)
  nearest_pin = models.IntegerField(max_length=2)
  birdies = models.IntegerField(max_length=2)
  eagles = models.IntegerField(max_length=2)

  def __str__(self):
    return self.name

# Blog Post Model

class Post(models.Model):
  author = models.CharField('golf_app.Players', related_name='author')
  title = models.CharField(max_length=200)
  text =  models.TextField()
  date_created = models.DateTimeField(default=timezone.now)
  date_published = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.date_published = timezone.now()
    self.save()

  def approve_comments(self):
    return self.comments.filter(approve_comments=True)

  def get_absolute_url(self):
    return reverse('post_detail',kwargs={'pk':self.pk})

  def __str__(self):
    return self.title

# Blog comments model

class Comment(models.Model):
  post = models.ForeignKey('golf_app.Post', related_name='comments')
  author = models.CharField(max_length=200)
  text = models.TextField()
  date_created = models.DateTimeField(default=timezone.now())
  approved_comment = models.BooleanField(default=False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def get_absolute_url(self):
    return reverse('post_list')

    def __str__(self):
      return self.text

