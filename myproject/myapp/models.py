from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=50)
    address =  models.CharField(max = 300)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    company_mail = models.EmailField()
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name
    

class employee (models.Model):
    name = models.CharField(max_length=50)
    address =  models.CharField(max = 300)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    company_mail = models.EmailField()
    contact_number = models.IntegerField()
    date_of_joining = models.DateField()
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    company = models.ForeignKey('company',blank=True, on_delete=models.CASCADE)
    e_id = models.IntegerField()
    DEPARTMENT_CHOICES = [
        ('tech', 'Tech'),
        ('non-tech', 'Non-Tech'),
        ('finance', 'Finance'),
    ]
    e_department = models.CharField( max_length=20,  choices=DEPARTMENT_CHOICES, default='tech' )
    e_salary = models.IntegerField()
    increament_date = models.DateField()

    def __str__(self):
        return self.name
    