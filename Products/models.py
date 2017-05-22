# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_type = models.CharField(max_length=128)

    class Meta:
        db_table = "Products"
