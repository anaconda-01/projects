from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Leads,Agents
from .forms import LeadForm,LeadModelForm
lead=Leads.objects.all()
context={
    "lead":lead
}

def home(request):
    return render(request, "a.html",context)


def lead_list(request,pk):
    print(pk)
    leads = Leads.objects.get(id=pk)
    context = {
        "leads": leads
    }   
    print(lead)
    return render(request, "leads/lead_list.html", context)

def lead_create(request):
    form=LeadModelForm()
    submitted="not submitted"
    if request.method=='POST':
        print(request.POST)
        form=LeadModelForm(request.POST)
        if form.is_valid():
            # print("it is validated")
            # data=form.cleaned_data
            # print(data)
            # Leads.objects.create(first_name=data['first_name'],last_name=data['last_name'],age=data['age'],agent=data['agent'])
            # submitted="submitted"
            form.save()
            return redirect("home")
            
    context_form={  
        "form":form,
        "submitted":submitted
    }
    return render(request,"leads/create_lead.html",context_form)
def alter_lead(request,pk):
    lead=Leads.objects.get(id=pk)
    alter_form=LeadModelForm(instance=lead)
    if request.method=='POST':
        alter_form=LeadModelForm(request.POST)
        if alter_form.is_valid():
            # data=alter_form.cleaned_data
            # lead.first_name=data['first_name']
            # lead.last_name=data['last_name']
            # lead.age=data['age']
            # lead.save()
            alter_form.save()

            return redirect("home")
    context_form={
            "alter_form":alter_form,
            "lead":lead
            }
    return render(request,"leads/alter_form.html",context_form)
def delete_lead(request,pk):
    lead=Leads.objects.get(id=pk)   
    if lead in Leads.objects.all():
        lead.delete()
        return redirect("home")
    return HttpResponse("error")


    


