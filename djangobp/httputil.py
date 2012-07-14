from bson.objectid import ObjectId
from django.http import HttpResponse, HttpResponseServerError
from djangobp.mongomodel import UserMessageException
import datetime
import logging
import simplejson

class HttpResponseJSON(HttpResponse):
    def __init__(self, data):
        HttpResponse.__init__(self, simplejson.dumps(data, ensure_ascii=False, cls=BSONEncoder), content_type='application/json')

class BSONEncoder(simplejson.encoder.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat() + 'Z'
#            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, ObjectId) :
            return str(obj)
        else:
            return simplejson.JSONEncoder.default(self, obj)

simplejson.JSONEncoder = BSONEncoder

logger = logging.getLogger(__name__)

class ErrorLoggingMiddleWare(object):
    def process_exception(self, request, exception):
        if request.path.startswith('/api'):
            if isinstance(exception, UserMessageException):
                return HttpResponseJSON({'error': {'message': exception.message}})
            logger.exception(exception)
            print 'exception:', exception.message
            return HttpResponseServerError(exception.message)

def to_json(obj):
    return simplejson.dumps(obj, indent=4)