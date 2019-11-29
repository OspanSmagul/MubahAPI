# Generated by Django 2.2.7 on 2019-11-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(blank=True, default='', max_length=32)),
                ('name', models.CharField(blank=True, default='', max_length=128)),
                ('ingridients', models.CharField(blank=True, default='', max_length=1024)),
                ('status', models.CharField(blank=True, default='', max_length=16)),
                ('why_haram', models.CharField(blank=True, default='', max_length=1024)),
                ('why_doubtful', models.CharField(blank=True, default='', max_length=1024)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]