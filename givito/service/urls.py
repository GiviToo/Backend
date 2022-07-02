from django.urls import path

from givito.service.views import CategoriesView, ProjectDetailView, ProjectView, RegistrantDetailView, RegistrantView


urlpatterns = [
    path('project/', ProjectView.as_view(), name="project_list"),
    path('project/categories/', CategoriesView.as_view(), name="categories_view"),
    path('project/<uuid>/', ProjectDetailView.as_view(), name="project_detail"),
    path('registrant/', RegistrantView.as_view(), name="registrant_list"),
    path('registrant/<uuid>/', RegistrantDetailView.as_view(), name="registrant_detail"),
]
