from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
