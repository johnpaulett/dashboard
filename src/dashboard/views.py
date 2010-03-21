from annoying.decorators import render_to
from django.utils.datastructures import SortedDict
from monit.models import Server
from stream.models import Item

@render_to('dashboard/index.html')
def index(request):
    stream = group_by_field(Item.objects.all().order_by('-time')[:20], lambda x: x.time.date())
    return {'stream': stream,
            'monit_servers': Server.objects.all()}


# TODO consider moving to a utils module
def group_by_field(queryset, field):
    result = SortedDict()
    for item in queryset:
        if callable(field):
            key = field(item)
        else:
            key = getattr(item, field)
        result.setdefault(key, []).append(item)
    return result
