# Generated by Django 3.1.1 on 2021-05-22 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.IntegerField(choices=[(1, 'exhibitions'), (2, 'theater'), (3, 'shows')], max_length=255, verbose_name='category name')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='event title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='event description')),
                ('date_event', models.DateField(verbose_name='event date')),
                ('time_event', models.TimeField(verbose_name='event time')),
                ('place', models.CharField(max_length=255, verbose_name='address of an event')),
                ('interval_time', models.DurationField(blank=True, null=True, verbose_name='event interval time')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.IntegerField(choices=[(1, 'will visit'), (2, "won't visit"), (3, 'already visited')], max_length=255, verbose_name='status name')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.IntegerField(choices=[(1, 'image'), (2, 'music'), (3, 'video')], max_length=255, verbose_name='type name')),
            ],
        ),
        migrations.CreateModel(
            name='VisitEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='visit_event', to='events.event')),
                ('status_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='visit_status', to='events.status')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='visit_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='', verbose_name='url of a media file')),
                ('event_id', models.ManyToManyField(to='events.Event')),
                ('types_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.type')),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.category')),
                ('event_id', models.ManyToManyField(to='events.Event')),
            ],
        ),
    ]
