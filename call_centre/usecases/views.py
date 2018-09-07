import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt


# @method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class BaseJsonView(View):
    @classmethod
    def get_response(cls, success, status_code, error_dict):
        response_dict = {"success": success, "errors": error_dict}
        return HttpResponse(json.dumps(response_dict), status=status_code, content_type='application/json')


class CallAgent(BaseJsonView):
    def post(self, request, *args, **kwargs):
        if request.POST.get('ConferenceFirstMember') == 'true':
            to_number = request.POST.get('To')
            return self.get_response(True, 200, {'to': to_number})
        return self.get_response(False, 400, {})
