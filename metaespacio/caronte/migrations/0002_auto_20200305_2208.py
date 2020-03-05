# Generated by Django 2.2.11 on 2020-03-05 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caronte', '0001_initial'),
        ('espacios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lector',
            name='espacio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.Espacio'),
        ),
        migrations.AddField(
            model_name='entradasalida',
            name='espacio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.Espacio'),
        ),
        migrations.AddField(
            model_name='entradasalida',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='autorizacion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
