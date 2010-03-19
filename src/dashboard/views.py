from annoying.decorators import render_to

@render_to('dashboard/index.html')
def index(request):
    return {}
