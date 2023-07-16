from django import forms
from task_manager.tasks.models import TasksModel
from task_manager.statuses.models import StatusModel
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from task_manager.labels.models import LabelModel
import django_filters
from task_manager.utils import UserChoiceField, UserFiletField


class TasksForm(forms.ModelForm):

    name = forms.CharField(max_length=100, label=_('Name'),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('Name'),
                                      'id': 'id_name',
                                      'class': 'form-control'}))

    description = forms.CharField(
        required=False, label=_('Description'),
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'id': 'id_description',
                   'placeholder': _('Description')}))

    status = forms.ModelChoiceField(
        queryset=StatusModel.objects.all(), label=_('Status'),
        widget=forms.Select(
            attrs={'id': 'id_status',
                   'class': 'form-select'}))

    executor = UserChoiceField(
        queryset=User.objects.all(), label=_('Executor'),
        required=False,

        widget=forms.Select(
            attrs={'id': 'id_executor',

                   'class': 'form-select'}))

    labels = forms.ModelMultipleChoiceField(
        queryset=LabelModel.objects.all(), label=_('labels'),
        required=False,
        widget=forms.SelectMultiple(attrs={'id': 'id_labels',
                                           'class': 'form-select'})
    )

    class Meta:
        model = TasksModel
        fields = ['name', 'description', 'status', 'executor', 'labels']


class FilterForm(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        queryset=StatusModel.objects.all(), label=_('Status'),
        widget=forms.Select(
            attrs={'id': 'id_status',
                   'class': 'form-select'}))

    executor = UserFiletField(
        queryset=User.objects.all(), label=_('Executor'), required=False,
        widget=forms.Select(
            attrs={'id': 'id_executor',
                   'class': 'form-select'}))

    labels = django_filters.ModelChoiceFilter(
        queryset=LabelModel.objects.all(), label=_('label'),
        required=False,
        widget=forms.Select(attrs={'id': 'id_labels',
                                   'class': 'form-select'}))

    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(attrs=({'id': 'id_self_tasks',
                                           'class': 'form-check-input'})),
        method='filter_is_mine', label=_('Only your tasks'))

    class Meta:
        model = TasksModel
        fields = ['status', 'executor', 'labels', 'self_tasks']
