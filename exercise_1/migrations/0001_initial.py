# Generated by Django 4.2.13 on 2024-07-08 18:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=3)),
                ('curr_symbol', models.CharField(max_length=3)),
                ('phone_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state_code', models.CharField(max_length=10)),
                ('gst_code', models.CharField(max_length=5)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='exercise_1.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city_code', models.CharField(max_length=10)),
                ('phone_code', models.CharField(max_length=10)),
                ('population', models.IntegerField()),
                ('avg_age', models.FloatField()),
                ('num_of_adult_males', models.IntegerField()),
                ('num_of_adult_females', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='exercise_1.state')),
            ],
        ),
    ]
