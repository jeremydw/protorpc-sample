from . import handlers
from products import services as product_services
from protorpc.wsgi import service
import webapp2


app = webapp2.WSGIApplication((
    ('/', handlers.MainHandler),
))

api_app = service.service_mappings((
   ('/_api/products.*', product_services.ProductService),
))
