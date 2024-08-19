from django.db import models
from django.db.models.signals import pre_delete
import os.path
from django.dispatch import receiver


class Article(models.Model):
    titre = models.CharField(max_length=400)
    date = models.DateField(auto_now_add=True)
    contenu = models.TextField()
    image1 = models.ImageField(upload_to='images/', null=True, blank= True)
    image2 = models.ImageField(upload_to='images/', null=True, blank= True)
    image3 = models.ImageField(upload_to='images/', null=True, blank= True)
    auteur = models.CharField(max_length=200)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.titre


@receiver(pre_delete, sender=Article)
def delete_image(sender, instance, **Kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)