from django.contrib import admin
from records.models import *

admin.site.register(Person)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Visit)
admin.site.register(Medicine)
admin.site.register(Test)
admin.site.register(Report)
admin.site.register(WorkingHour)

