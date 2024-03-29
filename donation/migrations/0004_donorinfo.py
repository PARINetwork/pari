# Generated by Django 2.2 on 2021-06-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_auto_20201113_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('pan', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=252)),
                ('payment_method', models.CharField(max_length=100)),
                ('donation_date_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'donation_donor_info',
            },
        ),
    ]
