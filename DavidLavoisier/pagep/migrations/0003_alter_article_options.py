# Generated by Django 5.0.6 on 2024-08-15 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagep', '0002_article_date_article_image1_article_image2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
    ]
