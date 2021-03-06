# Generated by Django 3.1.5 on 2021-04-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=256)),
                ('good_type', models.CharField(choices=[('A', 'Excellent'), ('A-', 'Outstanding'), ('B+', 'Very good'), ('B', 'Good'), ('C', 'Fair'), ('F', 'Fail')], max_length=2)),
                ('Grade', models.IntegerField()),
                ('Comments', models.TextField()),
            ],
        ),
    ]
