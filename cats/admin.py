from django.contrib import admin
from .models import Cat, Owner, Toy, Achievement

# Register your models here.
admin.site.register(Cat)
admin.site.register(Owner)
admin.site.register(Toy)
admin.site.register(Achievement)