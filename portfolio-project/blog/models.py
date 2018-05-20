from django.db import models


# Create Blog model

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_day = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(up_load='images/')

# Add the blog app to the settings


# Create a migration


# Migrate


# Add to admin
