from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from car_app.models import Car, Service_Company


class Failure_Node(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
      return  self.name


class Recovery_Method(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
       return self.name


def validate_date_recovery(date_recovery, date_rejection):
    if date_recovery > date_rejection:
        return True
    else:
        raise ValidationError('The date of failure is greater than the date of restoration')
    
class Claims(models.Model):
    date_rejection = models.DateField()
    operating_time_mh = models.PositiveIntegerField()
    failure_node = models.ForeignKey(to=Failure_Node, on_delete=models.CASCADE, \
                                     related_name='claims_fluire_node')
    failure_description = models.CharField(max_length=255)
    recovery_method = models.ForeignKey(to=Recovery_Method, on_delete=models.CASCADE, \
                                        related_name='claims_recovery_method')
    used_spare_parts = models.TextField()
    date_recovery = models.DateField()
    downtime = models.PositiveIntegerField(blank=True, null=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE, \
                            related_name='claims_car')
    service_company = models.ForeignKey(to=Service_Company, on_delete=models.CASCADE, \
                                        related_name='claims_service_company')

    def get_absolute_url(self):
        return reverse("claims:claims-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.failure_description

    def save(self,*args, **kwargs):
        self.downtime = (self.date_recovery - self.date_rejection).days
        self.full_clean()
        super(Claims, self).save(*args, **kwargs)

    def clean(self):
        validate_date_recovery(self.date_recovery, self.date_rejection)
        super(Claims,self).clean()

    class Meta:
        ordering = ['-date_rejection']

