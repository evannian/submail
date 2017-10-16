#coding=utf-8

from .field  import Field


class MailMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        for k,v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k]=v
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Mail(dict):
    __metaclass__ = MailMetaclass

    to = Field()

    def __init__(self, **kw):
        super(Mail, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Mail' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def send(self):
        print self.__mappings__
        for k, v in self.__mappings__.items():
            print self.get(k,'')

