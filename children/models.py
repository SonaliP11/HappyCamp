from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to parent user
    slug = models.SlugField(unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    allergies = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.parent.username}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.parent.username})"
