from contentstack import HTTPConnection
from contentstack import Config
from contentstack.errors import StackException


import os
import sys
sys.path.insert(0, os.path.abspath('.'))


class Stack(object):

    def __init__(self, **kwargs):

        """
        provide key-worded, variable-length argument list
        :param kwargs: key-worded list
        :type kwargs: object
        :param api_key: stack 'api_key' of your target stack.
        :param access_token: stack 'access_token' of your target stack.
        :param environment: stack 'environment' of your target stack.
        :param config: config='<contentstack.Config>' (optional) it is useful to change config of the stack's
        configurations like host, version of the stack.
        
        ==============================
        
        [Example]:

        >>> import contentstack
        >>> stack: Stack = Stack(api_key ='api_key', access_token='access_token', environment='environment')

        [OR] To declare custom stack
        >>> config = Config()
        >>> config.host('cdn.contentstack.io')
        >>> stack: Stack = Stack(api_key ='API_Key',access_token='access_token',environment='environment', config=config)
        
        ==============================
        """

        self.config = None
        self.__http_request = None
        self.__query_params = dict()
        self.__stack_headers = dict()
        self.__headers = dict()
        self.__image_transform_url = None
        self.__image_params = dict
        self.__sync_query = dict()
        for key, value in kwargs.items():
            self.__headers[key] = value
        self.__initialise_stack()

    @property
    def api_key(self):

        """
        :return: api_key of the stack
        :rtype: str
        
        ==============================
        
        [Example]:

        >>> api_key = stack.api_key
        
        ==============================
        """

        if 'api_key' in self.__stack_headers:
            app_key = self.__stack_headers['api_key']
            return app_key

    @property
    def get_http_instance(self):

        """
        This method returns http_instance of the stack.
        :return: http_request
        :rtype: <contentstack.http_connection.HTTPConnection()>
        
        ==============================
        
        [Example]:

        >>> http_instance = stack.get_http_instance
        
        ==============================
        """

        return self.__http_request

    @property
    def access_token(self):

        """
        This method returns access_token of the stack.
        :return: access_token
        :rtype: str
        
        ==============================
        
        [Example]:

        >>> access_token: str = stack.access_token
        
        ==============================
        """

        if 'access_token' in self.__stack_headers:
            access_token = self.__stack_headers['access_token']
            return access_token
        else:
            return None

    @property
    def environment(self):

        """
        This method returns  environment of the stack
        :return: environment of the stack
        :rtype: str
        
        ==============================
        
        [Example]:

        >>> env = stack.environment
        
        ==============================
        """

        if 'environment' in self.__stack_headers:
            return self.__stack_headers['environment']
        else:
            return None

    @environment.setter
    def environment(self, env):

        """
        :param env: environment for the stack
        :type env: str
        :return: self
        :rtype: Stack
        
        ==============================
        
        [Example]:

        >>> stack = stack.environment = 'product'
        
        ==============================
        """

        if env is not None and isinstance(env, str):
            self.__stack_headers['environment'] = env
        else:
            raise KeyError('Kindly provide valid Argument')

    @property
    def headers(self):

        """
        :return: list of stack headers
        :rtype: dict
        
        ==============================
        
        [Example]:

        >>> headers = stack.add_header
        
        ==============================
        """

        return self.__stack_headers

    def __initialise_stack(self):
        if len(self.__headers) > 0:
            if 'api_key' not in self.__headers:
                raise StackException('Kindly provide API_Key')
            else:
                self.__stack_headers['api_key'] = self.__headers['api_key']
            if 'access_token' not in self.__headers:
                raise StackException('Kindly provide access token')
            else:
                self.__stack_headers['access_token'] = self.__headers['access_token']
            if 'environment' not in self.__headers:
                raise StackException('Kindly provide environment')
            else:
                self.__stack_headers['environment'] = self.__headers['environment']
            if 'config' in self.__headers:
                self.config = self.__headers['config']
                # Remove the config from the headers
                self.__headers.pop('config', None)
            else:
                self.config = Config()
            self.__http_request = HTTPConnection(self.config.endpoint, self.__query_params, self.__stack_headers)

    def content_type(self, content_type_id):

        """
        Content type defines the structure or schema
        of a page or a section of your web or mobile property.
        To create content for your application, you
        are required to first create a content type.
        and then create entries using the content type.
        Read more about Content Types.
        API Reference: https://www.contentstack.com/docs/apis/content-delivery-api/#content-types

        :param content_type_id: Content Type UID.
        :type content_type_id: str
        :return: content_type
        :rtype: <contentstack.ContentType>

        ==============================
        
        [Example]:

        >>> content_type = stack.content_type('product')
        
        ==============================
        """

        from contentstack import ContentType
        if content_type_id is not None and isinstance(content_type_id, str) and len(content_type_id) > 0:
            content_type = ContentType(content_type_id)
            content_type._instance(self)
            return content_type
        else:
            raise StackException('Kindly provide valid content_type')

    def get_content_types(self, query_params):

        """
        Fetches all Content Types from the Stack.
        This call returns comprehensive information
        of all the content types available in a
        particular stack in your account.
        API Reference: https://www.contentstack.com/docs/apis/content-delivery-api/#content-types

        :return: ContentTypes dict response
        :rtype:  dict
        
        ==============================
        
        [Example]:

        >>> content_types = stack.get_content_types()
        
        ==============================
        """

        content_type_params: dict = {}
        if self.config is None:
            raise StackException('Kindly initialise stack')
        endpoint = self.config.endpoint
        url = '{}/content_types'.format(endpoint)
        if query_params is not None and isinstance(query_params, dict):
            content_type_params = query_params.copy()
        result = self.__http_request.get_result(url, content_type_params, self.__stack_headers)
        return result

    def asset(self, uid=None):

        """
        :param uid: asset uid is unique_id of the asset
        :type uid: str
        :return: asset file of the stack
        :rtype: <contentstack.asset.Asset>

        ==============================
        
        [Example]: [All Assets]
        Assets refer to all the media files (images, videos, PDFs, audio files, and so on)
        uploaded in your Contentstack repository for future use. These files can be
        attached and used in multiple entries. Learn more about Assets.
        Keep uid None to fetch list of all assets
        API Reference : https://www.contentstack.com/docs/guide/content-management#working-with-assets

        >>> asset_instance = stack.asset()
        >>> assets = asset_instance.fetch_all()
        
        ==============================
        ==============================
        
        [Example]: [Asset]
        This call fetches the latest version of a specific asset of a particular stack.
        provide asset_uid of the asset you have to find.
        Example: in case to fetch single asset, provide uid of the asset:

        >>> asset_instance = stack.asset('bltputyourassetuid')
        >>> asset = asset_instance.fetch()
        
        ==============================
        """

        from contentstack import Asset
        asset = Asset(uid=uid)
        asset._instance(self)
        return asset

    def image_transform(self, image_url: str, **kwargs):

        """
        :param image_url: on which we want to manipulate.
        :type image_url: str
        :param kwargs: this parameter in which we want to place different manipulation key-worded, variable-length argument list
        :type kwargs: str
        :return: image_url
        :rtype:str

        ==============================

        [Example]: The Image Delivery API is used to retrieve, manipulate and/or convert image
        files of your Contentstack account and deliver it to your web or mobile properties.
        It is an second parameter in which we want to place different manipulation key and
        value in array form ImageTransform method is define for image manipulation with
        different transform_params in second parameter in array form

        >>> stack.image_transform('image_url', width=100, height=100)

        ==============================
        """

        self.__image_transform_url = image_url
        self.__image_params = kwargs
        args = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
        if args:
            self.__image_transform_url += '?{0}'.format('&'.join(args))
        return self.__image_transform_url

    def collaborators(self):

        """
        :return: self, collaborators with whom the stacks are shared.
        A detailed information about each collaborator is returned.
        :rtype: <contentstack.Stack>

        ==============================

        [Example]: collaborators with whom the stacks are shared

        >>> stack = stack.collaborators()

        ==============================
        """

        self.__query_params['include_collaborators'] = 'true'

        return self

    def include_stack_variables(self):

        """
        :returns stack_variables

        ==============================

        [Example]: Stack variables are extra information about the stack,
        such as the description, format of date, format of time, and so on.
        Users can include or exclude stack variables in the response.

        >>> stack = stack.include_stack_variables()

        ==============================
        """

        self.__query_params['include_stack_variables'] = 'true'

        return self

    def include_discrete_variables(self):

        """
        :returns discrete variables of the stack

        ==============================

        [Example]:
        >>> stack = stack.include_discrete_variables()

        ==============================
        """

        self.__query_params['include_discrete_variables'] = 'true'

        return self

    def include_count(self):

        """
        It includes Count of stack response
        :return: self
        :rtype: Stack

        ==============================

        [Example]:
        >>> stack = stack.include_count()

        ==============================
        """

        self.__query_params['include_count'] = 'true'

        return self

    def fetch(self):
        url = '{}/stacks'.format(self.config.endpoint)
        result = self.__http_request.get_result(url, self.__query_params, self.__stack_headers)
        return result

    def sync(self, **kwargs):

        """
        :content_type_uid:  You can also initialize sync with entries of
        only specific content_type. To do this, use syncContentType and specify
        the content type uid as its value. However, if you do this,
        the subsequent syncs will only include the entries of the specified content_type.

        :from_date: You can also initialize sync with entries published
        after a specific date. To do this, use from_date
        and specify the start date as its value.

        :locale: You can also initialize sync with entries of only specific locales.
        To do this, use syncLocale and specify the locale code as its value.
        However, if you do this, the subsequent syncs will only include
        the entries of the specified locales.

        :publish_type:  Use the type parameter to get a specific type of content.
        You can pass one of the following values:

        asset_published, entry_published, asset_unpublished,
        asset_deleted, entry_unpublished, entry_deleted,
        content_type_deleted.

        If you do not specify any value, it will bring all published entries and published assets.

        ==============================

        [Explanation]:
        :param kwargs: content_type_uid='blt83847327434739', from_date='date', locale='en-us',
        publish_type='asset_published'
        :type kwargs: key-worded, variable-length argument list
        :return: list of SyncResult Object
        :rtype: list[SyncResult]

        [Example]:
        >>> result = stack.sync(content_type_uid='content_type_uid', from_date='date', locale='en-us', publish_type='asset_published')
        
        ==============================
        """

        self.__sync_query["init"] = 'true'
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                self.__sync_query[key] = value
        if self.__stack_headers is not None and len(self.__stack_headers) > 0:
            if 'environment' in self.__stack_headers:
                env = self.__stack_headers['environment']
                self.__sync_query['environment'] = env
        else:
            raise KeyError("Kindly provide stack headers")
        return self.__sync_request()

    def pagination(self, pagination_token):

        """
        If the result of the initial sync (or subsequent sync) contains more than 100 records, the response would be
        paginated. It provides pagination token in the response. However, you do not have to use the pagination token
        manually to get the next batch, the SDK does that automatically until the sync is complete. Pagination token
        can be used in case you want to fetch only selected batches. It is especially useful if the sync process is
        interrupted midway (due to network issues, etc.). In such cases, this token can be used to restart the sync
        process from where it was interrupted.

        ==============================

        [Explanation]:
        :param pagination_token: It can be found in the sync response
        :type pagination_token: str
        :return: list of SyncResult object
        :rtype: list[SyncResult]

        [Example]:

        >>> result = stack.pagination('blt8347235938759')

        ==============================
        """

        if isinstance(pagination_token, str):
            self.__sync_query = {'pagination_token': pagination_token}
        else:
            raise StackException('Kindly provide valid pagination_token')
        return self.__sync_request()

    def sync_token(self, sync_token):

        """
        You can use the sync token (that you receive after initial sync)
        to get the updated content next time.
        The sync token fetches only the content that was added after your last sync,
        and the details of the content that was deleted or updated.

        ==============================

        [Explanation]:
        :param sync_token: The sync token fetches only the content that was added after your last sync
        :type sync_token:
        :return: list of SyncResult object
        :rtype: list[SyncResult]

        [Example]:

        >>> result = stack.sync_token('bltsomekeytoput')

        ==============================
        """

        if isinstance(sync_token, str):
            self.__sync_query = {'sync_token': sync_token}
        else:
            raise StackException('Kindly provide valid sync_token')
        return self.__sync_request()

    def __sync_request(self):
        # This is useful to find sync_request for the stack
        url = '{}/stacks/sync'.format(self.config.endpoint)
        result = self.__http_request.get_result(url, self.__sync_query, self.__stack_headers)
        return result


