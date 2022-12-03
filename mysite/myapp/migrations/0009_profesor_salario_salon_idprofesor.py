# Generated by Django 4.1.3 on 2022-12-03 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_profesor_alter_orderedalum_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='salario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salon',
            name='idProfesor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.profesor'),
            preserve_default=False,
        ),
    ]