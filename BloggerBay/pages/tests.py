from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class ViewTests(SimpleTestCase):

	def test_view_index(self):
		response = self.client.get("/")
		set.assertEqual(response,)

	def check_template(self, page, template):
        response = self.client.get(page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name=template)

    def test_view_index(self):
        self.check_template('/', 'index.html')

    def test_view_prototype(self):
        #need prototypes

    def test_view_no_page(self):
        response = self.client.get('/home.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='missing.html')

    def test_view_missing_template(self):
        response = self.client.get('/xxx')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('missing.html')

    def test_view_bad_url(self):
        response = self.client.get('/xxx/home.html')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('missing.html')

class userTests(TestCase):


	def creat_test_user(self):
		#need login stuff