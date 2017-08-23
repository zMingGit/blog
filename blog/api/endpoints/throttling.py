from rest_framework.throttling import BaseThrottle


class NoThrottling(BaseThrottle):
    """ allow any request
    """
    def allow_request(self, request, view):
        return True
