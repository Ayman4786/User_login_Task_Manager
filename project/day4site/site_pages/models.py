from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteModels(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title} - {self.description} was created at {self.created_at}"


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_pics/',default='profile_pics/default.png')

    def __str__(self):
        return self.user.username   
