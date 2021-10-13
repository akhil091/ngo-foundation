from django.db import models
import sys
from django.utils.timezone import now
from PIL import Image
from io import BytesIO
from datetime import date
from django.core.files.uploadedfile import InMemoryUploadedFile
from ckeditor.fields import RichTextField

class Volunteer(models.Model):
    image = models.ImageField(upload_to="images_volunteer")
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class Cause(models.Model):
    image = models.ImageField(upload_to="images_cause")
    title = models.CharField(max_length=5000)
    text =  RichTextField(blank=True,null=True)
    target = models.IntegerField()
    progress = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-pub_date',]


    def __str__(self):
        return f"{self.title}"

class Blog(models.Model):
    image = models.ImageField(upload_to="images_blog")
    title = models.CharField(max_length=500)
    text =  RichTextField(blank=True,null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-date',]

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"


class gallery(models.Model):
    images = models.ImageField(upload_to='gallery', default="")
    pub_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-pub_date',]

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(gallery, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=50)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

class events(models.Model):
    title = models.CharField(max_length=1500,default="")
    description = RichTextField(blank=True,null=True)
    venue = models.CharField(max_length=1000,default="")
    eventdate = models.DateField()
    time = models.TimeField( default="", null=True, blank=True)

    def __str__(self):
        return self.title

    def month(self):
        return self.eventdate.strftime('%b')

    def year(self):
        return self.eventdate.strftime('%Y')

    def dateday(self):
        return self.eventdate.strftime("%d")

    class Meta:
        ordering = ['-eventdate','time']
