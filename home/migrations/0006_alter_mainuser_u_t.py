# Generated by Django 3.2.7 on 2021-09-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210921_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='u_t',
            field=models.CharField(choices=[(1, 'customer'), (2, 'seller')], default=2, max_length=50),
        ),
    ]
