from django.core.serializers import serialize
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from django.views import View
from django.urls import reverse_lazy
from .forms import MedicineForm
from django.views.generic import UpdateView, DeleteView

from rest_framework import generics
from .serializer import MediacineSerializer
from rest_framework.views import APIView

# class MedicineList(generics.ListAPIView):
#     queryset = Medicine.objects.all()
#     serializer_class = MediacineSerializer

class BookList(APIView):
    def get(self, request):
        medicines = Medicine.objects.all()
        serializeer = MediacineSerializer(medicines, many=True)









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


# class MedicineUpdate(UpdateView):
#
#     model = Medicine
#     fields = [
#             'title', 'company', 'country', 'price', 'definition', 'expiration_date', 'definition'
#         ]
#
#     template_name = 'webpages/medicine_update.html'
#     context_object_name = 'medicine'
#
#     def get_success_url(self):
#         return reverse_lazy('medicine-detail', kwargs={'pk':self.object.pk})


# class MedicineDelete(DeleteView):
#
#     model = Medicine
#     template_name = 'webpages/medicine_delete.html'
#
#     def get_success_url(self):
#         return reverse_lazy('medicine-list')


class MedicineDelete(View):
    template_name = 'webpages/medicine_delete.html'
    def get(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        return render(request, self.template_name, {'medicine': medicine})

    def post(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        medicine.delete()
        return redirect('medicine-list')




class MedicineUpdate(View):
    template_name = 'webpages/medicine_update.html'

    def get(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        form = MedicineForm(instance=medicine)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        form = MedicineForm(request.POST, instance=medicine, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('medicine-detail', kwargs={'pk': medicine.pk}))

        return render(request, self.template_name, {'form':form})






