from django.urls import path
from .views import DNASynthesisOrderView, DNASynthesisResultView

urlpatterns = [
    path('synthesis-order/', DNASynthesisOrderView.as_view(), name='dna_synthesis_order'),
    path('synthesis-result/<int:order_id>/', DNASynthesisResultView.as_view(), name='dna_synthesis_result'),
]
