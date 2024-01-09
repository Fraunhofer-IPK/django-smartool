# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

class ArduinoResults(models.Model):
    ID = models.IntegerField(primary_key=True)
    cycle_nr = models.CharField(max_length=255)
    mean_ambient_temperature = models.CharField(max_length=255)
    mean_ambient_humidity = models.CharField(max_length=255)
    mean_cavity_temperature = models.CharField(max_length=255)
    mean_cavity_pressure = models.CharField(max_length=255)
    mean_closing_force = models.CharField(max_length=255)
    class Meta:
        managed = False  # To indicate that this model does not create/manage the table
        db_table = 'sql_results'
        app_label = 'authentication'

    def __str__(self):
        return f"ID: {self.ID}, cycle_nr: {self.cycle_nr}, mean_ambient_temperature: {self.mean_ambient_temperature}, mean_ambient_humidity: {self.mean_ambient_humidity}, mean_cavity_temperature: {self.mean_cavity_temperature}, mean_cavity_pressure: {self.mean_cavity_pressure}, mean_closing_force: {self.mean_closing_force}"
    
results = ArduinoResults.objects.filter(ID__gt=0).values('ID', 'cycle_nr', 'mean_ambient_temperature', 'mean_ambient_humidity',
                                                          'mean_cavity_temperature', 'mean_cavity_pressure', 'mean_closing_force')
# print(results)