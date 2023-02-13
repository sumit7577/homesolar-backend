from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
selectChoices = (
    ("Verified","Verified"),
    ("Rejected","Rejected"),
    ("Not Checked","Not Checked")
)
class Email(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    name = models.CharField(null=False,blank=False,max_length=150)
    email = models.EmailField(null=True,blank=True,max_length=150)
    mobile = models.CharField(null=False,blank=False,validators=[phone_regex],max_length=15)
    address = models.CharField(null=False,blank=False,max_length=1000)
    verified = models.CharField(null=False,blank=False,choices=selectChoices,default="Not Checked",max_length=50)

    def __str__(self) -> str:
        return self.name
