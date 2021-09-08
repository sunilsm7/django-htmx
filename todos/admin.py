from django.contrib import admin
from compressor.filters import CompilerFilter
from .models import Todo
# Register your models here.


class PostCSSFilter(CompilerFilter):
    command = 'postcss'

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('excerpt',)

    def excerpt(self, obj):
        return obj.get_excerpt(8)
