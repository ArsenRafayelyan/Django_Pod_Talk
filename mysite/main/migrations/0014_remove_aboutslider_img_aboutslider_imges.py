# Generated by Django 4.1.7 on 2023-03-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutslider',
            name='img',
        ),
        migrations.AddField(
            model_name='aboutslider',
            name='imges',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Slider image'),
        ),
    ]
