from threading import local
import re

local_vars = local()


class DBMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if navigating to admin pages
        pattern = "^/admin/"
        uri = request.get_full_path()
        # when navigating to admin page
        # if first time, set url parameter db_id (?db=db_id) to session
        # otherwise, find db_id from session
        if re.match(pattern, uri):
            db_name = request.GET.get('db_id', None)
            if db_name:
                request.session['db_id'] = db_name
            else:
                local_vars.database_name = request.session.get('db_id', 'default')
        elif view_kwargs.get('db_id', None):
            local_vars.database_name = view_kwargs['db_id']
        else:
            local_vars.database_name = 'default'
        return None