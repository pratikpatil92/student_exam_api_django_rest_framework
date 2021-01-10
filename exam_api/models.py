from django.db import models
from django.conf import settings

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


def upload_to(instance, filename):
    return f'products2/{filename}'.format(filename=filename)


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """create new super user"""
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        name = self.first_name + " " + self.last_name
        return name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class Quenstions(models.Model):
    """Database model for questions"""
    question = models.CharField(max_length=800)
    question_type = models.CharField(max_length=255)
    choice_one = models.CharField(max_length=500, null=True)
    choice_two = models.CharField(max_length=500, null=True)
    choice_three = models.CharField(max_length=500, null=True)
    choice_four = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.question


class Answers(models.Model):
    """Database model for answers"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    questions = models.ForeignKey(Quenstions, on_delete=models.CASCADE)
    answer = models.TextField(null=True)
    image_ans = models.ImageField(null=True, upload_to=upload_to)
    submited = models.BooleanField(default=False)

    def __str__(self):
        return self.answer



