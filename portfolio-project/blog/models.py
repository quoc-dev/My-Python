from django.db import models


# Create Blog model

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_day = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_day.strftime('%b %e %Y')


