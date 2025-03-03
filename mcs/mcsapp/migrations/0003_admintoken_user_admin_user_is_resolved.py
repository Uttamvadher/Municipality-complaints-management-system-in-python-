# Generated by Django 5.1.6 on 2025-02-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcsapp', '0002_alter_complaint_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='Admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_resolved',
            field=models.BooleanField(default=False),
        ),
    ]
