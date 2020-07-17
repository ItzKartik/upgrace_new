from django.db import models


class used_by(models.Model):
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class left_id(models.Model):
    link = models.ForeignKey(used_by, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)


class insta_id(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=3000)

    def __str__(self):
        return self.email

class join_us(models.Model):
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.email