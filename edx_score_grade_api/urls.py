from django.conf.urls import include, patterns, url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = patterns(
    '',
    url(r'courses/(?P<course_id>.+)/users/(?P<user_id>[0-9]+)/blocks/(?P<block_id>.+)', views.CourseView.as_view(), name='course-user-block-grade'),
    url(r'courses/(?P<course_id>.+)/blocks/(?P<block_id>.+)/delete', views.CourseViewPurge.as_view(), name='course-list-user-block-grade-delete'),
    url(r'courses/(?P<course_id>.+)', views.CourseViewList.as_view(), name='course-list-user-block-grade')
)
