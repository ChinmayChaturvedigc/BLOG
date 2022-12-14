# Generated by Django 4.1.1 on 2022-09-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('timeStamp', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=130)),
            ],
        ),
    ]
