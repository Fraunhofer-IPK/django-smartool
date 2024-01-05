# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

class ArduinoResults(models.Model):
    ID = models.IntegerField(primary_key=True)
    cycle_nr = models.CharField(max_length=255)

    class Meta:
        managed = False  # To indicate that this model does not create/manage the table
        db_table = 'sql_results'
        app_label = 'authentication'

    def __str__(self):
        return f"ID: {self.ID}, cycle_nr: {self.cycle_nr}"
    
results = ArduinoResults.objects.filter(ID__gt=0).values('ID', 'cycle_nr')
# print(results)