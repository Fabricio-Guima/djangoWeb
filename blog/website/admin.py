from django.contrib import admin
from .models import Post,Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle','full_name', 'categories', 'deleted']
    search_fields = ['title', 'subtitle']
    #fields = ('title', 'sub_title')

    # def get_queryset(self, request):
    #     return Post.objects.filter(deleted=False)



admin.site.register(Post, PostAdmin)
admin.site.register(Contact)

