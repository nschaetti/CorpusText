# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Text, Author, Authorship


class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ['title']
    date_hierarchy = 'date'
    ordering = ['date']
    search_fields = ['title']
# end TextAdmin

admin.site.register(Text, TextAdmin)
admin.site.register(Author)
admin.site.register(Authorship)
