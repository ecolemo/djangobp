from bson.objectid import ObjectId
from django.http import HttpResponse, HttpResponseServerError
from djangobp.mongomodel import UserMessageException
import datetime
import logging
import simplejson
import openpyxl
import tempfile
import os
from django.forms.models import model_to_dict

class HttpResponseJSON(HttpResponse):
    def __init__(self, data):
        HttpResponse.__init__(self, simplejson.dumps(data, ensure_ascii=False, cls=BSONEncoder), content_type='application/json')

class HttpResponseExcel(HttpResponse):
    def __init__(self, title, queryset, fields, headers=None):
        HttpResponse.__init__(self, mimetype="application/ms-excel")
        self['Content-Disposition'] = 'attachment; filename=%s.xlsx' % title.encode('utf8')
        workbook = openpyxl.workbook.Workbook(optimized_write=True)
        worksheet = workbook.create_sheet()
        worksheet.title = title
        if headers: 
            worksheet.append(headers)
        else:
            worksheet.append(fields)

        for model in queryset:
            result = []
            for field in fields:
                value = getattr(model, field)
                value = value.strftime('%Y.%m.%d %H:%M:%S') if type(value) == datetime else value
                value = '' if value is None else value
                value = '%s' % (value)
                result.append(value)
            worksheet.append(result)

        f = tempfile.NamedTemporaryFile(delete=True)
        workbook.save(f)
        f.seek(0, os.SEEK_SET)
        self.write(f.read())
        f.close()

def admin_export_as_excel(modeladmin, request, queryset):
    return HttpResponseExcel(request.path.replace('/', '_'), queryset, modeladmin.list_display)

class BSONEncoder(simplejson.encoder.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat() + 'Z'
#            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, ObjectId) :
            return str(obj)
        else:
            return simplejson.JSONEncoder.default(self, obj)

#simplejson.JSONEncoder = BSONEncoder

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