from django.db import models

class ClientInfo(models.Model):
    client_name = models.CharField(max_length=100)
    website_link = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    no_of_employees = models.IntegerField()
    no_of_students = models.IntegerField()
    admin_email = models.CharField(max_length=100)
    admin_role = models.CharField(max_length=50)
    admin_sign = models.CharField(max_length=50)
    date_of_sign = models.DateField()