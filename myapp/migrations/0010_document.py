# Generated by Django 3.1.4 on 2021-09-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=200)),
                ('Image', models.FileField(upload_to='')),
            ],
        ),
    ]
