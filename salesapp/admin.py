from django.contrib import admin
from .models import product
admin.site.register(product)
from .models import client
admin.site.register(client)
from .models import order
admin.site.register(order)
# Register your models here.
