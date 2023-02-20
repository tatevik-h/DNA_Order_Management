from django.test import TestCase
from django.urls import reverse

from orders.forms import GeneSequenceForm
from orders.models import DNASynthesisOrder
from users.models import User


class DNASynthesisOrderTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass',
        )
        self.form_data = {
            'gene_sequence': 'ATCG',
            'valid_gene_sequences': 'ATCG',
            'invalid_gene_sequences': '',
        }

    def test_get_dna_synthesis_order(self):
        self.client.login(email='testuser@example.com', password='testpass')
        response = self.client.get(reverse('dna_synthesis_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dna_synthesis_order.html')
        self.assertIsInstance(response.context['form'], GeneSequenceForm)

    def test_post_valid_dna_synthesis_order(self):
        self.client.login(email='testuser@example.com', password='testpass')
        response = self.client.post(reverse('dna_synthesis_order'), self.form_data)
        self.assertRedirects(response, reverse('dna_synthesis_result'))
        self.assertEqual(DNASynthesisOrder.objects.count(), 1)

    def test_post_invalid_dna_synthesis_order(self):
        self.client.login(email='testuser@example.com', password='testpass')
        self.form_data['gene_sequence'] = 'ATCB'  # invalid sequence
        response = self.client.post(reverse('dna_synthesis_order'), self.form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dna_synthesis_order.html')
        self.assertContains(response, 'Enter a valid DNA sequence.')
        self.assertEqual(DNASynthesisOrder.objects.count(), 0)
