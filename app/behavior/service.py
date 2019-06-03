from flask import g
from lumavate_service_util import get_lumavate_request, LumavateRequest, SecurityAssertion
from lumavate_properties import Properties
from lumavate_exceptions import ApiException

class InternalRequest(LumavateRequest):
  def sign_url(self, method, path, payload, headers):
    return path

  def get_auth_token(self):
    return str(g.service_data.get('authType','Bearer')) + ' ' + str(g.service_data.get('accessToken',''))

class ServiceSecurityAssertion(SecurityAssertion):
  def load_rolemap(self):
    self._rolemap['readers'] = g.service_data.get('readRoles', [])

class Service():
  def do_properties(self, ic='ic', url_ref='ms'):
    groups = ServiceSecurityAssertion().get_all_auth_groups()
    authTypes = {
        "Bearer":"Bearer",
        "Token":"Token"
        }
    properties = []

    properties.append(Properties.Property('API', 'Base URI', 'apiEndpoint', 'Base URI for all endpoints', 'text'))
    properties.append(Properties.Property('API', 'Authentication Settings', 'authType', 'Authorization Header Type', 'dropdown', options=authTypes, default="Bearer"))
    properties.append(Properties.Property('API', 'Authentication Settings', 'accessToken', 'Access Token', 'text'))

    properties.append(Properties.Property('Authorization', 'Authorization Settings', 'readRoles', 'Read Roles', 'multiselect', options=groups, default=[]))

    return [x.to_json() for x in properties]

  def get_access_token(self):
    return g.service_data['accessToken']

  def authorize_wrapper(self, func):
    try:
      return func()
    except ApiException as e:
      #Update current Session
      return func()

  def get_data(self, data_type):
    ServiceSecurityAssertion().assert_has_role(['readers'])
    return self.authorize_wrapper(lambda: InternalRequest().get(g.service_data.get('apiEndpoint').rstrip("/") + "/" + data_type + "/"))
