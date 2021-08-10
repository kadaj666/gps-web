from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import permissions
from django.core.serializers import serialize
from .serializers import MarketApkSerializer
from .models import MarketApk

@login_required
def index(request):
    apk = MarketApk.objects.all()
    context = {'apks':apk}
    return render(request, 'market/index.html', context)

def details(request, apk):
    apk = MarketApk.objects.get(apk=apk)
    context = {'apk':apk}
    return render(request, 'market/details.html', context)

class MarketApkViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MarketApk.objects.all()
    serializer_class = MarketApkSerializer
    http_method_names = ['get', 'head', 'post', 'delete']