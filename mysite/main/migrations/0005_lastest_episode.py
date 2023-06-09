# Generated by Django 4.1.7 on 2023-03-25 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_homeslider_link1_name_homeslider_link2_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lastest_Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_rate', models.CharField(max_length=60, verbose_name='Video rate')),
                ('episode', models.PositiveIntegerField(verbose_name='Episode number')),
                ('name', models.CharField(max_length=60, verbose_name='Episode name')),
                ('text', models.CharField(max_length=100, verbose_name='Episode text')),
                ('button1', models.PositiveBigIntegerField(default=0, verbose_name='Button1')),
                ('button2', models.PositiveBigIntegerField(default=0, verbose_name='Button2')),
                ('button3', models.PositiveBigIntegerField(default=0, verbose_name='Button3')),
                ('button4', models.PositiveBigIntegerField(default=0, verbose_name='Button3')),
                ('after', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='after_post', to='main.homeslider')),
            ],
        ),
    ]
