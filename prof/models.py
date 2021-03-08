from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def path_upload_avatars(instance, filename):
    filebase, extension = filename.split('.')
    return 'profiles/avatars/%s.%s/' % (instance.username, extension)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(default='avatars/avatar.svg', upload_to=path_upload_avatars)
    birth_day = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True)
    about = models.CharField(max_length=400, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=User) # new registered user, automatically creates an instance of the Profile class
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def __str__(self):
        return str(self.user)


