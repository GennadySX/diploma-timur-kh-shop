# Generated by Django 3.0.7 on 2020-06-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200621_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('pc', 'pc'), ('mobile', 'mobile'), ('notebook', 'notebook'), ('accessories', 'accessories')], default='mobile', max_length=20),
        ),
    ]
