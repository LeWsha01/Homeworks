from django import http, urls
from django import template
from django import shortcuts
from django.views import generic
from dashboard import models, forms
from django.contrib.auth import models as auth_models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

def dynamic_template_view(request, page):
    try:
        return shortcuts.render(request, f'about/{page}.html')
    except template.TemplateDoesNotExist:
        raise http.Http404()


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = models.Project
    template_name = 'project_list.html'
    paginate_by = 1

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Developer').exists():
            return user.project.all()
        return models.Project.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count'] = models.Project.objects.count()
        return context_data


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = context['object'].issue_set.all()
        return context


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Project
    fields = [
        'name',
        'description',
    ]
    template_name = 'project_create.html'


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Project
    fields = [
        'name',
        'description',
    ]
    template_name = 'project_update.html'


class ProjectDeleteView(generic.DeleteView):
    model = models.Project
    success_url = urls.reverse_lazy('projects-list')
    template_name = 'project_delete.html'




class IssueCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Issue
    fields = [
        'name',
        'description',
        'created_at',
        'deadline',
        'reported',
        'assigne',
        'project',
    ]
    template_name = 'issue_create.html'


class IssueDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Issue
    template_name = 'issue_detail.html'


class IssueUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Issue
    fields = [
        'name',
        'description',
        'created_at',
        'deadline',
        'reported',
        'assigne',
        'project',
    ]
    template_name = 'issue_update.html'


class IssueDeleteView(generic.DeleteView):
    model = models.Issue
    success_url = urls.reverse_lazy('issues-list')
    template_name = 'issue_delete.html'


class IssuesListView(LoginRequiredMixin, generic.ListView):
    model = models.Issue
    template_name = 'issue_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Issue.objects.all()


class ContactUsView(generic.FormView):
    form_class = forms.ConstuctUsForm
    template_name = 'contact_us.html'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        recipients = [form.cleaned_data['email']]
        # send_mail(subject, message, sender, recipients)
        return http.HttpResponseRedirect('/projects/')
