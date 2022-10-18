from django.shortcuts import render, redirect
from .models import Field, FormName, FormData
import json
import collections
from .forms import FieldForm, FormNameForm
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import HttpResponseRedirect

# Create your views here.
def form_view(request):
    form = FieldForm(request.POST)
    formname_form = FormNameForm(request.POST)
    form_name = ''

    if request.method == "POST":
        name = request.POST['name']
        type = request.POST.getlist('type')
        label = request.POST.getlist('label')
        more_field = request.POST.getlist('more_field')
        field_type = ','.join(request.POST.getlist('field_type'))
        p, created = FormName.objects.get_or_create(
            name=name,
        )
        response_record = {}

        result = collections.defaultdict(list)
        form_name = FormName.objects.get(id=p.id)
        response_record[form_name.name] = dict(result)

        for t in zip(type, label):
            result[t[0]].append(t[1])
            response_record[form_name.name] = dict(result)

        if form_name:
            field = Field(type=type, label=response_record, more_field=more_field, field_type=field_type, formname=p)
            field.save()
            return render(request, 'core/index.html',{'form': form, 'formname_form': formname_form, 'form_name': form_name})
        return redirect('/')

    return render(request,'core/index.html',{'form':form,'formname_form':formname_form})

def contact_view(request,slug):
    form = FieldForm(request.POST,request.FILES)
    formname = FormName.objects.get(slug=slug)
    fields = Field.objects.filter(formname_id=formname.id)

    if request.method == "POST":
        response_record = {}
        img_respose = {}

        formname = FormName.objects.get(slug=slug)
        response_record[formname.name] = request.POST
        data = json.dumps(request.POST)
        load_data = json.loads(data)
        response_record[formname.name] = load_data
        del response_record[formname.name]['csrfmiddlewaretoken']
        if not request.FILES:
            formname = FormData(value=response_record, formname=formname)
            formname.save()
        for filename, file in request.FILES.items():
            formname = FormName.objects.get(slug=slug)
            img_respose[filename] = file
            folder = 'media/images'
            fs = FileSystemStorage(location=folder)
            filename = fs.save(img_respose[filename].name, img_respose[filename])
            response_record[formname.name]
            dict = {'Image' : filename}
            response_record[formname.name].update(dict)
            formname = FormData(value=response_record, formname=formname)
            formname.save()
    return render(request,'core/contact.html',{'formname':formname,'fields':fields,'form':form})

def get_form_data(request,id):
    formdata = FormData.objects.get(id=id)
    form_data = FormData.objects.all()
    return render(request, 'core/form_list.html', {'form_data': form_data,'formdata':formdata})