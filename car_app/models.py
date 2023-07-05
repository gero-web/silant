from django.db import models
from django.urls import reverse

class Model_Technique(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Model_Engine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Model_Transmission(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
class Model_Drive_Axle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Model_Steering_Bridge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Service_Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    head_machine_no = models.CharField(max_length=255,unique=True)
    model_techique = models.ForeignKey(to=Model_Technique, on_delete= models.CASCADE, related_name='cars_technique')
    model_engine = models.ForeignKey(to=Model_Engine, on_delete= models.CASCADE, related_name='cars_engine')
    head_engine_no = models.CharField(max_length=255)
    model_transmission = models.ForeignKey(to=Model_Transmission, on_delete=models.CASCADE, \
                                           related_name='cars_transmission')
    head_transmission_no = models.CharField(max_length=255)
    model_drive_axle = models.ForeignKey(to=Model_Drive_Axle, on_delete=models.CASCADE, related_name='cars_drive_axle')
    head_drive_axle_no = models.CharField(max_length=255)
    model_steering_bridge = models.ForeignKey(to=Model_Steering_Bridge, on_delete=models.CASCADE,\
                                              related_name='cars_steering_bridge')
    head_steering_bridge_no = models.CharField(max_length=255)
    deliver_contract_no = models.CharField(max_length=255)
    date_shipment = models.DateField()
    сonsignee = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE,related_name='cars_client')
    service_company = models.ForeignKey(to=Service_Company, on_delete=models.CASCADE,\
                                        related_name='cars_service_company')

    def get_absolute_url(self):
        return reverse("car:car_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return  self.head_machine_no

    class Meta:
        ordering = ['-date_shipment']


