# Generated by Django 3.2.4 on 2021-06-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kurs Başlığı Giriniz', max_length=200, unique=True, verbose_name='Kurs Adı')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='courses/default_courses_image.jpg', upload_to='courses/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
