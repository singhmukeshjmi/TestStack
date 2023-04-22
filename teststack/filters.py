import django_filters as filters
from .models import *

class TestCaseFilter(filters.FilterSet):
    # name = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = TestCase
        fields = ['project', 'created_by', 'testcase_type']

class BugFilter(filters.FilterSet):

    class Meta:
        model = Bug
        fields = ['project', 'testcase', 'created_at', 'created_by', 'bug_category']


class Project(filters.FilterSet):

    class Meta:
        model = Project
        fields = ['created_at', 'created_by', 'project_type', 'project_status']