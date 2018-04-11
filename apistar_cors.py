from wsgicors import CORS

__all__ = ["CORSMixin", "make_cors_mixin"]
__version__ = "0.2.0"


def make_cors_mixin(**options):
    """Generate a CORS mixin class with custom options.  All keyword
    arguments are passed to wsgicors.CORS.
    """
    class CORSMixin:
        def __call__(self, environ, start_response):
            cors = CORS(super().__call__, **options)
            return cors(environ, start_response)

    return CORSMixin


#: A generic CORS mixin for API Star apps.
CORSMixin = make_cors_mixin(headers="*", methods="*", maxage="86400", origin="*")
