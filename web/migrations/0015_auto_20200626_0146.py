# Generated by Django 3.0.7 on 2020-06-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20200624_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='availability',
        ),
        migrations.AddField(
            model_name='product',
            name='available_count',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Облицовочные материалы', 'Облицовочные материалы'), ('Листовые материалы', 'Листовые материалы'), ('Изоляционные материалы', 'Изоляционные материалы'), ('сухие смеси и грунтовки', 'сухие смеси и грунтовки')], default='сухие смеси и грунтовки', max_length=50),
        ),
    ]
