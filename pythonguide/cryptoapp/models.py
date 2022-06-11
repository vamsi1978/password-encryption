from django.db import models

class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=16)
    class Meta:
        db_table="Login"