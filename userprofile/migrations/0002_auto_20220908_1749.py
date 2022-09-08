# Generated by Django 3.2.15 on 2022-09-08 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.role'),
        ),
    ]