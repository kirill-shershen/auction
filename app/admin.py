from django.contrib import admin
from app.models import Animal, Lot, Bid, User


admin.site.register(Animal)
admin.site.register(Lot)
admin.site.register(Bid)
admin.site.register(User)