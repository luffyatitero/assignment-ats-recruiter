from django.urls import path

from candidates.views import CandidateViewSet, CandidateSearchAPIView

# Django REST Framework URL routing
urlpatterns = [
    path('', CandidateViewSet.as_view({'get': 'list', 'post': 'create'}), name='candidate-list'),
    path('<int:pk>/', CandidateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='candidate-detail'),
    path('search/', CandidateSearchAPIView.as_view(), name='candidate-search'),
]