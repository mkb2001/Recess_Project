# Generated by Django 4.2.3 on 2023-08-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_merge_0003_studentdetails_0004_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
                ('courseCode', models.CharField(max_length=20)),
                ('courseDescription', models.TextField()),
                ('effectiveness', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('interest', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('improvement', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
