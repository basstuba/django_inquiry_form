from django.db import models


class Contact(models.Model):
    GENDER_CHOICES = [
        (1, '男性'),
        (2, '女性'),
        (3, '未回答'),
    ]
    CATEGORY_CHOICES = [
        (1, '商品のお届けについて'),
        (2, '商品の交換について'),
        (3, '商品トラブル'),
        (4, 'ショップへのお問い合わせ'),
        (5, 'その他'),
    ]
    first_name = models.CharField(
        verbose_name='名',
        max_length=100,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name='姓',
        max_length=100,
        null=False,
        blank=False
    )
    gender = models.PositiveSmallIntegerField(
        verbose_name='性別',
        choices=GENDER_CHOICES,
        default=3
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        null=False,
        blank=False
    )
    tell = models.CharField(
        verbose_name='電話番号',
        max_length=20,
        null=False,
        blank=False
    )
    address = models.CharField(
        verbose_name='住所',
        max_length=255,
        null=False,
        blank=False
    )
    building = models.CharField(
        verbose_name='建物名',
        max_length=255,
        null=True,
        blank=True
    )
    category = models.PositiveSmallIntegerField(
        verbose_name='お問い合わせの種類',
        choices=CATEGORY_CHOICES
    )
    detail = models.TextField(
        verbose_name='お問い合わせ内容',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(verbose_name='お問い合わせ日', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
