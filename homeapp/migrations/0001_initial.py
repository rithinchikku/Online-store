# Generated by Django 4.2.13 on 2024-07-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='book_media')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
