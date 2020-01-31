from django.contrib.auth.models import User
from django.db import models


class resume( models.Model ):
    user = models.OneToOneField( User, on_delete=models.CASCADE,primary_key=True )
    phone=models.BigIntegerField()
    country=models.CharField(max_length=150)
    city=models.CharField(max_length=150)

    def __str__(self):
        return str(self.user)+str(self.country)

