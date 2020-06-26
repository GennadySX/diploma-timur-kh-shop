# Generated by Django 3.0.7 on 2020-06-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20200626_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='delivery',
            field=models.PositiveIntegerField(default=0, verbose_name='Стоимость доставки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Изоляционные материалы', 'Изоляционные материалы'), ('Облицовочные материалы', 'Облицовочные материалы'), ('сухие смеси и грунтовки', 'сухие смеси и грунтовки'), ('Листовые материалы', 'Листовые материалы')], default='сухие смеси и грунтовки', max_length=50),
        ),
    ]
