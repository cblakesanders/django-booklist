from django.db import models
from django.contrib.auth.models import User
from booklist.models import Book
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='Sam.jpg', upload_to='profile_pics')
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Relationship(models.Model): 
    followerUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requesting')
    followingUser = models.ForeignKey(User, on_delete= models.CASCADE, related_name='accepting')
    # Status 1 = normal
    status = models.IntegerField()

    def __str__(self): 
        return f'{self.followerUser} follows {self.followingUser}'