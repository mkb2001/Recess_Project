from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentDetails, name='home'),
    path('course', views.course, name='course'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('courses', views.courses, name='courses'),
    path('facilities', views.facilities, name='facilities'),
    path('instructors', views.instructors, name='instructors'),
    path('signout', views.signout, name='sign_out'),
    path('signin', views.signin, name='sign_in'),
    path('signup', views.signup, name='sign_up'),
    path('profile', views.profile, name='profile'),
    path('instructor_feedback/', views.instructor_feedback, name='instructor'),
    path('instructor_feedbacks/<int:feedback_id>/delete/',
         views.delete_instructor_feedback, name='delete_instructor_feedback'),
     path('course_feedbacks/<int:feedback_id>/delete/',
         views.delete_course_feedback, name='delete_course_feedback'),
    path('facility_feedback/', views.facility, name='facility'),

]


