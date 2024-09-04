from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('trainer', 'trainer'),
        ('student', 'student'),
        ('reviewer', 'reviewer'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    enrollment_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    student_id = models.CharField(max_length=10, unique=True)
    grade = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    credits = models.PositiveIntegerField()
    instructor_name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.course_name} ({self.course_id})"