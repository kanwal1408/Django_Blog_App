from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile', validators=[
        FileExtensionValidator(['png', 'jpg'])])  # validators: used to accept only images other than videos

    def __str__(self):
        return self.user.username
