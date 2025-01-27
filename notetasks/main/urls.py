from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, TaskViewSet, MainPageView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', MainPageView.as_view(), name='mainpage'),
    ]
