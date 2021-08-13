from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MarketApkSerializer
from .models import MarketApk, ApkReview



@login_required
def index(request):
    apk_name = MarketApk.objects.all()
    context = {'apks':apk_name}
    return render(request, 'market/index.html', context)

@login_required
def details(request, apk_id):
    try:
        apk_name = MarketApk.objects.get(apk=apk_id)
    except:
        apk_name = None 
    reveiws =  ApkReview.objects.filter(apk=apk_name).order_by('-at')
    context = {'apk':apk_name, 'reviews':reveiws}
    return render(request, 'market/details.html', context)

class MarketApkViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MarketApk.objects.all()
    serializer_class = MarketApkSerializer
    http_method_names = ['get', 'head', 'post', 'delete']