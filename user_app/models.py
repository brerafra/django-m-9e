from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    card = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    password = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        txt = f"{self.name}"
        return txt

    class Meta:
        verbose_name_plural = 'users'