from .models import Dummy
from django.http.response import JsonResponse
# Create your views here.


def test(request):
    objs = Dummy.objects.with_raw()
    res = []
    for obj in objs:
        res.append({'id': obj.id, 'current_time': obj.current_time, 'first_field': obj.first_field, 'is_valid': obj.is_valid})

    return JsonResponse(res)
