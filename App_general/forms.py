from dataclasses import field, fields
from django import forms
from App_foods.models import FoodModel
from .models import Subscription

class FoodMultipleChoice(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj: FoodModel) -> str:
        return obj.title

#Create Form SubscriptionForm for Subcription_form
# class SubscriptionForm(forms.Form):
#     name = forms.CharField(max_length=60, required=True, label='ชื่อ-สกุล')
#     email = forms.EmailField(max_length=60, required=True, label='Email')
#     food_set = FoodMultipleChoice(
#         queryset= FoodModel.objects.order_by('-is_Premium'),
#         required= True,
#         label= 'เมนูที่สนใจ',
#         widget= forms.CheckboxSelectMultiple
#     )
#     acceptedPolicy = forms.BooleanField(required=True, label= 'ยอมรับนโยบายความเป็นส่วนตัวสำหรับลูกค้า')


#Create ModelForm SubscriptionModelForm for Subcription_form
class SubscriptionModelForm(forms.ModelForm):
    food_set = FoodMultipleChoice(
        queryset = FoodModel.objects.order_by('-is_Premium'),
        required = True,
        label = 'เมนูที่สนใจ',
        widget = forms.CheckboxSelectMultiple
    )
    acceptedPolicy = forms.BooleanField(required=True, label= 'ยอมรับนโยบายความเป็นส่วนตัวสำหรับลูกค้า')

    class Meta:
        model = Subscription
        fields = ['name', 'email', 'food_set', 'acceptedPolicy']
        labels = {
            'name': 'ชื่อ-สกุล',
            'email': 'Email',
            'food_set': 'เมนูที่สนใจ'
        }