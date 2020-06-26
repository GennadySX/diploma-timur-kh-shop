# Generated by Django 3.0.7 on 2020-06-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20200623_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterModelOptions(
            name='pay',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказов'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('pc', 'pc'), ('notebook', 'notebook'), ('accessories', 'accessories'), ('mobile', 'mobile')], default='mobile', max_length=20),
        ),
    ]