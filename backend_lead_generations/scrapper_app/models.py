from django.db import models

# Create your models here.

class Job_Posts(models.Model):
    lead_title = models.CharField(max_length=200,null=True, blank=True)
    job_post_url = models.URLField(max_length=500, null=True, blank=True)
    job_title = models.CharField(max_length=200, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=500, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    mobile_number1 = models.CharField(max_length=15, null=True, blank=True)
    mobile_number2 = models.CharField(max_length=15, null=True, blank=True)
    person_linkedin_url = models.URLField(max_length=500, null=True, blank=True)
    person_location = models.CharField(max_length=200, null=True, blank=True)
    platform_name = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.lead_title} )"