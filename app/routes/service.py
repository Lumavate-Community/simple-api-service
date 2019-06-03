from lumavate_service_util import lumavate_route, SecurityType, RequestType
from flask import request, render_template, g
from behavior import Service

@lumavate_route('/', ['GET'], RequestType.page, [SecurityType.jwt])
def root():
  return render_template('home.html', logo='/{}/{}/discover/icons/microservice.png'.format(g.integration_cloud, g.widget_type))

@lumavate_route('/data/<path:route_path>', ['GET','POST'], RequestType.api, [SecurityType.signed, SecurityType.sut])
def data(route_path):
  if request.method == 'POST':
    return Service().post_data(route_path)
  else:
    return Service().get_data(route_path)

@lumavate_route('/discover/properties', ['GET'], RequestType.system, [SecurityType.jwt])
def properties():
  return Service().do_properties()
