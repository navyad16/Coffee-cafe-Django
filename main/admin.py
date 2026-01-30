from django.contrib import admin
from .models import MenuItem, ContactMessage,Order, OrderItem, Reservation

admin.site.register(MenuItem)
admin.site.register(ContactMessage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Reservation)
