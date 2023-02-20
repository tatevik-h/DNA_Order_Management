from django.test import TestCase
from django.urls import reverse
from users.models import User
from orders.models import DNASynthesisOrder
from orders.forms import GeneSequenceForm


class DNASynthesisOrderViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('dna_synthesis_order')
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass')
        self.client.login(email='testuser@example.com', password='testpass')

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], GeneSequenceForm)

    def test_post_request_with_invalid_data(self):
        invalid_data = {'gene_sequence': 'ATC', 'valid_gene_sequences': '', 'invalid_gene_sequences': 'ATC'}
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(DNASynthesisOrder.objects.filter(gene_sequence='ATC').exists())
        self.assertIsInstance(response.context['form'], GeneSequenceForm)


class DNASynthesisResultViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass')
        self.order = DNASynthesisOrder.objects.create(user=self.user, gene_sequence='ATCG', valid_gene_sequences='ATCG', invalid_gene_sequences='')
        self.url = reverse('dna_synthesis_result', kwargs={'order_id': self.order.id})
        self.client.login(email='testuser@example.com', password='testpass')

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['order'], self.order)
