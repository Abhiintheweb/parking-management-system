# Generated by Django 3.1.3 on 2020-11-04 03:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parking_service', '0002_auto_20201104_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingInteraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(db_column='created_at', default=django.utils.timezone.now)),
                ('updatedAt', models.DateTimeField(db_column='updated_at', default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(db_column='is_deleted', default=False)),
                ('parkingSlotId', models.IntegerField(db_column='parking_slot_id')),
                ('vehicleId', models.IntegerField(db_column='vehicle_id')),
                ('exitTime', models.DateTimeField(db_column='exit_time', null=True)),
            ],
            options={
                'db_table': 'parking_interaction',
            },
        ),
    ]
