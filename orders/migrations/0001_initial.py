# Generated by Django 4.0.5 on 2022-06-07 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lectures', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
