# Generated by Django 3.0.3 on 2020-12-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigint_f', models.BigIntegerField()),
                ('bool_f', models.BooleanField()),
                ('date_f', models.DateField(auto_now=True)),
                ('char_f', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('size', models.CharField(choices=[('S', 'Smaill'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
    ]