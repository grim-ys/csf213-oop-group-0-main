from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
# from .forms import DocumentForm



# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from .models import Records

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = records(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
    # return render(request, 'upload.html', {'form': form})

def home(request):
    documents = Records.objects.all()
    return render(request, './home.html', { 'documents': documents })

def approve_rec(request):
    documents = Records.objects.exclude( approval_rec="N")
    documents = documents.exclude( approval_rec="Y")
    return render(request, './approve_rec.html', { 'documents': documents })

def approve(request,id):
    approval_rec = request.POST['approval_rec']
    member = Records.objects.get(id=id)
    member.approval_rec = approval_rec.upper()
    member.save()
    return HttpResponseRedirect(reverse('home'))

def approve_doc(request):
    documents = Records.objects.exclude( approval_doc="N")
    documents = documents.exclude( approval_doc="Y")
    return render(request, './approve_doc.html', { 'documents': documents })

def approved(request,id):
    approval_doc = request.POST['approval_doc']
    member = Records.objects.get(id=id)
    member.approval_doc = approval_doc.upper()
    member.save()
    return HttpResponseRedirect(reverse('home'))

def req_doc(request):
    documents = Records.objects.all()
    # documents = documents.exclude( approval_doc="Y")
    return render(request, './req_doc.html', { 'documents': documents })

def approvedoc(request,id):
    time = request.POST['time']
    member = Records.objects.get(id=id)
    member.time_limit = time.upper()
    member.save()
    return HttpResponseRedirect(reverse('home'))

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, './simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, './simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, './form.html', {'form': form})
    # return render(request, './model_form_upload.html', {
    #     'form': form
    # })


def req_rec(request):
    documents = Records.objects.filter(time_limit__isnull=True)
    approved_reports = Records.objects.filter( approval_doc="Y")
    pending = Records.objects.exclude( approval_rec="N")
    pending = pending.exclude( approval_rec="Y")
    patients = patient.objects.all()
    # documents = documents.exclude( approval_rec="Y")
    return render(request, './apna-doctor-dashboard.html', { 'documents': documents, 'approved_reports': approved_reports, 'pending': pending, 'patients': patients })


def patientdb(request):
    documents = Records.objects.filter(time_limit__isnull=False)
    documents = documents.exclude( approval_doc="Y")
    approved_reports = Records.objects.filter( approval_rec="Y")
    pending = Records.objects.exclude( approval_rec="N")
    pending = pending.exclude( approval_rec="Y")
    patients = patient.objects.all()
    # documents = documents.exclude( approval_rec="Y")
    return render(request, './patient.html', { 'documents': documents, 'approved_reports': approved_reports, 'pending': pending, 'patients': patients })