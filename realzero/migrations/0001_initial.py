# Generated by Django 4.2 on 2025-03-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='realzero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Manufacturer', models.CharField(default='Unknown', max_length=50, verbose_name='제조사명')),
                ('product_name', models.CharField(max_length=50, verbose_name='제품명')),
                ('Capacity', models.CharField(default=0, max_length=50, verbose_name='용량 (g)')),
                ('Product_calorific_value', models.CharField(default=0, max_length=50, verbose_name='열량 (g)')),
                ('carbohydrates', models.CharField(max_length=50, verbose_name='탄수화물 (g)')),
                ('protein', models.CharField(max_length=50, verbose_name='단백질 (g)')),
                ('fat', models.CharField(max_length=50, verbose_name='지방 (g)')),
                ('saturated_fat', models.CharField(default=0, max_length=50, verbose_name='포화지방 (g)')),
                ('trans_fat', models.CharField(default=0, max_length=50, verbose_name='트렌스지방 (g)')),
                ('Cholesterol', models.CharField(default=0, max_length=50, verbose_name='콜레스테롤 (mg)')),
                ('sodium', models.CharField(default=0, max_length=50, verbose_name='나트륨 (mg)')),
                ('Caffeine', models.CharField(default=0, max_length=50, verbose_name='카페인 (g)')),
                ('sugar', models.CharField(default=0, max_length=50, verbose_name='당류 (g)')),
                ('Sugar_alcohol', models.CharField(default=0, max_length=50, verbose_name='당알콜 (g)')),
                ('GI', models.CharField(default=0, max_length=50, verbose_name='GI지수')),
                ('GL', models.CharField(default=0, max_length=50, verbose_name='GL지수')),
                ('Raw_materials', models.TextField(default='Unknown', max_length=255, verbose_name='원재료명')),
                ('emoji', models.CharField(default='😊', max_length=20)),
                ('image', models.URLField(blank=True, max_length=500, null=True, verbose_name='이미지')),
                ('price', models.CharField(default=0, max_length=50, verbose_name='가격 (원)')),
            ],
            options={
                'verbose_name': '제로식품',
                'verbose_name_plural': '제로식품 목록',
            },
        ),
    ]
