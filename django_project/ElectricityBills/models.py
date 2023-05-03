from django.db import models

class Payment(models.Model):
    codenumber = models.CharField(max_length=20)
    meterreding = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    comments = models.TextField()

    def __str__(self):
        return self.number