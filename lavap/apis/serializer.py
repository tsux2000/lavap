from rest_framework import serializers
from .models import Lavatory

class LavatorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Lavatory
    fields = ('lat', 'lng', 'building_name', 'floor', 'urinals_num', 'bowls_num', 'jp_styles_num', 'wash_num', 'score_ave', 'create_user_id', 'create_date', 'update_date', 'confirmed_flg', 'del_flg')
