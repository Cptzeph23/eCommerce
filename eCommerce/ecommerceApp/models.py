from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# Profile
class Profile(models.Model):
    """ Extends Django's Built in User with app-specific fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE,
    related_name="profile")
    phone_number = models.CharField(max_length=20, blank=True)
    google_id = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """Automatically creates a profile whenever a new User is created"""
    if created:
        Profile.objects.create(User=instance)
    else:
        # Profile might not exist for pre-existing users; get_or_create is effective    
        Profile.objects.get_or_create(user=instance)


     








class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

# model for login and registration

class Member(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email   
    
# model for registration form
class NewUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

