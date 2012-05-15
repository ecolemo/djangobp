import datetime

date_isoformat = '%Y-%m-%dT%H:%M:%S.%fZ'
def parse_dt(s):
    return datetime.datetime.strptime(s, date_isoformat)

def dthandler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat() + 'Z'
    else:
        raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj))
