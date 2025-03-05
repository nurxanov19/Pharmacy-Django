from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from django.views import View
from django.urls import reverse_lazy
from .forms import MedicineForm
from django.views.generic import UpdateView, DeleteView


def home_page(request):
    return render(request, 'home.html')


class MedicineList(View):

    def get(self, request):
        medicines = Medicine.objects.all()
        return render(request, 'webpages/medicine_list.html', {'medicines': medicines})


class MedicineDetail(View):

    def get(self, request, pk):
        medicine = Medicine.objects.get(id=pk)
        return render(request, 'webpages/medicine_detail.html', {'medicine': medicine})


class MedicineCreate(View):

    def get(self, request):
        form = MedicineForm()
        return render(request, 'webpages/medicine_create.html', {'form': form})

    def post(self, request):
        form = MedicineForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('medicine-list')

        return render(request, 'webpages/medicine_create.html', {'form': form})


class MedicineUpdate(UpdateView):

    model = Medicine
    fields = [
            'title', 'company', 'country', 'price', 'definition', 'expiration_date', 'definition'
        ]

    template_name = 'webpages/medicine_update.html'
    context_object_name = 'medicine'

    def get_success_url(self):
        return reverse_lazy('medicine-detail', kwargs={'pk':self.object.pk})


class MedicineDelete(DeleteView):

    model = Medicine
    template_name = 'webpages/medicine_delete.html'

    def get_success_url(self):
        return reverse_lazy('medicine-list')
