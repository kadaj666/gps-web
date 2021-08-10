from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MarketApk
from django.utils.timesince import timesince




class MarketApkSerializer(serializers.HyperlinkedModelSerializer):
    score = serializers.SerializerMethodField(method_name='set_score')
    developer = serializers.SerializerMethodField(method_name='set_info')
    last_sync = serializers.SerializerMethodField(method_name='last_sync_format')
    class Meta:
        model = MarketApk
        fields = ('__all__')


    def set_score(self, instance):
        if not instance.score:
            score = 0
        else:
            score = round(float(instance.score),2)
        return score
    
    def set_info(self, instance):
        developer = MarketApk.objects.values('developerid').get(id=instance.id)
        developer = "https://play.google.com/store/apps/developer?id="+str(developer["developerid"])+"&hl=en&gl=us"
        return developer

    def last_sync_format(self, instance):
        if not instance.last_sync:
            return()
        else:
            return timesince(instance.last_sync)