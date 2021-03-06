# Generated by Django 3.0.7 on 2020-06-28 21:15

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('member_calendar', '0002_membercalendarevent_no_physical_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEventTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='member_calendar.MemberCalendarEvent')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_calendar_calendareventtag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
