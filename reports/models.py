from django.db import models

class Assignments(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    good_type = models.CharField(
        max_length=2,
        choices=[
            ('A',"Excellent"),
            ('A-',"Outstanding"),
            ('B+',"Very good"),
            ('B',"Good"),
            ('C',"Fair"),
            ('F',"Fail"),
        ]
    )
    Grade = models.IntegerField()
    Comments = models.TextField()