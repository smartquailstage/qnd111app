from .models import Coupon
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(Coupon)
class Order(TranslationOptions):
    fields = ('code','valid_from ','valid_to','discount','active')


