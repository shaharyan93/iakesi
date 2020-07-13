# Generated by Django 3.0.7 on 2020-07-13 04:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200609_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationimage',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('4136d706-daea-4377-a3ea-a19e15e27eb4'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('c7a25c38-7283-4629-b022-cc86a20443b5'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='serieslocationimage',
            name='image_name',
            field=models.UUIDField(default=uuid.UUID('f54e6150-88b1-4d78-825d-e30511380b71'), editable=False, unique=True),
        ),
    ]
