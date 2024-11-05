from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.permissions import AllowAny
from .models import TouristDestination
from .serializers import TouristDestinationSerializer
from rest_framework import generics
from .forms import TouristDestinationForm

class DestinationCreateView(generics.ListCreateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer
    permission_classes = [AllowAny]

class DestinationDetailView(generics.RetrieveAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class DestinationUpdateView(generics.RetrieveUpdateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class DestinationDeleteView(generics.DestroyAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class DestinationListView(generics.ListAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer
    permission_classes = [AllowAny]

class DestinationSearchView(generics.ListAPIView):
    serializer_class = TouristDestinationSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if query:
            return TouristDestination.objects.filter(place_name__icontains=query)
        return TouristDestination.objects.all()

def create_destination(request):
    if request.method == 'POST':
        form = TouristDestinationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url = 'http://127.0.0.1:8000/api/create/'
                data = form.cleaned_data

                files = {}
                if 'image' in request.FILES:
                    files['image'] = request.FILES['image']

                response = requests.post(api_url, data=data, files=files)

                if response.status_code == 201:
                    messages.success(request, 'Destination added successfully')
                    return redirect('index')
                else:
                    messages.error(request, f'Error {response.status_code}')
                    return redirect('index')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request {str(e)}')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = TouristDestinationForm()

    return render(request, 'create_destination.html', {'form': form})

def update_destination(request, pk):
    try:
        destination = TouristDestination.objects.get(pk=pk)
    except TouristDestination.DoesNotExist:
        messages.error(request, 'Destination not found.')
        return redirect('index')

    if request.method == 'POST':
        form = TouristDestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()

            data = form.cleaned_data
            api_url = f'http://127.0.0.1:8000/api/update/{pk}/'

            files = {}
            if 'image' in request.FILES:
                files['image'] = request.FILES['image']

            try:
                response = requests.put(api_url, data=data, files=files)

                if response.status_code == 200:
                    messages.success(request, 'Destination updated successfully')
                    return redirect('index')
                else:
                    messages.error(request, f'Error {response.status_code}: {response.text}')
                    return redirect('index')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request: {str(e)}')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = TouristDestinationForm(instance=destination)

    return render(request, 'update_destination.html', {'form': form, 'destination': destination})



def delete_destination(request, pk):
    if request.method == 'POST':
        try:
            api_url = f'http://127.0.0.1:8000/api/delete/{pk}/'
            response = requests.delete(api_url)

            if response.status_code == 204:
                messages.success(request, 'Destination deleted successfully')
            else:
                messages.error(request, f'Error {response.status_code}: {response.text}')
        except requests.RequestException as e:
            messages.error(request, f'Error during API request: {str(e)}')

        return redirect('index')

    return redirect('index')


def index(request):
    if request.method == 'POST':
        search = request.POST.get('search', '')
        api_url = f'http://127.0.0.1:8000/api/search/?query={search}'
    else:
        api_url = 'http://127.0.0.1:8000/api/list/'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            paginator = Paginator(data, 10)
            page = request.GET.get('page')

            try:
                destinations = paginator.page(page)
            except PageNotAnInteger:
                destinations = paginator.page(1)
            except EmptyPage:
                destinations = paginator.page(paginator.num_pages)

            return render(request, 'index.html', {'destinations': destinations})
        else:
            return render(request, 'index.html', {'error_message': f'Error {response.status_code}: {response.text}'})
    except requests.RequestException as e:
        return render(request, 'index.html', {'error_message': f'Error during API request: {str(e)}'})


def destination_detail(request, pk):
    api_url = f'http://127.0.0.1:8000/api/detail/{pk}/'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            destination = response.json()
            return render(request, 'destination_detail.html', {'destination': destination})
        else:
            return render(request, 'destination_detail.html',
                          {'error_message': f'Error {response.status_code}: {response.text}'})
    except requests.RequestException as e:
        return render(request, 'destination_detail.html', {'error_message': f'Error during API request: {str(e)}'})
