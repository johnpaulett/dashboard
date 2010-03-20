from annoying.decorators import render_to
from debug_toolbare.debug.version import DebugVersion
from stream.models import Item

@render_to('dashboard/index.html')
def index(request):
    
    return {'stream': Item.objects.all().order_by('-time')[:20],
            'versions': DebugVersion()}
