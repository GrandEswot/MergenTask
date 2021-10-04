from django.db import models


class Number(models.Model):
    numbers = models.IntegerField(verbose_name='Число')

    def __str(self):
        return self.numbers
