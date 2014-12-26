# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime
import time

class Community(models.Model):
    name = models.CharField(max_length=255, blank=True , null=True)
    left = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    link = models.CharField(max_length=1024, blank=True , null=True)
    pic_url = models.CharField(max_length=1024, blank=True , null=True)


class Building(models.Model):
    community = models.ForeignKey(Community)
    name = models.CharField(max_length=255, blank=True , null=True)
    left = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    pic_url = models.CharField(max_length=1024, blank=True , null=True)

    @property
    def houses(self):
        return self.house_set.order_by("-name")


class House(models.Model):
    building = models.ForeignKey(Building)
    name = models.CharField(max_length=255, blank=True , null=True)
    price = models.CharField(max_length=255, blank=True , null=True)
    description = models.CharField(max_length=1024, blank=True , null=True)
    is_sell = models.BooleanField(default=True)
    left = models.IntegerField(default=0)
    top = models.IntegerField(default=0)

    @property
    def show_status(self):
        if self.is_sell:
            return u"出售"
        else:
            return u"出租"

    @property
    def pics(self):
        return self.pic_set.order_by("id")


class Pic(models.Model):
    house = models.ForeignKey(House)
    url = models.CharField(max_length=1024, blank=True , null=True)




class Info(models.Model):
    category = models.CharField(max_length=255, blank=True , null=True)     # zxcj xqxxs bmfw wtczcs
    title = models.CharField(max_length=255, blank=True , null=True)
    content = models.CharField(max_length=2048, blank=True , null=True)
    pic_url = models.CharField(max_length=1024, blank=True , null=True)
    link = models.CharField(max_length=1024, blank=True , null=True)




