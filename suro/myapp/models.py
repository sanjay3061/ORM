from django.db import models
from django.contrib import admin
class Football_Player(models.Model):
    jessi_no=models.CharField(max_length=20,help_text="JESSI NO")
    name=models.CharField(max_length=100)
    Team =models.CharField(max_length=100)
    age=models.IntegerField()
    Matches=models.IntegerField()
class Football_PlayerAdmin(admin.ModelAdmin):
    list_display=('jessi_no','name','Team','age','Matches')