class SyncResult:

    def __init__(self):
        self.__resp: dict = {}
        self.__items: list = []
        self.__skip = int
        self.__limit = int
        self.__total_count = int
        self.__sync_token = str
        self.__pagination_token = str

    def _configure(self, result: dict):
        if result is not None and len(result) > 0:
            self.__resp = result
            if 'items' in self.__resp:
                self.__items = self.__resp['items']
            if 'skip' in self.__resp:
                self.__skip = self.__resp['skip']
            if 'limit' in self.__resp:
                self.__limit = self.__resp['limit']
            if 'total_count' in self.__resp:
                self.__total_count = self.__resp['total_count']
            if 'sync_token' in self.__resp:
                self.__sync_token = self.__resp['sync_token']
            if 'pagination_token' in self.__resp:
                self.__pagination_token = self.__resp['pagination_token']
        return self

    @property
    def json(self):
        return self.__resp

    @property
    def items(self):
        return self.__items

    @property
    def skip(self):
        return self.__skip

    @property
    def limit(self):

        """
        :return: This property returns limit
        :rtype: int

        ==============================

        Example:
        limit = SyncResult.limit

        ==============================
        """
        return self.__limit

    @property
    def count(self):

        """
        :return: This property returns count
        :rtype: int

        ==============================

        Example:
        count = SyncResult.count

        ==============================
        """
        return self.__total_count

    @property
    def sync_token(self):

        """
        :return: This property returns sync_token
        :rtype: str

        ==============================

        Example:
        sync_token = SyncResult.sync_token

        ==============================
        """
        return self.__sync_token

    @property
    def pagination_token(self):

        """
        :return: This property returns pagination_token
        :rtype: str
        
        ==============================

        Example:
        pagination_token = SyncResult.pagination_token

        ==============================
        """
        return self.__pagination_token
