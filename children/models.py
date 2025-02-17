from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to parent user
    slug = models.SlugField(unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    allergies = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate a new slug if it doesn't exist
            base_slug = slugify(f"{self.first_name}-{self.last_name}-{self.parent.username}")
            slug = base_slug
            counter = 1
            while Child.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.parent.username})"
