from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')

class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')
    temperature = models.FloatField(verbose_name='Температура при измерении')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
