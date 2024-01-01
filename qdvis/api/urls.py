from api.views import CheckGpuAPIView, SampleAPIView, XyGraphAPIView
from django.urls import path

urlpatterns = [
    path("sample/", SampleAPIView.as_view(), name="sample"),
    path("xy_graph/", XyGraphAPIView.as_view()),
    path("gpu/", CheckGpuAPIView.as_view()),
]
