from django.contrib import admin
from compressor.filters import CompilerFilter
# Register your models here.


class PostCSSFilter(CompilerFilter):
    command = 'postcss'
