from django.db import models


class Math(models.Model):
    operand_one = models.IntegerField()
    operand_two = models.IntegerField()
    operation = models.CharField(max_length=1)
    answer = models.IntegerField()