# views.py
from django.http import HttpResponse
from .models import FacilityToken, Facilities
import uuid
from datetime import datetime
from django.utils import timezone  # Importing timezone from Django's utilities
from datetime import datetime, timedelta

def generate_token():
    return str(uuid.uuid4())

def home(request):
    # Get all facilities from the database
    facilities = Facilities.objects.all()
    response_message = ""

    for facility in facilities:
        try:
            # Try to get the token for the current facility
            facility_token = FacilityToken.objects.get(facility=facility)
            # Check if token has expired
            if facility_token.expires_at < timezone.now():
                # Regenerate token if expired
                token = generate_token()
                # Update token and expiration date
                facility_token.token = token
                facility_token.expires_at = timezone.now() + timedelta(days=365)
                facility_token.save()
            else:
                token = facility_token.token
        except FacilityToken.DoesNotExist:
            # If the token doesn't exist, generate a new one
            token = generate_token()
            # Create a new FacilityToken for the current facility
            expires_at = timezone.now() + timedelta(days=365)
            FacilityToken.objects.create(facility=facility, token=token, expires_at=expires_at)
        
        # Add facility name and token to the response message
        response_message += f"Facility: {facility.facility_name}, Token: {token}<br>"
    
    return HttpResponse(response_message)


from django.shortcuts import render
from .forms import UploadFileForm
from .script import read_excel_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            data= read_excel_file(file_path)

            #data validation
            
            return render(request, 'success.html')
        
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
import os

from django.conf import settings
def handle_uploaded_file(file):
    # Get the upload directory from Django settings
    upload_dir = os.path.join(settings.BASE_DIR,'app1','uploaded_files')
    

    # Create the directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Save the file to the upload directory
    with open(os.path.join(upload_dir, file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    file_path = os.path.join(upload_dir, file.name)
    print("file_path",file_path)
    return file_path