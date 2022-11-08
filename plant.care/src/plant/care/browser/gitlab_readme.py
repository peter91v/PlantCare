import requests
from requests.structures import CaseInsensitiveDict
from Products.Five.browser import BrowserView

class ReadMeView(BrowserView):
    def __call__(self, *args, **kwargs):
        self.error_msg = ''
        return super(ReadMeView, self).__call__(*args, **kwargs)

    def getHtmlFromGitlab(self):
        x = self.getResponse('https://github.com/peter91v/PlantCare/blob/master/plant.care/README.rst') 
        #we filter from hole html only inside <article
        s1 = x.find('<article')
        html = x[s1:]
        s1 = html.find('<h2')
        html = html[s1:]
        s1 = html.find('</article')
        html = html[0:s1]
        html = html.replace('src="/peter91v','src="https://github.com/peter91v')
        return html.encode()

    def initRestapi(self):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "text/html"
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64)"
        session = requests.Session()
        session.headers.update(headers)
        return session
    def getResponse(self,url):
        session = self.initRestapi()
        response = requests.get(url)
        #print(response.headers,response.status_code)
        if response.status_code == requests.codes.ok:
            if 'text/html' in response.headers['Content-Type']:
                return response.text
        return {'errors': ['StatusCode:'+str(response.status_code),'CONTENTTYPE:'+response.headers['Content-Type']]}


