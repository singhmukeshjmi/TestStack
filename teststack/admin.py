from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','description','created_at','updated_at','created_by','ProjectType')


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('name','project','description','steps_to_run','expected_outcome','created_at','updated_at','created_by','testcase_type')


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('name','project','testcase','description','steps_to_reproduce','created_at','updated_at','created_by','bug_category')


from tinymce.widgets import TinyMCE
@admin.register(Htmlfieldtry)
class HtmlfieldAdmin(admin.ModelAdmin):
    list_display = ['name','desc']
    formfield_overrides = { models.TextField: {'widget': TinyMCE()} }


@admin.register(BugComments)
class BugCommentsAdmin(admin.ModelAdmin):
    list_display = ['sno','comment', 'user']
    formfield_overrides = { models.TextField: {'widget': TinyMCE()} }


@admin.register(TestCaseOutcome)
class TestCaseOutcomeAdmin(admin.ModelAdmin):
    list_display = ['id','testcase','iteration','outcome']