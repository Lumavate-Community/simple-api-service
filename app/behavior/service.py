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

    #Text
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is useful for entering free-form text
* Type: Text
* Options: None
    '''

    properties.append(Properties.Property('Sample Properties', 'Text', 'txtProp', 'Text', 'text',help_text=helpText))

    #Numeric - With Maximum & Minimum values
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a numeric value is required
* Type: Numeric
* Options:
  * Min - Sets the minimum allowed value
  * Max - Sets the maximum allowed value
    '''

    properties.append(Properties.Property('Sample Properties', 'Numeric', 'numProp', 'Numeric (with Max & Min)', 'numeric', default=0, help_text=helpText, options={ 'max': 100, 'min': -100 }))

    #Text Area - Configured for 3 rows
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a larger amount of free-form text is input.
* Type: Numeric
* Options:
  * Rows - Sets the number of rows in the Textarea
    '''

    properties.append(Properties.Property('Sample Properties', 'Text', 'taProp', 'TextArea (with 3 rows)', 'text', options={ 'rows': 3 }, help_text=helpText))

    #Translatable Text
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a text value will be supplied for different languages, so that the proper text will display based on the user's language settings.
* Type: Translated-Text
    '''

    properties.append(Properties.Property('Sample Properties', 'Text', 'tText', 'Translatable Text', 'translated-text',help_text=helpText))

    #Dropdown - configured with sample options
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a list of options is required for user selection.
* Type: Dropdown
* Options:
  * An object which contains key-value pairs representing the selection options

  { "value1": "Option 1" }
    '''

    sampleOptions = {
        "value1": "Option 1",
        "value2": "Option 2"
        }
    properties.append(Properties.Property('Sample Properties', 'Selectable', 'ddProp', 'Dropdown', 'dropdown', options=sampleOptions,help_text=helpText))

    #Multiselect
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user is required to select multiple options from a list.
* Type: Dropdown
* Options:
  * An array of options

  [ { "value": "value1", "displayValue": "Option 1" }, { "value": "value2", "displayValue" : "Option 2" } ]
    '''

    multiselectOptions = [
      { "value": "value1", "displayValue": "Option 1" },
      { "value": "value2", "displayValue" : "Option 2" }
    ]
    properties.append(Properties.Property('Sample Properties', 'Selectable', 'msProp', 'Multiple Selection', 'multiselect', options=multiselectOptions,help_text=helpText))

    #Checkbox
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user is required to select a single, or multiple, options
* Type: Checkbox
    '''

    properties.append(Properties.Property('Sample Properties', 'Selectable', 'cbProp', 'Checkbox', 'checkbox',help_text=helpText))

    #Toggle
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user is required to set a boolean (True/False) option
* Type: Toggle
    '''

    properties.append(Properties.Property('Sample Properties', 'Selectable', 'togProp', 'Toggle', 'toggle',help_text=helpText))

    #Color
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user needs to select a color from a color picker.
* Type: Color
    '''

    properties.append(Properties.Property('Sample Properties', 'Colors', 'clrProp', 'Color', 'color',help_text=helpText))

    #Theme Color - Will use the included Component-set Color Families
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user needs to select a color from a pre-defined color pallette.  The color pallette is defined by any style property on a component set which ends in 'ColorFamily'
* Type: Theme-Color
    '''

    properties.append(Properties.Property('Sample Properties', 'Colors', 'tclrProp', 'Theme Color', 'theme-color',help_text=helpText))

    #Image Upload
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user needs to upload an image for the given property
* Type: Image-Upload
    '''

    properties.append(Properties.Property('Sample Properties', 'Media', 'imgProp', 'Image Upload', 'image-upload',help_text=helpText))

    #Code Editor
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user needs to insert/edit any type of code (Javascript, HTML, etc.).
* Type: Code-Editor
    '''

    properties.append(Properties.Property('Sample Properties', 'Code', 'codeProp', 'Code Editor', 'code-editor',help_text=helpText))

    #Page Link
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used when a user needs to select anotehr widget that is being uesd within the experience
* Type: Page-Link
    '''

    properties.append(Properties.Property('Sample Properties', 'Links', 'plProp', 'Page Link - List of Experience Widgets', 'page-link', help_text=helpText))

    #Admin Launcher
    helpText = '''
Sample help for a property.  The Help Text attribute of a property support markdown to provide rich content to assist the user.

### Property Type
This type of property is used to link an admin UI defined by the container.  The container must provide the appropraite manage routes to support this property type
* Type: Admin-Launcher
    '''

    properties.append(Properties.Property('Sample Properties', 'Links', 'alProp', 'Admin Launcher', 'admin-launcher',help_text=helpText))

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
