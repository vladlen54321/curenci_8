import random
from time import time
from currency.models import ResponseLog


class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time() - start
        method = request.method
        path = request.path
        key = request.GET
        idy = 0
        for i in range(4, random.randint(50, 200)):
            idy += i
        saved = ResponseLog(response_time=end, request_method=method, query_params=key, ip=idy, path=path)
        saved.save()
        return response
