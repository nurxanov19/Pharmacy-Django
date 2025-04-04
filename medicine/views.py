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
from rest_framework.response import Response
from rest_framework.views import status

# class MedicineList(generics.ListAPIView):
#     queryset = Medicine.objects.all()
#     serializer_class = MediacineSerializer

class MedicineApiList(APIView):
    def get(self, request):
        medicines = Medicine.objects.all()
        serializer = MediacineSerializer(medicines, many=True)

        response = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
            'message': 'Medicine List'
        }
        return Response(response)


class MedicineApiCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MediacineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
                'message': 'Medicine List',
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Oops,something went wrong',
            }
        return Response(response)


class MedicineApiUpdate(APIView):
    def put(self, request, pk, *args, **kwargs):
        medicine = Medicine.objects.get(pk=pk)
        serializer = MediacineSerializer(medicine, data=request.data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                'message': 'Medicine Update',
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Oops, Something went wrong',
            }
        return Response(response)

    def patch(self, request, pk, *arg, **kwarg):
        medicine = Medicine.objects.get(pk=pk)
        serializer = MediacineSerializer(medicine, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            response = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                'message': 'Medicine Update patch',
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Smth gone wrong',
            }
        return Response(response)


class MedicineApiDetail(APIView):
    def get(self, request, pk):
        medicine = Medicine.objects.get(pk=pk)
        serializer = MediacineSerializer(medicine, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                'message': 'Medicine Detail',
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Smth gone wrong',
            }

        return Response(response)


class MedicineApiDelete(APIView):
    def delete(self, request, pk):
        medicine = Medicine.objects.get(pk=pk)
        medicine.delete()

        response = {
            'data': None,
            'status': status.HTTP_200_OK,
            'message': 'Medicine Detail',
        }
        return Response(response)




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






