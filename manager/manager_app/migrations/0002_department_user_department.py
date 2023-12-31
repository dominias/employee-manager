# Generated by Django 4.2.5 on 2023-10-20 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("manager_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "department_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("department_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="manager_app.department",
            ),
        ),
    ]
