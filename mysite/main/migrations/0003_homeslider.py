# Generated by Django 4.1.7 on 2023-03-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_homebginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Slider name')),
                ('img', models.ImageField(upload_to='images', verbose_name='Slider image')),
                ('proff1', models.CharField(blank=True, max_length=60, verbose_name='Slider proff1')),
                ('proff2', models.CharField(blank=True, max_length=60, verbose_name='Slider proff2')),
                ('logo', models.ImageField(blank=True, upload_to='images', verbose_name='Slider logo')),
                ('link1', models.URLField(blank=True, verbose_name='Slider link1')),
                ('link2', models.URLField(blank=True, verbose_name='Slider link2')),
                ('link3', models.URLField(blank=True, verbose_name='Slider link3')),
            ],
        ),
    ]
