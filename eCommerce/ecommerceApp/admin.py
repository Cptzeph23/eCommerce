from django.contrib import admin
from .models import Contact, Profile, NewUser, Member

# Register your models here.

admin.site.register(Contact)
admin.site.register(Profile)

admin.site.register(NewUser)
admin.site.register(Member)




