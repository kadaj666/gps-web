from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MarketApk
from django.utils.timesince import timesince




class MarketApkSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField(method_name='add_to_name')
    score = serializers.SerializerMethodField(method_name='set_score')
    developer = serializers.SerializerMethodField(method_name='set_info')
    last_sync = serializers.SerializerMethodField(method_name='last_sync_format')
    class Meta:
        model = MarketApk
        fields = ('__all__')


    def add_to_name(self, instance):
        name = MarketApk.objects.values('id','name','url','apk').get(id=instance.id)
        return name
  
    def set_score(self, instance):
        if not instance.score:
            score = 0
        else:
            score = round(float(instance.score),2)
        return score
    
    def set_info(self, instance):
        developer = MarketApk.objects.values('developerid').get(id=instance.id)
        try:
            int(developer["developerid"])
            developer = "https://play.google.com/store/apps/dev?id="+developer["developerid"]+"&hl=en&gl=us"
        except:
            developer = "https://play.google.com/store/apps/developer?id="+str(developer["developerid"])+"&hl=en&gl=us"
        return developer

    def last_sync_format(self, instance):
        if not instance.last_sync:
            return()
        else:
            return timesince(instance.last_sync)