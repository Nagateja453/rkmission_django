# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from krish.models import AddPost, AddPage,Imageshow, Testinomials,Latestnews,Donations

# Register your models here.
admin.site.register(AddPost)
admin.site.register(AddPage)
admin.site.register(Imageshow)
admin.site.register(Testinomials)
admin.site.register(Latestnews)
admin.site.register(Donations)
