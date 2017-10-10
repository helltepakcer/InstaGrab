from django.db import models


# Create your models here.
class Instagraminfo(models.Model):
    id = models.TextField(primary_key=True)
    image_ins = models.TextField()
    tag_ins = models.TextField()

    def __str__(self):
        return str(self.id) + "_" + str(self.tag_ins)





