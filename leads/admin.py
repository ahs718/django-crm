from django.contrib import admin

from .models import Agent, Category, Lead, User, UserProfile

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)
