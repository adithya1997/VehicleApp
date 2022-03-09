from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class VehicleOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manufacturer = models.CharField(max_length=100)
    modelname = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.id

    def __str__(self):
        return str(self.id)

