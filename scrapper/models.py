from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_date = models.DateField()

    def __str__(self):
        return f"{self.title} at {self.company}"