from django.db.models import Q


def get_filters(filters):
    query = Q()
    for key, value in filters.items():
        if not value is None:
            query &= Q((f'{key}', value))
    return query 
