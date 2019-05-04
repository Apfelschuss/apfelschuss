# Generated by Django 2.0.13 on 2019-05-04 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Voting category title')),
                ('slug', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Voting category URL slug')),
                ('voting_date', models.DateTimeField(verbose_name='Voting final date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False, verbose_name='Featured category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_de', models.CharField(blank=True, max_length=160, verbose_name='Voting title')),
                ('title_fr', models.CharField(blank=True, max_length=160, verbose_name='Voting title')),
                ('title_it', models.CharField(blank=True, max_length=160, verbose_name='Voting title')),
                ('title_rm', models.CharField(blank=True, max_length=160, verbose_name='Voting title')),
                ('title_en', models.CharField(blank=True, max_length=160, verbose_name='Voting title')),
                ('slug', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Voting URL slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False, verbose_name='Voting published')),
                ('description_de', tinymce.models.HTMLField(blank=True, verbose_name='Voting description')),
                ('description_fr', tinymce.models.HTMLField(blank=True, verbose_name='Voting description')),
                ('description_it', tinymce.models.HTMLField(blank=True, verbose_name='Voting description')),
                ('description_rm', tinymce.models.HTMLField(blank=True, verbose_name='Voting description')),
                ('description_en', tinymce.models.HTMLField(blank=True, verbose_name='Voting description')),
                ('thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Thumbnail')),
                ('video_url', models.URLField(blank=True, verbose_name='Youtube embedded URL')),
                ('admin_brochure', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Formal brochure')),
                ('admin_pro', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Final result pro [%]')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured voting')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.Author')),
                ('categories', models.ManyToManyField(to='votes.Category', verbose_name='Voting category')),
                ('next_voting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='votes.Voting')),
                ('previous_voting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='votes.Voting')),
            ],
        ),
    ]
