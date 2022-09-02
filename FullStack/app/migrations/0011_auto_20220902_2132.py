# Generated by Django 3.2.2 on 2022-09-02 15:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_apartment_is_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='type',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale'), ('Booked', 'Booked')], default='Rent', max_length=20),
        ),
        migrations.CreateModel(
            name='VisitRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_date', models.DateTimeField(default=datetime.datetime.now)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_request_apartment', to='app.apartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_request_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('attatched_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('is_approved', models.BooleanField(blank=True, null=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_request_apartment', to='app.apartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_request_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
