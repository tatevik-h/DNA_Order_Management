from django.db import models

from users.models import User, Organization


class RegularDNAProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_restricted = models.BooleanField(default=False)
    restricted_to = models.ManyToManyField(Organization, blank=True)


class DNASynthesisOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gene_sequence = models.JSONField()
    status = models.CharField(
        max_length=20,
        choices=[('complete', 'Complete'), ('incomplete', 'Incomplete')],
        default='incomplete'
    )
    valid_gene_sequences = models.CharField(max_length=255)
    invalid_gene_sequences = models.CharField(max_length=255)

    def __str__(self):
        return f"DNA Synthesis Order {self.id}"
