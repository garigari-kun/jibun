from datetime import datetime

from django import forms
from django.forms.extras import SelectDateWidget
from .models import (
    BasicInfo,
    Education,
    WorkExperience,
    Certification,
    Reason,
    Question,
    ExtraInfo,
)

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'school_name',
            'start_date',
            'end_date',
            'status',
        ]

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            'company_name',
            'title',
            'start_date',
            'end_date',
            'status',
        ]

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = [
            'title',
            'acquired_date',
        ]

class ReasonForm(forms.ModelForm):
    class Meta:
        model = Reason
        fields = [
            'content',
        ]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'content',
        ]

class ExtraInfoForm(forms.ModelForm):
    class Meta:
        model = ExtraInfo
        fields = [
            'commuting_time',
            'dependent',
            'spouse',
            'duty_of_support',
        ]

class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = [
            # 'first_name',
            # 'last_name',
            # 'first_name_kana',
            # 'last_name_kana',
            'full_name',
            'full_name_kana',
            'sex',
            'birth_date',
            'age',
            'zip_code',
            'address',
            'address2',
            'address_kana',
            'address2_kana',
            'phone_number',
            'cellphone_number',
            'email',
        ]

        now = datetime.now()

        widgets = {
            'birth_date': SelectDateWidget(years = range(1900, now.year)),
        }





    # now = datetime.now()
    # birth_date = forms.DateField(widget = extras.SelectDateWidget(years = range(1900, now.year)))
