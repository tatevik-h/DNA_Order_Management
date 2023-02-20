from django.shortcuts import render

from .forms import GeneSequenceForm
from .models import DNASynthesisOrder


def dna_synthesis_order(request):
    if request.method == 'POST':
        form = GeneSequenceForm(request.POST)
        if form.is_valid():
            # Save the order
            order = DNASynthesisOrder(user=request.user, gene_sequence=form.cleaned_data['gene_sequence'],
                                      valid_gene_sequences=form.cleaned_data['valid_gene_sequences'],
                                      invalid_gene_sequences=form.cleaned_data['invalid_gene_sequences'])
            order.save()

            # Show the result
            context = {'order': order}
            return render(request, 'dna_synthesis_result.html', context)
    else:
        form = GeneSequenceForm()

    context = {'form': form}
    return render(request, 'dna_synthesis_order.html', context)
