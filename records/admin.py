from django.contrib import admin
from records.models import *

admin.site.register(Person)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Visit)
admin.site.register(TestType)
admin.site.register(TestField)
admin.site.register(BooleanTestField)
admin.site.register(NumericTestField)
admin.site.register(NumericResult)
admin.site.register(BooleanResult)
admin.site.register(Range)
admin.site.register(Category)
