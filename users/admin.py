from django.contrib import admin
from users.models import User
# Register your models here.







class UserAdmin(admin.ModelAdmin):
     filter_horizontal=('following', ) 
     readonly_fields =('username',)
     fieldsets=(
        ('Dados pessoais', {'fields':('username', 'email','date_joined'),'classes': 'wide',}),
        ('Tuirer', { 'fields': ('following',),
        'description':'Coisas relacionadas ao system'})

    )



admin.site.register(User, UserAdmin)
# Register your models here.
