from django.db import models
from datetime import date

class empinfo(models.Model):

    employeeid = models.AutoField(primary_key=True)
    employeeemail = models.EmailField(max_length=250, null=True, blank=True)
    employeename = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    mobno = models.CharField(max_length=10)
    department = models.CharField(max_length=250, default='General')
    designation = models.CharField(max_length=250, default='Employee')
    salary = models.FloatField(default=0)
    date_of_joining = models.DateField(default=date.today)

    class Meta:
        db_table = 'empinfo'

    def __str__(self):
        return self.employeename