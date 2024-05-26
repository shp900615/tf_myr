from django.db import models


class Facilities(models.Model):
    facility_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.facility_name

class FacilityToken(models.Model):
    facility = models.OneToOneField(Facilities, on_delete=models.CASCADE)
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.facility.facility_name

    
class raw_crh_patient_diagnosis(models.Model):
    visit_no = models.CharField(max_length=100)
    clinic = models.CharField(max_length=100)
    diagnosis_name = models.CharField(max_length=100)
    location = models.CharField(max_length = 100)
    syc_month_year = models.CharField(max_length=10)
    facility_code = models.CharField(max_length=100)

class raw_crh_patient_services(models.Model):
    visit_no = models.CharField(max_length=100)
    bill_no = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    item_name = models.CharField(max_length= 500)
    amount = models.FloatField()
    payment_category = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    syc_month_year = models.CharField(max_length=10)
    facility_code = models.CharField(max_length=100)

class raw_hrm_patient_dignosis(models.Model):
    visit_no = models.CharField(max_length=100)
    clinic = models.CharField(max_length=100)
    diagnosis_name = models.CharField(max_length=100)
    location = models.CharField(max_length = 100)
    syc_month_year = models.CharField(max_length=10)
    facility_code = models.CharField(max_length=100)

class raw_hrm_patient_services(models.Model):
    visit_no = models.CharField(max_length=100)
    bill_no = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    item_name = models.CharField(max_length= 500)
    amount = models.FloatField()
    payment_category = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    syc_month_year = models.CharField(max_length=10)
    facility_code = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name

    