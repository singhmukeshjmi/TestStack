from django.forms import ValidationError
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect

from django.conf import settings
#from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Project
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import *
from .serializers import *
# Create your views here.
from .filters import *




def index(request):
    return render(request, "index.html")
def home(request):
    subject = 'django try mail'
    message = f'Try mail'
    email_from = settings.EMAIL_HOST_USER
    print(email_from)
    recipient_list = ['faltukaam597@gmail.com']
    #send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("home")


def trytry(request):
    return render(request, 'registration/password_reset_confirm.html')
    #return render(request, 'admin/app_list.html')

def form(request):
    if request.method == 'POST':
        form = testcasesForm(request.POST)
        if form.is_valid:
            print(form)
            form.save()
        else:
            print("Not valid")
        return render(request, "form.html", {'form' : form})
    form = testcasesForm()
    return render(request, "form.html", {'form' : form})

def base(request):
    return render(request, 'base.html')
















@login_required
def homepage(request):
    return render(request, 'homepage.html')
def userregistrationpage(request):
    return HttpResponse('userregistrationpage<br><h1><a href="/"> Back</a></h2>')
def userloginpage(request):
    return HttpResponse('userloginpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def userprofilepage(request):
    return HttpResponse('userprofilepage<br><h1><a href="/"> Back</a></h2>')
@login_required
def usermanagementpage(request):
    return HttpResponse('usermanagementpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def projectcreationpage(request):
    return render(request, 'projectcreationpage.html')
from django.views import View
class ProjectCreateView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'projectcreationpage.html', {'form':form})
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            project_type = form.cleaned_data['project_type']
            projectobject = Project(name=name, description=description, project_type=project_type, created_by=request.user)
            projectobject.save()
            print(projectobject.id)
            return redirect('projecteditingpage',projectobject.id)
        else:
            return HttpResponse('form not valid')

class ProjectEditView(View):
   def get(self, request, pk):
        inst=Project.objects.get(id=pk)
        form = ProjectForm(instance=inst)
        return render(request, 'projectcreationpage.html', {'form':form})
   def post(self, request, pk):
        form = ProjectForm(request.POST)
        if form.is_valid():
            projectobject = Project.objects.get(id=pk)
            projectobject.name = form.cleaned_data['name']
            projectobject.description = form.cleaned_data['description']
            projectobject.project_type = form.cleaned_data['project_type']
            projectobject.save()
            return render(request, 'projectcreationpage.html', {'form':form})

class ProjectOverview(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'projectsoverview.html', {'projects':projects})
        

@login_required
def projectassignmentpage(request):
    return render(request, 'projectassignmentpage.html')
@login_required
def projectstatustrackingpage(request):
    return HttpResponse('projectstatustrackingpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def testcaseassignmentpage(request):
    return HttpResponse('testcaseassignmentpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def testcaseexecutionpage(request):
    return HttpResponse('testcaseexecutionpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def testcasestatustrackingpage(request):
    return HttpResponse('testcasestatustrackingpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def testexecutionassignmentpage(request):
    return HttpResponse('testexecutionassignmentpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def testexecutionstatustrackingpage(request):
    return HttpResponse('testexecutionstatustrackingpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def testcaseexecutionreportspage(request):
    return HttpResponse('testcaseexecutionreportspage<br><h1><a href="/"> Back</a></h2>')
@login_required
def testexecutionreportspage(request):
    return HttpResponse('testexecutionreportspage<br><h1><a href="/"> Back</a></h2>')
@login_required
def summaryreportspage(request):
    return HttpResponse('summaryreportspage<br><h1><a href="/"> Back</a></h2>')
@login_required
def systemconfigurationpage(request):
    return HttpResponse('systemconfigurationpage<br><h1><a href="/"> Back</a></h2>')
@login_required
def administrationpage(request):
    return HttpResponse('administrationpage<br> <input type=button value="Previous Page" onClick="javascript:history.go(-1);">')
@login_required
def helpandsupportpage(request):
    return HttpResponse('helpandsupportpage<br><h1> <input type=button value="Previous Page" onClick="javascript:history.go(-1);"></h2>')




class TestCaseCreateView(View):
    def get(self, request):
        form = TestCaseForm()
        return render(request, 'testcasecreationpage.html', {'form':form})
    def post(self, request):
        form = TestCaseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project = form.cleaned_data['project']
            description = form.cleaned_data['description']
            testcase_type = form.cleaned_data['testcase_type']
            steps_to_run = form.cleaned_data['steps_to_run']
            expected_outcome = form.cleaned_data['expected_outcome']
            testcaseobject = TestCase(name=name, project=project, description=description,steps_to_run=steps_to_run, expected_outcome=expected_outcome, testcase_type=testcase_type, created_by=request.user)
            testcaseobject.save()
            #print(testcaseobject.id)
            return redirect('testcaseeditingpage',testcaseobject.id)
        else:
            return HttpResponse('form not valid')

class TestCaseEditView(View):
   def get(self, request, pk):
        inst=TestCase.objects.get(id=pk)
        form = TestCaseForm(instance=inst)
        return render(request, 'testcasecreationpage.html', {'form':form})
   def post(self, request, pk):
        form = TestCaseForm(request.POST)
        if form.is_valid():
            testcaseobject = TestCase.objects.get(id=pk)
            testcaseobject.name = form.cleaned_data['name']
            testcaseobject.project = form.cleaned_data['project']
            testcaseobject.description = form.cleaned_data['description']
            testcaseobject.testcase_type = form.cleaned_data['testcase_type']
            testcaseobject.steps_to_run = form.cleaned_data['steps_to_run']
            testcaseobject.expected_outcome = form.cleaned_data['expected_outcome']
            testcaseobject.save()
            return render(request, 'testcasecreationpage.html', {'form':form})

class TestCaseOverview(View):
    def get(self, request):
        querydict = {}
        if request.GET.get('project') and request.GET.get('project') != '':
            querydict['project']=request.GET.get('project')
        if request.GET.get('created_by') and request.GET.get('created_by') != '':
            querydict['created_by']=request.GET.get('created_by')
        if request.GET.get('testcase_type') and request.GET.get('testcase_type') != '':
            querydict['testcase_type']=request.GET.get('testcase_type')
        testcases = TestCase.objects.filter(**querydict)
        projectoptions = Project.objects.filter(pk__in=TestCase.objects.values_list('project', flat=True).distinct())
        created_by_options = User.objects.filter(pk__in=TestCase.objects.values_list('created_by', flat=True).distinct())
        testcase_type_options = TestCase.objects.values_list('testcase_type', flat=True).distinct()
        filteroptions={
            'projectoptions':projectoptions,
            'created_by_options':created_by_options,
            'testcase_type_options':testcase_type_options
        }
        print(filteroptions)
        filterform = TestCaseFilter(request.GET, queryset=TestCase.objects.all())
        return render(request, 'testcasesoverview.html', {'testcases':testcases, 'filteroptions':filteroptions, 'filterform':filterform})


from django.http import JsonResponse
def apitry(request):
    return JsonResponse({"name":"tfghj","comp":"ftghjkl"})




class BugCreateView(View):
    def get(self, request):
        form = BugForm()
        return render(request, 'bugcreationpage.html', {'form':form})
    def post(self, request):
        form = BugForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project = form.cleaned_data['project']
            testcase = form.cleaned_data['testcase']
            description = form.cleaned_data['description']
            steps_to_reproduce = form.cleaned_data['steps_to_reproduce']
            bug_category = form.cleaned_data['bug_category']
            bugobject = Bug(name=name, project=project, testcase=testcase, description=description,steps_to_reproduce=steps_to_reproduce, bug_category=bug_category, created_by=request.user)
            bugobject.save()
            print(bugobject.id)
            return redirect('bugeditingpage',bugobject.id)
        else:
            return HttpResponse('form not valid')

class BugEditView(View):
   def get(self, request, pk):
        # print(request.user.id)
        inst=Bug.objects.get(id=pk)
        print(request.META.get('REMOTE_ADDR'))
        form = BugForm(instance=inst)
        commentform = BugCommentsForm()
        comments = BugComments.objects.filter(bug=inst)
        return render(request, 'bugcreationpage.html', {'form':form, 'comments':comments, 'commentform': commentform})
   def post(self, request, pk):
        if request.POST.get('comment_delete'):
            print('Yo')
            comment_delete = BugComments.objects.get(sno=request.POST.get('comment_delete'))
            comment_delete.delete()


        elif request.POST.get('comment'):
            user = User.objects.get(id=request.user.id)
            comment = request.POST.get('comment')
            bug = Bug.objects.get(id=request.POST.get('bug'))
            # if commentform.cleaned_data['primary']:
            #     primary = BugComments.objects.get(id=commentform.cleaned_data['primary'].id)
            #     commentobject=BugComments(user=user, comment=comment, bug=bug, primary=primary)
            # else:
            commentobject=BugComments(user=user, comment=comment, bug=bug)
            print(commentobject)
            commentobject.save()

        
        elif request.POST.get('bug_category'):
            bugobject = Bug.objects.get(id=pk)
            bugobject.name = request.POST.get('name')
            bugobject.project = Project.objects.get(id=request.POST.get('project'))
            bugobject.testcase = TestCase.objects.get(id=request.POST.get('testcase'))
            bugobject.description = request.POST.get('description')
            bugobject.steps_to_reproduce = request.POST.get('steps_to_reproduce')
            bugobject.bug_category = request.POST.get('bug_category')
            bugobject.save()
        commentform = BugCommentsForm()
        comments = BugComments.objects.filter(bug=Bug.objects.get(id=pk))
        form = BugForm(instance=Bug.objects.get(id=pk))
        return render(request, 'bugcreationpage.html', {'form':form, 'comments':comments, 'commentform': commentform})

class BugOverview(View):
    def get(self, request):
        bugs = Bug.objects.all()
        return render(request, 'bugsoverviewpage.html', {'bugs':bugs})









class HtmlCreateView(View):
    def get(self, request):
        form = HtmlFormtry()
        return render(request, 'bugcreationpage.html', {'form':form})
    def post(self, request):
        form = HtmlFormtry(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            Htmlobject = Htmlfieldtry(name=name, desc=desc)
            Htmlobject.save()
            print(Htmlobject.id)
            return redirect('bugeditingpage',Htmlobject.id)
        else:
            return HttpResponse('form not valid')

class HtmlEditView(View):
   def get(self, request, pk):
        inst=Htmlfieldtry.objects.get(id=pk)
        form = HtmlFormtry(instance=inst)
        return render(request, 'bugcreationpage.html', {'form':form})
   def post(self, request, pk):
        form = HtmlFormtry(request.POST)
        if form.is_valid():
            Htmlobject = Htmlfieldtry.objects.get(id=pk)
            Htmlobject.name = form.cleaned_data['name']
            Htmlobject.desc = form.cleaned_data['desc']
            Htmlobject.save()
            return render(request, 'bugcreationpage.html', {'form':form})
