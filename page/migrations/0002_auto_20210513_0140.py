# Generated by Django 3.2 on 2021-05-12 20:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todomodel',
            options={'ordering': ['completed']},
        ),
        migrations.AddField(
            model_name='todomodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='discription',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
