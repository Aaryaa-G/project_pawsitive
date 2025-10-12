from django.db import models

class Donation(models.Model):
    email_id = models.EmailField()
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    payment_screenshot = models.ImageField(upload_to='payment/')

    def __str__(self):
        return self.name

class Adoption(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    adults = models.IntegerField()
    children = models.IntegerField()
    allergy = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')])
    agreement = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])
    time_for_pet = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')])
    experience = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])
    pet_name = models.CharField(max_length=100)
    pet_gender = models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=12)
    consent_form = models.FileField(upload_to='consents/')
    regular_updates = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')])
    pet_photo = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.pet_name


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    member_type = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=100)
    residence = models.CharField(max_length=20)
    experience_with_animals = models.BooleanField()
    volunteer_areas = models.TextField()
    reason_for_volunteering = models.TextField()

    def __str__(self):
        return self.name

class PreAdoption(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    dog_name = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='uploads/pet_photos/', blank=True, null=True)
    owned_pets = models.BooleanField()
    other_pets = models.BooleanField()
    schedule = models.TextField()
    financially_prepared = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"