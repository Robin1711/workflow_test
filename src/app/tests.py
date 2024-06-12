from django.test import TestCase
from app.models import User, Post
from datetime import datetime
import pytz

# Create your tests here.
class TestAppModels(TestCase):
    def test_model_str(self):
        user_obj = User.objects.create(name="Robin", date_of_birth=datetime(1995, 11, 17, 0, 0, 0, tzinfo=pytz.timezone('Europe/Amsterdam')), email="r.som@mer.net", address="Hardewiker")
        post_obj = Post.objects.create(title="Django Testing", content='Hello World!', posted_by=user_obj)
        self.assertEqual(post_obj.posted_by.name, "Robin")
