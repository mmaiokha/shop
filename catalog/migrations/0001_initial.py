# Generated by Django 3.0.2 on 2022-06-24 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('author', models.CharField(max_length=255, verbose_name='ФИО автора')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.PositiveIntegerField(verbose_name='Цена товара')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('type_of_product', models.CharField(max_length=255, verbose_name='Тип товара')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_available', models.BooleanField()),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория товара')),
            ],
        ),
        migrations.CreateModel(
            name='EProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.Product')),
                ('file', models.FileField(upload_to='')),
            ],
            bases=('catalog.product',),
        ),
        migrations.CreateModel(
            name='PProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.Product')),
                ('weight', models.PositiveIntegerField(verbose_name='Вес товара')),
                ('count_of_product', models.PositiveIntegerField(verbose_name='Кол-во товаров на складе')),
            ],
            bases=('catalog.product',),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Отзыв')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_children', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='catalog.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductCategory'),
        ),
    ]