from django.test import TestCase
from.models import Teacher
import datetime
from.forms import TeacherForm
# Create your tests here.
class CreateTeacherTestCase(TestCase):
    def setUp(self):
        self.data={"first_name":"James",
            "last_name":"Mwai",
            "date_of_birth":datetime.date(1998,8,25),
            "registration_no":"123",
            "place_of_residence":"Nairobi",
            "phone_number":"123456789",
            "email":"james@akirachix.com",
            "id_number":1111111,
            "profession":"Consultant",}
        self.bad_data={"first_name":"Consolata",
            "last_name":"Akoth",
            "date_of_birth":datetime.date(1998,8,25),
            "registration_no":"",
            "place_of_residence":"Nairobi",
            "phone_number":"123456789",
            "email":"",
            "id_number":1111111,
            "profession":"Consultant",}
    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertFalse(form.is_valid())
    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())

