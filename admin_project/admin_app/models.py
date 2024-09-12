from django.db import models

# Create your models here.
class Membership_model(models.Model):
    name=models.CharField(max_length=500)
    MEMBERSHIP_CHOICES=(
        ('s','Standard'),
        ('p','Premium'),
        ('ux','Ultimate Deluxe'),
    )
    membership_plan=models.CharField(max_length=2,choices=MEMBERSHIP_CHOICES)
    membership_active=models.BooleanField(default=True)
    unique_code=models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Gym Members'
        ordering=['name']
        
class Client_model(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Job_title=models.CharField(max_length=100)