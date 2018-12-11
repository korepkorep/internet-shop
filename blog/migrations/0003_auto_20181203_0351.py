# Generated by Django 2.0.9 on 2018-12-03 02:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_products', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_hire', models.DateTimeField(default=django.utils.timezone.now)),
                ('working_days', models.TextField()),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_products', models.IntegerField(default=1)),
                ('name_of_product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('form_of_payment', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('date_completed', models.DateTimeField()),
                ('delivery_type', models.CharField(max_length=200)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('ident_num', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('num_of_products', models.IntegerField(default=1)),
                ('name_of_product', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='date_of_manufacture',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bucket',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Order'),
        ),
    ]