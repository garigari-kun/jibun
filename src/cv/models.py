from django.db import models
from django import forms


class BasicInfo(models.Model):

    SEX_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )

    # user field should be here
    full_name = models.CharField(max_length = 64)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    full_name_kana = models.CharField(max_length = 64)
    first_name_kana = models.CharField(max_length = 32)
    last_name_kana = models.CharField(max_length = 32)
    sex = models.CharField(max_length = 1, choices = SEX_CHOICES)
    birth_date = models.DateField()
    age = models.CharField(max_length = 3)
    zip_code = models.CharField(max_length = 12)
    address = models.CharField(max_length = 128)
    address2 = models.CharField(max_length = 128)
    address_kana = models.CharField(max_length = 128)
    address2_kana = models.CharField(max_length = 128)
    phone_number = models.CharField(max_length = 32)
    cellphone_number = models.CharField(max_length = 32)
    email = models.EmailField()
    created = models.DateTimeField(auto_now = False, auto_now_add = True)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return 'ID {}: {} {}'.format(self.id, self.first_name, self.last_name)

class Education(models.Model):
    STATUS = (
        ('e', '入学'),
        ('g', '卒業'),
        ('d', '中途退学'),
        ('t', '編入'),
        ('m', '転入'),
        ('l', '休学'),
    )

    school_name = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length = 10, choices = STATUS)

    def __str__(self):
        return self.school_name


class WorkExperience(models.Model):
    STATUS = (
        ('e', '入社'),
        ('q', '退社'),
    )

    company_name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length = 10, choices = STATUS)

    def __str__(self):
        return self.company_name


class Certification(models.Model):
    title = models.CharField(max_length = 120)
    acquired_date = models.DateField()

    def __str__(self):
        return self.title

class Reason(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.id

class Question(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.id

class ExtraInfo(models.Model):

    SPOUSE_CHOICES = (
        ('y', '有'),
        ('n', '無'),
    )

    DUTY_OF_SUPPORT_CHOICES = (
        ('y', '有'),
        ('n', '無'),
    )

    commuting_time = models.CharField(max_length = 12)
    dependent = models.IntegerField()
    spouse = models.CharField(
        max_length = 1,
        choices = SPOUSE_CHOICES
    )
    duty_of_support = models.CharField(
        max_length = 1,
        choices = DUTY_OF_SUPPORT_CHOICES
    )

    def __str__(self):
        return self.id

class CV(models.Model):
    basic_info = models.ForeignKey(BasicInfo)
    education = models.ManyToManyField(Education)
    work_experience = models.ManyToManyField(WorkExperience)
    certification = models.ManyToManyField(Certification)
    reason = models.ForeignKey(Reason)
    qustion = models.ForeignKey(Question)
    extra_info = models.ForeignKey(ExtraInfo)

class CVTemplate(models.Model):
    basic_info = models.ForeignKey(BasicInfo)
    education = models.ManyToManyField(Education)
    work_experience = models.ManyToManyField(WorkExperience)
    certification = models.ManyToManyField(Certification)
