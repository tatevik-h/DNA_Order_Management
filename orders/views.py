from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import GeneSequenceForm
from .models import DNASynthesisOrder


@method_decorator(login_required, name='dispatch')
class DNASynthesisOrderView(View):
    def get(self, request):
        form = GeneSequenceForm()
        context = {'form': form}
        return render(request, 'dna_synthesis_order.html', context)

    def post(self, request):
        form = GeneSequenceForm(request.POST)
        if form.is_valid():
            # Save the order
            order = DNASynthesisOrder(user=request.user, gene_sequence=form.cleaned_data['gene_sequence'],
                                      valid_gene_sequences=form.cleaned_data['valid_gene_sequences'],
                                      invalid_gene_sequences=form.cleaned_data['invalid_gene_sequences'])
            order.save()

            # Show the result
            return redirect('dna_synthesis_result', order_id=order.id)

        context = {'form': form}
        return render(request, 'dna_synthesis_order.html', context)


@method_decorator(login_required, name='dispatch')
class DNASynthesisResultView(View):
    def get(self, request, order_id):
        # Retrieve the order
        order = DNASynthesisOrder.objects.get(id=order_id)

        context = {'order': order}
        return render(request, 'dna_synthesis_result.html', context)
