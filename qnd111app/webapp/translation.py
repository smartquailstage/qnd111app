from .models import Home
from modeltranslation.translator import TranslationOptions, register

@register(Home)  # Asegúrate de que Home esté registrado
class HomeTranslationOptions(TranslationOptions):
    fields = ('bio','slug', 'banner_title4', 'banner_title5', 
        'banner_title6', 'banner_title7', 'banner_title8', 'banner_title9', 
        'banner_title10', 'banner_title11', 'TS_info1', 'TS_date1', 'TS_info2', 
        'TS_date2', 'TS_info3', 'TS_date3', 'TS_info4', 'TS_date4', 'TS_info5', 
        'TS_date5', 'TS_info6', 'TS_date6', 'TS_info7', 'TS_date7', 'TS_info8', 
        'TS_date8', 'TS_info9', 'TS_date9', 'TS_info10', 'TS_date10', 'TS_info11', 
        'TS_date11', 'TS_info12', 'TS_date12', 'TS_info13', 'TS_date13', 'TS_info14', 
        'TS_date14', 'TS_info15', 'TS_date15', 'TS_info16', 'TS_date16', 'TS_info17', 
        'TS_date17', 'TS_info18', 'TS_date18', 'TS_info19', 'TS_date19', 'TS_info20', 
        'TS_date20', 'consulta', 'thank_you_text', 'custom_title'
    )
