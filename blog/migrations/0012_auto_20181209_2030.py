# Generated by Django 2.0.9 on 2018-12-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181209_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]