# Generated by Django 3.1.7 on 2021-08-11 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketApk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apk', models.CharField(max_length=300)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.CharField(blank=True, max_length=300, null=True)),
                ('descriptionHTML', models.CharField(blank=True, max_length=10000, null=True)),
                ('summary', models.CharField(blank=True, max_length=1000, null=True)),
                ('installs', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('ratings', models.CharField(blank=True, max_length=100, null=True)),
                ('reviews', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('androidVersionText', models.CharField(blank=True, max_length=100, null=True)),
                ('developer', models.CharField(blank=True, max_length=200, null=True)),
                ('developerid', models.CharField(blank=True, max_length=200, null=True)),
                ('developerEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('developerWebsite', models.CharField(blank=True, max_length=300, null=True)),
                ('developerInternalID', models.CharField(blank=True, max_length=200, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=300, null=True)),
                ('screenshots', models.JSONField(blank=True, null=True)),
                ('contentRating', models.CharField(blank=True, max_length=100, null=True)),
                ('released', models.CharField(blank=True, max_length=100, null=True)),
                ('updated', models.CharField(blank=True, max_length=100, null=True)),
                ('version', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_sync', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApkReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(blank=True, max_length=300, null=True)),
                ('userImage', models.CharField(blank=True, max_length=300, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('thumbsUpCount', models.IntegerField(blank=True, null=True)),
                ('reviewCreatedVersion', models.CharField(blank=True, max_length=1000, null=True)),
                ('at', models.DateTimeField(blank=True, null=True)),
                ('replyContent', models.CharField(blank=True, max_length=1000, null=True)),
                ('repliedAt', models.DateTimeField(blank=True, null=True)),
                ('reviewId', models.CharField(blank=True, max_length=1000, null=True)),
                ('apk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.marketapk')),
            ],
        ),
    ]