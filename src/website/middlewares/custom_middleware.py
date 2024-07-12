import time 

from django.http import HttpResponse
from django.template.response import TemplateResponse


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before')
        # کدهایی که قبل از پردازش view اجرا می‌شوند
        start_time = time.time()
        
        response = self.get_response(request)
        print('after')
        # کدهایی که بعد از پردازش view اجرا می‌شوند
        duration = time.time() - start_time
        print(f"Request took {duration} seconds")
        
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # کدهایی که قبل از فراخوانی view اجرا می‌شوند
        print('view_func : ', view_func)
        print('view_func : ', view_func.__dict__)
        print('view_args : ', view_args)
        print('view_kwargs : ', view_kwargs)
        pass
    
    # def process_exception(self, request, exception):
    #     # کدهایی که برای مدیریت Exception استفاده می‌شوند
    #     print(f"An error occurred: {exception}")
    #     return HttpResponse("An error occurred", status=500)
    
    
    def process_template_response(self, request, response):
        # کدهایی که برای اصلاح TemplateResponse استفاده می‌شوند
        # if isinstance(response, TemplateResponse):
        response.context_data['additional_data'] = 'Some extra data'
        return response


# custom decorator usage
# from django.utils.decorators import decorator_from_middleware

# custom_middleware = decorator_from_middleware(CustomMiddleware)

# @custom_middleware
# def my_view(request):
#     # کدهای view
#     return HttpResponse("Hello, world!")