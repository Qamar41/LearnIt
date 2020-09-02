from django.contrib import admin
from .models import faculty,testimonial,about,blog,contact,jobform,home_course,Comment,Lecture
# Register your models here.
class facultyadmin(admin.ModelAdmin):
    list_display = ('name','position','fb_id','twiter_id','linkden_id','image')
    list_display_links = ('name','position')
    search_fields = ('name','position')
    list_per_page = 10
# testimonial
class testimonialadmin(admin.ModelAdmin):
    list_display = ('name','image')

class contactadmin(admin.ModelAdmin):
    list_display = ('name','subject','email')

#blog

class blogadmin(admin.ModelAdmin):
    list_display = ('title','author','published_date','image','is_published')
    list_display_links = ('title','author')
    search_fields = ('title','author')
    list_per_page = 10
    list_editable = ('is_published',)





class jobformadmin(admin.ModelAdmin):
    list_display = ('name','email','image',)
    list_display_links = ('name','email')
    search_fields = ('name','email')
    list_per_page = 10



class home_courseadmin(admin.ModelAdmin):
    list_display = ('title','instructor','image','Free')
    list_display_links = ('title','instructor')
    search_fields = ('title','instructor')
    list_per_page = 10
    list_editable = ('Free',)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(faculty,facultyadmin)
admin.site.register(testimonial,testimonialadmin)
admin.site.register(about)
admin.site.register(blog,blogadmin)
admin.site.register(contact,contactadmin)
admin.site.register(jobform,jobformadmin)
admin.site.register(home_course,home_courseadmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Lecture)


