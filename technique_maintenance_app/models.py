from django.db import models
from django.urls import reverse
from car_app.models import Car, Service_Company

class Kind_Technique_Maintenance(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Organization_Tat_Carried_Out(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Technique_Maintenance(models.Model):
    kind_technique_maintenance = models.ForeignKey(to=Kind_Technique_Maintenance, on_delete=models.CASCADE, \
                                                   related_name='kind_TO')
    date_holding_TO = models.DateField()
    operating_time_mh = models.PositiveIntegerField()
    dress_order_no = models.CharField(max_length=255)
    dress_order = models.DateField()
    organization_that_carried_TO = models.ForeignKey(to=Organization_Tat_Carried_Out, on_delete=models.CASCADE, \
                                                   related_name='TO_organization_that_carried')
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE, \
                                                   related_name='TO_Car')
    service_company = models.ForeignKey(to=Service_Company, on_delete=models.CASCADE, \
                                        related_name='technique_maintenance_service_company')

    def get_absolute_url(self):
        return reverse("technique_maintenance:to-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-date_holding_TO']



