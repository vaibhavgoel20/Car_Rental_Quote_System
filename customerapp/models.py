from django.db import models

# Create your models here.


class CustomerDetails(models.Model):
    cust_name = models.CharField(max_length=50, null=True, blank=True)
    phone_no = models.IntegerField()
    code = (
        ('B', 'B'),
        ('D', 'D'),
        ('W', 'W'),
    )
    cust_code = models.CharField(max_length=1, choices=code)
    days = models.IntegerField()
    first_odo = models.IntegerField()
    state = (
        ('Punjab', 'Punjab'),
        ('Haryana', 'Haryana'),
        ('Himachal', 'Himachal'),
        ('UP', 'Uttar Pradesh'),
    )
    cust_state = models.CharField(max_length=30, choices=state)

    def __str__(self):
        return self.cust_name




class SignupDetails(models.Model):
    admin_name = models.CharField(max_length=50, null=True, blank=True)
    admin_email = models.CharField(max_length=50) 
    admin_username = models.CharField(max_length=50) 
    admin_password = models.CharField(max_length=50)

    def __str__(self):
        return self.admin_name




class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name




class States(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return self.state_name



class BillDetails(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    c_name = models.CharField(max_length=50, null=True, blank=True)
    phn_no = models.IntegerField()
    c_code =  models.CharField(max_length=1)
    c_state = models.CharField(max_length=50)
    no_days = models.IntegerField()
    odo_first = models.IntegerField()
    odo_final = models.IntegerField()
    no_miles = models.IntegerField()
    tax_rate = models.CharField(max_length = 5)
    amount_tax = models.IntegerField()
    amount_due = models.IntegerField()

    def __str__(self):
        return str(self.created_at)
