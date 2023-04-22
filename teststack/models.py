from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ProjectType = [
        ('Sanity testing', 'Sanity testing'),
        ('testing', 'testing'),
        ('overview/checking', 'overview/checking'),
        ('Not related to product quality', 'Not related to product quality'),
    ]
    project_type = models.CharField(max_length = 50, choices = ProjectType, default = '1')
    ProjectStatus = [
        ('Not started', 'Not started'),
        ('Under investigation / testcase creation', 'Under investigation / testcase creation'),
        ('Under testing', 'Under testing'),
        ('Tested', 'Tested'),
        ('Sent for fixation', 'Sent for fixation'),
        ('Ready for Launch with some known bugs', 'Ready for Launch with some known bugs'),
        ('Ready for Launch', 'Ready for Launch'),
    ]
    project_status = models.CharField(max_length = 50, choices = ProjectStatus, default = 'Not started')
    def __str__(self):
        return self.name


class TestCase(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    description = HTMLField()
    steps_to_run = models.TextField()
    expected_outcome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    TestCaseType = [
        ('functional case', 'functional case'),
        ('UI case', 'UI case'),
        ('edge case', 'edge case'),
        ('simple case', 'simple case'),
    ]
    testcase_type = models.CharField(max_length = 50, choices = TestCaseType, default = '1')
    def __str__(self):
        return self.name


class Bug(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    testcase = models.ForeignKey(TestCase, on_delete=models.SET_NULL, null=True)
    description = HTMLField()
    steps_to_reproduce = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    BugCategory = [
        ('Critical', 'Critical'),
        ('Blocker', 'Blocker'),
        ('Non Critical', 'Non Critical'),
        ('Undecided', 'Undecided'),
    ]
    bug_category = models.CharField(max_length = 50, choices = BugCategory, default = 'Undecided')
    def __str__(self):
        return self.name


# class BugAssignee(models.Model):
#     bug = models.ForeignKey(Bug, on_delete=models.CASCADE)


class Htmlfieldtry(models.Model):
    name = models.CharField(max_length=100)
    desc = HTMLField()



class BugComments(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = HTMLField()
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class TestCaseOutcome(models.Model):
    id = models.AutoField(primary_key=True)
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    iteration = models.PositiveIntegerField()
    tested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='Assignee')
    bug = models.ForeignKey(Bug, on_delete=models.SET_NULL, null=True, blank=True)
    outcome_state = [
        ('Untested', 'Untested'),
        ('passed', 'Passed'),
        ('failed', 'Failed'),
        ('failed but ignorable', 'Failed but Ignorable'),
        ('comment awaited', 'Comment Awaited'),
    ]
    outcome = models.CharField(max_length = 50, choices = outcome_state, default = 'Untested')
    class Meta:
        unique_together = (
            ("testcase", "iteration"),
        )
