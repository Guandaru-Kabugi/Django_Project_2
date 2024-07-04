# Generated by Django 5.0.6 on 2024-07-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://th.bing.com/th/id/OIP.kz5A86qjMCk6lHYchAsRZAHaHa?rs=1&pid=ImgDetMain', max_length=600),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(),
        ),
    ]
