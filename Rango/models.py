# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localdate

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField( unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.views <= 0:
            self.views = 0
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    last_visit = models.DateField(default=localdate())
    first_visit = models.DateField(default=localdate())

    def save(self, *args, **kwargs):

        if localdate() < self.first_visit:
            self.first_visit = localdate()

        if localdate() < self.last_visit:
            self.last_visit = localdate()

        if self.last_visit < self.first_visit:
            self.first_visit = self.last_visit
        super(Page, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

