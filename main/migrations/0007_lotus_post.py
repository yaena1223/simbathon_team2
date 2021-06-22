# Generated by Django 3.2.4 on 2021-06-22 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_drama_post_odc_post_opus_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='lotus_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
