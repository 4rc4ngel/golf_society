from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

# Players Model

class Player(models.Model):
  name = models.ForeignKey('auth.User')
  nickname = models.CharField(max_length=30, blank=True, null=True)
  handicap = models.IntegerField()
  current_score = models.IntegerField()
  total_score = models.IntegerField()
  nearest_pin = models.IntegerField()
  birdies = models.IntegerField()
  eagles = models.IntegerField()

  def __str__(self):
    return self.name

# Blog Post Model

class Post(models.Model):
  author = models.CharField('golf_app.Player',max_length=200)
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

