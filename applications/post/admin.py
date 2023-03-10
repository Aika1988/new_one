from django.contrib import admin
from applications.post.models import *

class ImageAdmin(admin.TabularInline):
    model = PostImage
    fields = ('image',)
    max_num = 4

class PostAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,)


    list_display = ('title', 'owner', 'post_count', 'created_at', 'john')
    list_filter = ('owner',)
    search_fields = ('title',)
    exclude = ('john',)

    def post_count(self, obj):
        return obj.likes.filter(is_like=True).count()



admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Comment)
