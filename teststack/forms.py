from django import forms
from .models import *
from datetime import datetime
from tinymce.widgets import TinyMCE



class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'htmlfield'})
    class Meta:
        model = Project
        fields = ['name', 'description', 'project_type']
    

class TestCaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'htmlfield'})
        self.fields['project'].required = False
    class Meta:
        model = TestCase
        fields = ['name','project','description','steps_to_run','expected_outcome','testcase_type']

class BugForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'htmlfield'})
        self.fields['project'].required = False
        self.fields['testcase'].required = False
    class Meta:
        model = Bug
        fields = ['name','project','testcase','description','steps_to_reproduce','bug_category']
        widgets =   {
                        'steps_to_reproduce':forms.Textarea(attrs={'rows':4}),
                    }


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    

class HtmlFormtry(forms.ModelForm):
    # content = forms.CharField(
    #     widget=TinyMCEWidget(
    #         attrs={'required': False, 'cols': 30, 'rows': 10}
    #     )
    # )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs.update({'class': 'htmlfield'})
    class Meta:
        model = Htmlfieldtry
        fields = ['name','desc']
        

class BugCommentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'htmlfield'})
    class Meta:
        model = BugComments
        fields = ['user', 'comment', 'bug', 'parent']