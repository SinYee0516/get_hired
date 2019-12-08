from django.contrib import admin
from .models import User, Job, Company, Status, Saved, Message

admin.site.register(User)
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Status)
admin.site.register(Saved)
admin.site.register(Message)

