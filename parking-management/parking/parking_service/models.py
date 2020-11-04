from django.db import models
from django.utils import timezone


class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'
    createdAt = models.DateTimeField(db_column='created_at', default=timezone.now)
    updatedAt = models.DateTimeField(db_column='updated_at', default=timezone.now)
    isDeleted = models.BooleanField(db_column='is_deleted', default=False)

    class Meta:
        abstract = True  # Set this model as Abstract


# Create your models here.
class ParkingSlots(BaseModel):
    name = models.CharField(max_length=30)
    isBlocked = models.BooleanField(db_column='is_blocked', default=False)
    blockedByVehicleId = models.IntegerField(db_column='blocked_by_vehicle_id', blank=True, null=True)

    class Meta:
        db_table = 'parking_slot'


class ParkingInteraction(BaseModel):
    parkingSlotId = models.IntegerField(db_column='parking_slot_id')
    vehicleId = models.IntegerField(db_column='vehicle_id')
    exitTime = models.DateTimeField(db_column='exit_time', null=True)

    class Meta:
        db_table = 'parking_interaction'
