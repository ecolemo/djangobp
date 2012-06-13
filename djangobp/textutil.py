from django.utils.translation import ugettext

def gettext(msgid):
    return ugettext(msgid).decode('utf8')
