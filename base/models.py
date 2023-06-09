from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


# Model for Buddies
class Buddies(models.Model):
    BUDDY_CHOICES = (
        ('whale', 'Whale'),
        ('turtle', 'Turtle'),
        ('dolphin', 'Dolphin'),
        ('seal', 'Seal'),
        ('seagull', 'Seagull'),
    )

    name = models.CharField(max_length=50, choices=BUDDY_CHOICES)
    picture = models.ImageField(upload_to='static/images/profile-pictures')

    # Many-to-One relationship with User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # Add unique constraint to user and name fields
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

    
# --------------------------------------------------------------------------------------

# Model for User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    age = models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to='static/images/profile-pictures', null=True, blank=True)
    


    def __str__(self):
        return str(self.user)

    
#------------------------------------------------------------------------------------------

# Model for user Posts
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    postBody = models.TextField(null=True)
    
    #Date and time fields
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)
    

#Model for Videos
class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-added']

    
