from django.http.request import HttpRequest


def get_host_with_scheme(request: HttpRequest) -> str:
    """Get host with the scheme of the request.

    Args:
        request (HttpRequest): Request instance.

    Returns:
        str: Host with scheme.
            e.g.: https://domain.com or http://127.0.0.1
    """
    scheme = request.scheme
    server_name = request.get_host()
    host = f'{scheme}://{server_name}'
    return host
