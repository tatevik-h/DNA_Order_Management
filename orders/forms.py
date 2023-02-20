from django import forms
from django.core.exceptions import ValidationError


class GeneSequenceForm(forms.Form):
    gene_sequence = forms.JSONField()

    def clean_gene_sequence(self):
        gene_sequence = self.cleaned_data['gene_sequence']
        valid_count = 0
        invalid_count = 0

        # Check length, characters, and duplicates
        for seq in gene_sequence:
            if len(seq) < 300 or len(seq) > 5000:
                raise ValidationError('Gene sequence must be between 300 and 5000 characters.')
            if set(seq) - set(['A', 'T', 'G', 'C']):
                raise ValidationError('Gene sequence must contain only A, T, G, or C.')
            if gene_sequence.count(seq) > 1:
                raise ValidationError('Gene sequence cannot contain duplicates.')

            # Calculate GC ratio
            gc_ratio = (seq.count('G') + seq.count('C')) / len(seq)
            if gc_ratio < 0.25 or gc_ratio > 0.65:
                invalid_count += 1
            else:
                valid_count += 1

        self.cleaned_data['valid_gene_sequences'] = valid_count
        self.cleaned_data['invalid_gene_sequences'] = invalid_count
        return gene_sequence
