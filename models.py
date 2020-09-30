from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=10)
    emailID = models.EmailField()
    feedback = models.TextField()
    def __str__(self):
        return self.name