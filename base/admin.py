from django.contrib import admin
from .models import Profile, Buddies, Posts, Video

# Register your models here.
admin.site.register(Profile)
admin.site.register(Buddies)
admin.site.register(Posts)
admin.site.register(Video)