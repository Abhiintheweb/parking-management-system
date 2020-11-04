from django.db import models


# Create your models here.
from django.utils import timezone


class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'
    createdAt = models.DateTimeField(db_column='created_at', default=timezone.now)
    updatedAt = models.DateTimeField(db_column='updated_at', default=timezone.now)
    isDeleted = models.BooleanField(db_column='is_deleted', default=False)

    class Meta:
        abstract = True  # Set this model as Abstract


class Vehicle(BaseModel):
    name = models.CharField(max_length=30)
    vehicleNumber = models.CharField(db_column='vehicle_number', max_length=50)
    vehicleType = models.CharField(db_column='vehicle_type',max_length=50)
    userId = models.IntegerField(db_column='user_id')

    class Meta:
        db_table = 'vehicle'
