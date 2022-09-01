# Generated by Django 3.2.2 on 2022-09-01 15:27

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False, unique='True')),
                ('password', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('fb_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('website_link', models.URLField()),
                ('about', models.TextField()),
                ('img', models.ImageField(upload_to='media')),
                ('is_agent', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_varified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], default='Rent', max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('area', models.IntegerField()),
                ('building_year', models.DateField()),
                ('img', models.ImageField(upload_to='media')),
                ('about', models.TextField()),
                ('bedroom', models.IntegerField()),
                ('living', models.IntegerField()),
                ('dinning', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('garage', models.BooleanField(default=False)),
                ('watchman', models.BooleanField(default=False)),
                ('garden', models.BooleanField(default=False)),
                ('swimmingpool', models.BooleanField(default=False)),
                ('hospital', models.BooleanField(default=False)),
                ('shoppingmall', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]