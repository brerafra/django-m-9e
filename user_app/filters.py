import django_filters
from .models import User

status_choices = (
    (0, 'Cancelado'),
    (1, 'Activo')
)

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=status_choices)
    card = django_filters.CharFilter(lookup_expr='exact')
    email = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = User
        fields = {
            'created_at':['exact', 'year__gt'],
        }
