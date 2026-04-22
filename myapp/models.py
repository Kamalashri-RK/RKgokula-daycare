from django.db import models

# Create your models here.
from django.db import models

class AdmissionEnquiry(models.Model):

    child_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    age_group = models.CharField(max_length=50)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=[('New','New'),('Contacted','Contacted')],
        default='New'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parent_name


    