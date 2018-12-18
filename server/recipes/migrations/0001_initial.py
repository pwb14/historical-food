# Generated by Django 2.1.4 on 2018-12-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
                ('place_of_birth', models.CharField(max_length=16)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField()),
                ('pages', models.PositiveIntegerField(default=200)),
                ('authors', models.ManyToManyField(related_name='books', to='recipes.Author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipe',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='recipes',
            field=models.ManyToManyField(blank=True, related_name='books', to='recipes.Recipe'),
        ),
    ]
