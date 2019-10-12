from django.contrib import admin
#后台用户名： lishiqiang
# Register your models here.

from .models import Food_info, Drinks_info, user_info, Order
admin.site.register(Food_info)
admin.site.register(Drinks_info)
admin.site.register(user_info)
admin.site.register(Order)