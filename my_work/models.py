from io import BytesIO
import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.urls import reverse
from tinymce.models import HTMLField


def upload_to_original(instance, filename):
    return f'projects/images/original/{filename}'

def upload_to_thumbnail(size):
    return f'projects/images/thumb_{size}/'


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="nom", max_length=50)

    class Meta:
        verbose_name="catégorie de projet"

    def __str__(self) -> str:
        return self.name
    


class Project(models.Model):
    name = models.CharField(verbose_name="nom", max_length=150)
    url = models.URLField(blank=True)
    created = models.CharField(verbose_name="créé en", max_length=4, blank=True, help_text="année de création")
    image = models.ImageField(upload_to=upload_to_original, default="", help_text="Ex : 1905x1177. Soit largeur divisé par 1.618")
    desc = HTMLField(verbose_name="description", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    thumb_2048 = models.ImageField(blank=True)
    thumb_1024 = models.ImageField(blank=True)
    thumb_512 = models.ImageField(blank=True)
    thumb_256 = models.ImageField(blank=True)

    class Meta:
        verbose_name="projet"

    
    """Renvoie l'URL permettant d'accéder à une instance particulière de film."""
    def get_absolute_url(self):
        return reverse("portfolio-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return self.name
    

@receiver(post_save, sender=Project)
def create_thumbnails(sender, instance, **kwargs):
    if kwargs.get('created', False):
        image = Image.open(instance.image.path)
        
        sizes = [2048, 1024, 512, 256]

        for size in sizes:
            if image.width >= size or image.height >= size:
                thumb = image.copy()
                thumb.thumbnail((size, size))

                field_name = f'thumb_{size}'
                filename = f'projects/images/thumb_{size}/{instance.image.name.split("/")[-1]}'  # chemin relatif du fichier
                print(filename)

                # Créez le répertoire si nécessaire
                directory = os.path.dirname(filename)
                if not default_storage.exists(directory):
                    default_storage.makedirs(directory)

                # Enregistrez la vignette en utilisant ContentFile
                buffer = BytesIO()
                thumb.save(buffer, format='JPEG')
                content_file = ContentFile(buffer.getvalue())
                default_storage.save(filename, content_file)

                # Mise à jour du champ de vignette dans l'instance du modèle
                setattr(instance, field_name, filename)
                instance.save()