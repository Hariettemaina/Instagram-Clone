# Generated by Django 4.0.5 on 2022-06-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_likes_posts_remove_image_likes_remove_image_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike')], default='like', max_length=10),
        ),
    ]
