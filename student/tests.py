from django.test import TestCase
from .models import Student
import datetime
from .forms import StudentForm
from django.urls import reverse
from django.test import Client
client = Client()


class StudentTestCase(TestCase):
	"""docstring for Student TestCase"""
	def setUp(self):
		self.student=Student(
			first_name="Aziz",
			last_name="Akama",
			date_of_birth=datetime.date(1999,6,21),
			registration_number="1234XZ",
			email="akama@gmail.com",
			phone_number="123456",
			place_of_residence="Nairobi",
			guardian_phone="12345",
			id_number=123456,
			date_joined=datetime.date.today(),
			)

	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name, self.student.full_name())

	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name, self.student.full_name())

	def test_age_above_18(self):
		self.assertFalse(self.student.clean() < 18)

	def test_age_below_30(self):
		self.assertFalse( self.student.clean() > 30)
		
	
class CreateStudentTestCase(TestCase):
    def setUp(self):
        self.data={
            "first_name":"Aziz",
            "last_name":"Akama",
            "date_of_birth":datetime.date(1999,6,21),
            "registration_number":"1234XZ",
            "email":"akama@gmail.com",
            "phone_number":"123456",
            "place_of_residence":"Nairobi",
            "guardian_phone":"12345",
            "id_number":123456,
            "date_joined":datetime.date.today(),
            }

        self.bad_data={
            "first_name":"Aziz",
            "last_name":"Akama",
            "date_of_birth":datetime.date(1999,6,21),
            "registration_number":"1234XZ",
            "email":" ",
            "phone_number":"123456",
            "place_of_residence":"Nairobi",
            "guardian_phone":"12345",
            "id_number":123456,
            "date_joined":datetime.date.today(),
            }

    def test_student_form_accepts_valid_data(self):
    	form = StudentForm(self.data)
    	self.assertTrue(form. is_valid())

    def test_Student_form_rejects_invalid_data(self):
    	form = StudentForm(self.bad_data)
    	self.assertFalse(form. is_valid())

    def test_add_student_view(self):
        url = reverse("add_student")
        response=client.post(url,self.data)
        self.assertEqual(response.status_code,200)

    def test_reject_add_student_view(self):
        client = Client()
        url = reverse("add_student")
        response=client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)


# Create your tests here.
