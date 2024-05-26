from rest_framework import serializers
from .models import FacilityToken, raw_crh_patient_diagnosis, raw_crh_patient_services, raw_hrm_patient_dignosis, raw_hrm_patient_services

class FacilityTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityToken
        fields = '__all__'

class RawCrhPatientDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = raw_crh_patient_diagnosis
        fields = '__all__'

class RawCrhPatientServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = raw_crh_patient_services
        fields = '__all__'

class RawHrmPatientDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = raw_hrm_patient_dignosis
        fields = '__all__'

class RawHrmPatientServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = raw_hrm_patient_services
        fields = '__all__'
