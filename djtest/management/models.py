from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=256)
    publickey = models.CharField(max_length=256)

    def __str__(self):
        return '%s of %s' % (self.name, self.group_name)

class Tx(models.Model):
    txhash=models.CharField(max_length=256)
    package=models.BooleanField(default=False)

class Block(models.Model):
    blockhash=models.CharField(max_length=256)