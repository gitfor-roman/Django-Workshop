# Generated by Django 5.0.1 on 2024-01-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
