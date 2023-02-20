from django.views import View
from django.shortcuts import render, redirect

from .forms import GeneSequenceForm
from .models import DNASynthesisOrder


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


class DNASynthesisResultView(View):
    def get(self, request, order_id):
        # Retrieve the order
        order = DNASynthesisOrder.objects.get(id=order_id)

        context = {'order': order}
        return render(request, 'dna_synthesis_result.html', context)
