"""A spell checker for the PPP. Use the Aspell API."""

from ppp_libmodule import HttpRequestHandler
from .requesthandler import RequestHandler, StringCorrector, Word

def app(environ, start_response):
    """Function called by the WSGI server."""
    return HttpRequestHandler(environ, start_response, RequestHandler) \
            .dispatch()

__all__ = ['StringCorrector','Word']
