from django.contrib import admin

# Register your models here.
from . models import QuoteCategory
from . models import Quote

admin.site.register(QuoteCategory)
admin.site.register(Quote)