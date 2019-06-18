from django.db import models
from django.utils import timezone

class User(models.Model):
    slug = models.SlugField(max_length=255, unique=True,)
    name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255, blank=True, null=True,)
    password = models.CharField(max_length=255,)
    bio = models.TextField(blank=True, null=True,)
    create_date = models.DateTimeField(default=timezone.now,)
    update_date = models.DateTimeField(auto_now=True,)
    icon = models.ImageField(blank=True, null=True, upload_to='icon')
    del_flg = models.BooleanField(default=False,)

    def __str__(self):
        return self.slug + "(" + str(self.pk) + ")"

class Comment(models.Model):
    SCORE = ((0, '最悪'), (1, 'ひどい'), (2, 'あまり良くない'), (3, '普通'), (4, '良い'), (5, '非常に良い'))
    user = models.ForeignKey('User', on_delete=models.CASCADE,)
    lavatory_id = models.IntegerField()
    total_score = models.FloatField(blank=True, null=True, choices=SCORE,)
    beautiful_score = models.IntegerField(blank=True, null=True, choices=SCORE,)
    access_score = models.IntegerField(blank=True, null=True, choices=SCORE,)
    abilability_score = models.IntegerField(blank=True, null=True, choices=SCORE,)
    message = models.TextField(blank=True, null=True,)
    create_date = models.DateTimeField(default=timezone.now,)
    update_date = models.DateTimeField(auto_now=True,)
    del_flg = models.BooleanField(default=False,)

    def __str__(self):
        return self.user.name + "… (" + self.lavatory_id + ": " + str(self.total_score) + ")"



