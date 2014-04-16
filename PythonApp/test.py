#testuwsgi.py
def app(env,start_response):
   start_response('200 OK',[('Content-Type','text/html')])
   return "hello world"
