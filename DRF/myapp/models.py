from django.db import models

# Create your models here.

class Music(models.Model):
    class Meta:
        db_table = 'music'

    title = models.CharField(max_length=50)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title
