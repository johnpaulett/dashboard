from annoying.decorators import render_to
from collections import defaultdict
from django.utils.datastructures import SortedDict
from monit.models import Server
from stream.models import Item
import operator

@render_to('dashboard/index.html')
def index(request):
    stream = group_by_field(Item.objects.all().order_by('-time')[:20], lambda x: x.time.date())
    return {'stream': stream,
            'monit_table': monit_widget()}

def distinct_services(servers):
    # count how often each service occurs
    services = defaultdict(int) # int defaults to 0
    for server in servers:
        for service in server.service_set.all():
            services[service.name] += 1
    sorted_services = sorted(dict(services).items(), key=operator.itemgetter(1))
    return [service for service, count in sorted_services]


#TODO move to django-monit
def monit_widget():
    servers = Server.objects.all()
    services  = distinct_services(servers)

    header = ['']
    header.extend(services)

    empty_row = lambda : [None for i in xrange(0, len(services)+1)]
    table = [header]

    # TODO consider refactoring duplicate loop (distinct_services())
    for server in servers:
        row = empty_row()
        row[0] = server
        for service in server.service_set.all():
            row[services.index(service.name)+1] = service.get_status_display()
        table.append(row)
            
    return table

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
