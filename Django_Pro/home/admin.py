from django.contrib import admin
from django.http import HttpResponse
from .models import User,DeletedUser
import json
#from .models import DeletedRecord  #For Deleted Record page

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    actions = ['export_selected_as_json', 'mark_as_deleted']

    def mark_as_deleted(self, request, queryset):
        for user in queryset:
            DeletedUser.objects.create(
                name=user.name,
                email=user.email,
                password=user.password,
            )
            user.delete()  # Delete the user from the User table

    mark_as_deleted.short_description = "Mark selected users as deleted"

    def export_selected_as_json(self, request, queryset):
        data = []
        for item in queryset:
            data.append({
                'id': item.id,
                'name': item.name,
                'email': item.email,
                'password': item.password,
                # Add more fields as needed
            })

        response = HttpResponse(json.dumps(data, indent=4), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=data.json'
        return response

    export_selected_as_json.short_description = "Export selected records as JSON"

class DeletedUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    actions = ['export_selected_as_json']

    def export_selected_as_json(self, request, queryset):
        data = []
        for deleted_user in queryset:
            data.append({
                'id': deleted_user.id,
                'name': deleted_user.name,
                'email': deleted_user.email,
                'password': deleted_user.password,
                # Add more fields as needed
            })

        response = HttpResponse(json.dumps(data, indent=4), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=deleted_data.json'
        return response

    export_selected_as_json.short_description = "Export selected records as JSON"


admin.site.register(User, UserAdmin)
admin.site.register(DeletedUser, DeletedUserAdmin)

# Custom admin template
admin.site.index_template = 'admin/custom_adminbase.html'



#admin.site.register(User, UserAdmin)


