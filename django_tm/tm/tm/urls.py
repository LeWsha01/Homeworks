from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from dashboard import views
from authentication import views as auth_views
from dashboard import api_views as dashboard_api

router = routers.DefaultRouter()
router.register(r'projects/', dashboard_api.ProjectViewSet)
router.register(r'issue/', dashboard_api.IssueViewSet)

urlpatterns = [

    path(
        '', include(router.urls)
    ),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')
    ),
    path(
        'admin/', admin.site.urls
    ),
    path(
        'about/',
        views.AboutView.as_view(),
        name='about.html'
    ),
    #projects
    path(
        'about/<str:page>/',
        views.dynamic_template_view
    ),
    path(
        'projects/',
        views.ProjectListView.as_view(),
        name='projects-list'
    ),
    path(
        'projects/<int:pk>/',
        views.ProjectDetailView.as_view(),
        name='projects-detail'
    ),
    path(
        'projects/create/',
        views.ProjectCreateView.as_view(),
        name='projects-create'
    ),
    path(
        'projects/<int:pk>/update/',
        views.ProjectUpdateView.as_view(),
        name='projects-update'
    ),
    path(
        'projects/<int:pk>/delete/',
        views.ProjectDeleteView.as_view(),
        name='projects-delete'
    ),
    # issues
    path(
        'issues/issuecreate/',
        views.IssueCreate.as_view(),
        name='issue-create'
    ),
    path(
        'issues/',
        views.IssuesListView.as_view(),
        name='issues-list'
    ),
    path(
        'issues/<int:pk>/',
        views.IssueDetailView.as_view(),
        name='issue-detail'
    ),
    path(
        'issues/<int:pk>/update/',
        views.IssueUpdateView.as_view(),
        name='issue-update'
    ),
    path(
        'issues/<int:pk>/delete/',
        views.IssueDeleteView.as_view(),
        name='issue-delete'
    ),
    # authification
    path(
        'contact-us/',
        views.ContactUsView.as_view(),
        name='contact-us'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),
    path(
        'signup/',
        auth_views.SignUp.as_view(),
        name='sign-up'
    )
]
