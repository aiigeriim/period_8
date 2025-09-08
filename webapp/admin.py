from django.contrib import admin
from webapp.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'summary')
    list_display_links = ( 'id', 'summary')
    search_fields = ('summary',)
    fields = ('summary', 'status', 'type', 'description')
    readonly_fields = ('id', 'created_at', 'updated_at')

class StatusAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name')
    list_display_links = ( 'id', 'name')


class TypeAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name')
    list_display_links = ('id', 'name')




admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)




