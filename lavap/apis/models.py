from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Lavatory(models.Model):
    # 位置情報
    lat = models.DecimalField('Latitude', max_digits=9, decimal_places=6,)
    lng = models.DecimalField('Longitude', max_digits=9, decimal_places=6,)
    # 建物情報
    building_name = models.CharField('Building name', max_length=255, default="",)
    floor = models.IntegerField('Floor', default=0, validators=[MinValueValidator(-99), MaxValueValidator(99)],)
    # トイレ情報
    urinals_num = models.IntegerField('Number of urinals', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(20)],)
    bowls_num = models.IntegerField('Number of toilet bowls', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(20)],)
    jp_styles_num = models.IntegerField('Number of japanese style toilets', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(20)],)
    wash_num = models.IntegerField('Number of wash basins', blank=True,null=True,  validators=[MinValueValidator(0), MaxValueValidator(20)],)
    # 平均スコア
    score_ave = models.FloatField('Average score', default=0.00, validators=[MinValueValidator(0.00), MaxValueValidator(5.00)],)
    # TODO: 利用可能曜日の実装
    # TODO: 利用可能時間帯の実装（利用可能曜日に即す）
    # TODO: 利用不可日の実装
    # 登録情報
    create_user_id = models.IntegerField('User id', default=0,)
    create_date = models.DateTimeField('Create date', default=timezone.now,)
    update_date = models.DateTimeField('Update date', auto_now=True,)
    confirmed_flg = models.BooleanField('Confirmed', default=False,)
    del_flg = models.BooleanField('Deleted', default=False,)

    def __str__(self):
        return "Lavatory No. " + str(self.pk) + "(lat: " + str(self.lat) + ", lng: " + str(self.lng) + ")"

