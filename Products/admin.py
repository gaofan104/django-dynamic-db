# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .middleware import local_vars
from .models import Product
# Register your models here.
# TODO: implement multiple DB support


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'default'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(local_vars.database_name)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(local_vars.database_name)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(local_vars.database_name)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request, using=local_vars.database_name, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request, using=local_vars.database_name, **kwargs)

admin.site.register(Product, MultiDBModelAdmin)
