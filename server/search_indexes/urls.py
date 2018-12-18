from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .viewsets import BookDocumentView

router = DefaultRouter()
books = router.register(r'books',
                        BookDocumentView,
                        base_name='bookdocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]