from django.contrib import admin
from .models import ClearEntityDown, ClearEntityUp, ClearedReserveDown, ClearedReserveUp, Reserve, TimeBlock, UpReserve
admin.site.register(Reserve)
admin.site.register(UpReserve)
admin.site.register(ClearedReserveUp)
admin.site.register(ClearEntityUp)
admin.site.register(ClearedReserveDown)
admin.site.register(ClearEntityDown)
admin.site.register(TimeBlock)
# Register your models here.
