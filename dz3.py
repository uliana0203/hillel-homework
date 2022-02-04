class Url:
    def __init__(self, scheme, authority, path=None, query=None, fragment=None):
        self.scheme = scheme + '://'
        self.authority = authority
        self.par = [self.scheme, self.authority]
        if path is not None:
            self.path = '/' + '/'.join(path)
            self.par.append(self.path)
        if query is not None:
            l = []
            query = list(query.items())
            for key, value in query:
                l.append(key)
                l.append(value)
            self.query = '?' + '='.join(l[0:2]) + '&' + '='.join(l[2:4])
            self.par.append(self.query)
        if fragment is not None:
            self.fragment = '#' + fragment
            self.par.append(self.fragment)

    def __str__(self):
        return ''.join(self.par)

    def __eq__(self, other):

        return str(''.join(self.par)) == other


class HttpsUrl(Url):
    def __init__(self, authority, path=None, query=None, fragment=None):
        super().__init__('https', authority, path, query, fragment)


class HttpUrl(Url):
    def __init__(self, authority, path=None, query=None, fragment=None):
        super().__init__('http', authority, path, query, fragment)


class GoogleUrl(HttpsUrl):
    def __init__(self, path=None, query=None, fragment=None):
        super().__init__('google.com', path, query, fragment)


class WikiUrl(HttpsUrl):
    def __init__(self, path=None, query=None, fragment=None):
        super().__init__('wikipedia.org', path, query, fragment)
