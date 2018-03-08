from wsgicors import CORS

__all__ = ["CORSMixin", "make_cors_mixin"]
__version__ = "0.1.0"


def make_cors_mixin(**options):
    """Generate a CORS mixin class with custom options.  All keyword
    arguments are passed to wsgicors.CORS.
    """
    class CORSMixin:
        def __call__(self, environ, start_response):
            def start_response_wrapper(status, headers, exc_info=None):
                return start_response(status, headers)

            cors = CORS(super().__call__, **options)
            return cors(environ, start_response_wrapper)

    return CORSMixin


#: A generic CORS mixin for API Star apps.
CORSMixin = make_cors_mixin(headers="*", methods="*", maxage="86400", origin="*")
