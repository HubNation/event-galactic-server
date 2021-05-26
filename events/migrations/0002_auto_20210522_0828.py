# Generated by Django 3.1.1 on 2021-05-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.IntegerField(choices=[(1, 'exhibitions'), (2, 'theater'), (3, 'shows')], verbose_name='category name'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_name',
            field=models.IntegerField(choices=[(1, 'will visit'), (2, "won't visit"), (3, 'already visited')], verbose_name='status name'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.IntegerField(choices=[(1, 'image'), (2, 'music'), (3, 'video')], verbose_name='type name'),
        ),
    ]