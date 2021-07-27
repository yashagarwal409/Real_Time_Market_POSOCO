from buyer.views import schedule
from django.contrib import admin
from .models import ClearEntityDown, ClearEntityUp, ClearedReserveDown, ClearedReserveUp, Declaration, Reserve, Schedule, TimeBlock, UpReserve
admin.site.register(Reserve)
admin.site.register(UpReserve)
admin.site.register(ClearedReserveUp)
admin.site.register(ClearEntityUp)
admin.site.register(ClearedReserveDown)
admin.site.register(ClearEntityDown)
admin.site.register(TimeBlock)
admin.site.register(Declaration)
admin.site.register(Schedule)
# Register your models here.
