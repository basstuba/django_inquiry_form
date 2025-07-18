# Generated by Django 4.2.5 on 2025-06-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='名')),
                ('last_name', models.CharField(max_length=100, verbose_name='姓')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, '男性'), (2, '女性'), (3, '未回答')], default=3, verbose_name='性別')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('tell', models.CharField(max_length=20, verbose_name='電話番号')),
                ('address', models.CharField(max_length=255, verbose_name='住所')),
                ('building', models.CharField(blank=True, max_length=255, null=True, verbose_name='建物名')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, '商品のお届けについて'), (2, '商品の交換について'), (3, '商品トラブル'), (4, 'ショップへのお問い合わせ'), (5, 'その他')], verbose_name='お問い合わせの種類')),
                ('detail', models.TextField(verbose_name='お問い合わせ内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='お問い合わせ日')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
