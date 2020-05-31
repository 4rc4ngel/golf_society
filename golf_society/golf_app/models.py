from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

# Players Model

class Player(models.Model):
  name = models.ForeignKey('auth.User')
  full_name = models.CharField(max_length=200)
  nickname = models.CharField(max_length=30, blank=True, null=True)
  handicap = models.IntegerField()
  current_score = models.IntegerField()
  total_score = models.IntegerField()
  nearest_pin = models.IntegerField()
  birdies = models.IntegerField()
  eagles = models.IntegerField()

  def save_player(self):
    self.save()

  def get_absolute_url(self):
    return reverse('player_list')

  def __str__(self):
    return self.nickname

# Blog Post Model

class Post(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text =  models.TextField()
  date_created = models.DateTimeField(default=timezone.now)
  date_published = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.date_published = timezone.now()
    self.save()

  def approve_comments(self):
    return self.comments.filter(approved_comment=True)

  def get_absolute_url(self):
    return reverse('post_detail',kwargs={'pk':self.pk})

  def __str__(self):
    return self.title

# Blog comments model

class Comment(models.Model):
  post = models.ForeignKey('Post', related_name='comments')
  author = models.CharField(max_length=200)
  text = models.TextField()
  date_created = models.DateTimeField(default=timezone.now)
  approved_comment = models.BooleanField(default=False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def get_absolute_url(self):
    return reverse('post_list')

    def __str__(self):
      return self.text

