# Generated by Django 4.1.3 on 2022-12-07 16:45

from django.db import migrations, models
import django.db.models.deletion
import uitshare_main.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uitshare_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Category ID')),
                ('name', models.CharField(max_length=180, verbose_name='Category Title')),
                ('code_name', models.SlugField(max_length=200, unique=True, verbose_name='Category Code-name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('thumbnail_img', models.ImageField(blank=True, default='images/covers/default-cover.jpg', max_length=255, upload_to=uitshare_main.models.generate_cover_img_filepath_for_category, verbose_name='Thumbnail Image')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'uit_share_category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Course ID')),
                ('name', models.CharField(max_length=200, verbose_name='Course Title')),
                ('code_name', models.SlugField(max_length=255, unique=True, verbose_name='Course Code-name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('thumbnail_img', models.ImageField(blank=True, default='images/covers/default-cover.jpg', max_length=255, upload_to=uitshare_main.models.generate_cover_img_filepath_for_course, verbose_name='Background Cover Image')),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'db_table': 'uit_share_course',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='File ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='File Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('file_uploaded', models.FileField(max_length=255, upload_to=uitshare_main.models.generate_file_path, verbose_name='File/Document')),
                ('file_type', models.CharField(choices=[('Lab', 'Labs'), ('Lecture', 'Lectures'), ('Exam', 'Exams'), ('Exercise', 'Exercises'), ('Book', 'Books'), ('Other', 'Others')], default='Other', max_length=10, verbose_name='File Type')),
                ('course_id', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, related_name='files', to='uitshare_main.course', verbose_name='Course')),
            ],
            options={
                'verbose_name_plural': 'Files',
                'db_table': 'uit_share_file',
                'ordering': ['name'],
            },
        ),
    ]
