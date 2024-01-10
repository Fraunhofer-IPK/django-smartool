# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

class ArduinoResults(models.Model):
    ID = models.IntegerField(primary_key=True)
    cycle_nr = models.CharField(max_length=255)# Maximum length of 255 characters
    mean_ambient_temperature = models.CharField(max_length=255)
    mean_ambient_humidity = models.CharField(max_length=255)
    mean_cavity_temperature = models.CharField(max_length=255)
    mean_cavity_pressure = models.CharField(max_length=255)
    mean_closing_force = models.CharField(max_length=255)
    class Meta:#  A class inside the model used to provide metadata for the model.
        managed = False # To indicate that this model does not create/manage the table. It assumes the table already exists in the database.
        db_table = 'sql_results' # Specifies the name of the database table where this model's data is stored
        app_label = 'authentication' # Specifies the app label to which this model belongs

    def __str__(self): # Defines a method that returns a string representation of the model instance
        return f"ID: {self.ID}, cycle_nr: {self.cycle_nr}, mean_ambient_temperature: {self.mean_ambient_temperature}, mean_ambient_humidity: {self.mean_ambient_humidity}, mean_cavity_temperature: {self.mean_cavity_temperature}, mean_cavity_pressure: {self.mean_cavity_pressure}, mean_closing_force: {self.mean_closing_force}"
    
results = ArduinoResults.objects.filter(ID__gt=0).values('ID', 'cycle_nr', 'mean_ambient_temperature', 'mean_ambient_humidity',
                                                          'mean_cavity_temperature', 'mean_cavity_pressure', 'mean_closing_force')
# print(results)