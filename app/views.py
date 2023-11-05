import requests
from django.http import HttpResponse

def proxy_view(request):
    target_url = request.GET.get('')
    custom_headers = request.META.get('HTTP_CUSTOM_HEADERS')
    
    blocked_sites = ["facebook.com", "youtube.com", "twitter.com", "instagram.com", "yts.mx"] # only used for testing the proxy server
    
    if any(site in target_url for site in blocked_sites): # only used for testing the proxy server
        return HttpResponse("Access to this website is prohibited.") # only used for testing the proxy server

    headers = {}
    if custom_headers:
        headers.update({'Custom-Headers': custom_headers})

    response = requests.get(target_url, headers=headers)

    return HttpResponse(content=response.content, content_type=response.headers['Content-Type'])
