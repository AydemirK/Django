# Generated by Django 5.0.4 on 2024-04-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='year_of_issue',
            field=models.DateField(unique_for_year=False),
        ),
    ]