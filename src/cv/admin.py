from django.contrib import admin

from .forms import BasicInfoForm
from .models import (
    BasicInfo,
    Education,
    WorkExperience,
    Certification,
    Reason,
    Question,
    ExtraInfo,
    CV,
    CVTemplate,
)


class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'updated', 'created']
    form  = BasicInfoForm


admin.site.register(BasicInfo, BasicInfoAdmin)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Certification)
admin.site.register(Reason)
admin.site.register(Question)
admin.site.register(ExtraInfo)
admin.site.register(CV)
admin.site.register(CVTemplate)
