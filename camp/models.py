from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Club(models.Model):
    name = models.CharField(max_length=255)  # Club name
    slug = models.SlugField(max_length=255)  # Club slug
    description = models.TextField()  # Detailed club description
    location = models.CharField(max_length=255)  # Physical location
    age_group_min = models.IntegerField()  # Minimum age allowed
    age_group_max = models.IntegerField()  # Maximum age allowed
    start_date = models.DateField()  # Club start date
    end_date = models.DateField()  # Club end date
    daily_schedule = models.TextField(blank=True, null=True)  # Activities per day
    capacity = models.PositiveIntegerField()  # Maximum number of kids allowed
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price per child
    is_active = models.BooleanField(default=True)  # If club is active or not
    contact_email = models.EmailField(blank=True, null=True)  # Contact email for queries
    contact_phone = models.CharField(max_length=20, blank=True, null=True)  # Phone number
    website = models.URLField(blank=True, null=True)  # Club website link
    available_spots = models.PositiveIntegerField(default=0)  # Track available slots
    featured_image = CloudinaryField('image', default='placeholder')  # Club image
    status = models.IntegerField(choices=STATUS, default=0)  # Club status

    def __str__(self):
        return self.name


