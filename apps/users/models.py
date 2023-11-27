from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class UserRole(models.TextChoices):
    ADMIN = "admin"
    STUDENT = "student"


class CustomUser(AbstractUser):
    """
    Django defalut fields

        first_name
        last_name
        username
        password
        email
    """

    # optional fields
    patronymic = models.CharField(max_length=128, blank=True, null=True)
    course_number = models.IntegerField(blank=True, null=True)
    iin = models.CharField(max_length=32, blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STUDENT
    )

    def __str__(self):
        return str(f"{self.first_name} {self.last_name}")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
