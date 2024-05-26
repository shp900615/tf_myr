from django.contrib import admin

from .models import (Facilities, FacilityToken, raw_crh_patient_diagnosis,
                     raw_crh_patient_services, raw_hrm_patient_dignosis,
                     raw_hrm_patient_services)


@admin.register(Facilities)
class FacilityTokenAdmin(admin.ModelAdmin):
    list_display = ('id','facility_name',)
    search_fields = ('facility_name',)

@admin.register(FacilityToken)
class FacilityTokenAdmin(admin.ModelAdmin):
    list_display = ('facility', 'token', 'created_at')
    search_fields = ('facility',)

@admin.register(raw_crh_patient_diagnosis)
class RawCrhPatientDiagnosisAdmin(admin.ModelAdmin):
    list_display = ('visit_no', 'clinic', 'diagnosis_name', 'location', 'syc_month_year', 'facility_code')
    search_fields = ('visit_no', 'clinic', 'diagnosis_name')

@admin.register(raw_crh_patient_services)
class RawCrhPatientServicesAdmin(admin.ModelAdmin):
    list_display = ('visit_no', 'bill_no', 'department', 'item_name', 'amount', 'payment_category', 'payment_type', 'syc_month_year', 'facility_code')
    search_fields = ('visit_no', 'bill_no', 'department', 'item_name')

@admin.register(raw_hrm_patient_dignosis)
class RawHrmPatientDignosisAdmin(admin.ModelAdmin):
    list_display = ('visit_no', 'clinic', 'diagnosis_name', 'location', 'syc_month_year', 'facility_code')
    search_fields = ('visit_no', 'clinic', 'diagnosis_name')

@admin.register(raw_hrm_patient_services)
class RawHrmPatientServicesAdmin(admin.ModelAdmin):
    list_display = ('visit_no', 'bill_no', 'department', 'item_name', 'amount', 'payment_category', 'payment_type', 'syc_month_year', 'facility_code')
    search_fields = ('visit_no', 'bill_no', 'department', 'item_name')
