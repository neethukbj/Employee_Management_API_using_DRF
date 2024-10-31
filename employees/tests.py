from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Employee
from django.contrib.auth.models import User

class EmployeeAPITests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(
            name="Alice Johnson",
            email="alice.johnson@example.com",
            department="HR",
            role="MANAGER"
        )

    def test_list_employees(self):
        response = self.client.get(reverse('employee-list-create'))
        print(response.data)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Alice Johnson")

    def test_create_employee(self):
        response = self.client.post(reverse('employee-list-create'), {
            "name": "Bob Smith",
            "email": "bob.smith@example.com",
            "department": "ENGINEER",
            "role": "DEVELOPER"
        })
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_create_employee_with_existing_email(self):
        response = self.client.post(reverse('employee-list-create'), {
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "department": "HR",
            "role": "MANAGER"
        })
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This email is already in use..!", response.data['email'])

    def test_create_employee_with_invalid_department(self):
        response = self.client.post(reverse('employee-list-create'), {
            "name": "Charlie Brown",
            "email": "charlie.brown@example.com",
            "department": "INVALID_DEPT",
            "role": "DEVELOPER"
        })
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('"INVALID_DEPT" is not a valid choice.', str(response.data))

    def test_retrieve_employee(self):
        response = self.client.get(reverse('employee-detail', kwargs={'pk': self.employee.pk}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.employee.name)

    def test_update_employee(self):
        response = self.client.patch(reverse('employee-detail', kwargs={'pk': self.employee.pk}), {
            "role": "ANALYST"
        })
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.role, "ANALYST")

    def test_delete_employee(self):
        response = self.client.delete(reverse('employee-detail', kwargs={'pk': self.employee.pk}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)
