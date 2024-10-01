from django.contrib import admin
from .models import Post, Category, Comment, Privacy


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "image_url", "updated_by", "views")


class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "comment")


class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('privacy', 'last_updated')



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Privacy, PrivacyAdmin)

