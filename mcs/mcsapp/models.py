



from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username  = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)  
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    last_login =models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)




class Complaint(models.Model):
    DEPARTMENT_CHOICES = [
        ('Water', 'Water Department'),
        ('electricity', 'Electricity Department'),
        ('sanitation', 'Sanitation Department'),
        ('Road', 'Road Maintenance'),
    ]

    name = models.CharField(max_length=255)  # Directly add the name field
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    address = models.TextField()
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateField(null=True, blank=True)




    def __str__(self):
        return f"{self.name} - {self.department}"




    

   
