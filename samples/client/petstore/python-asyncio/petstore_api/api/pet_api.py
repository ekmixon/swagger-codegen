# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from petstore_api.api_client import ApiClient


class PetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_pet(self, body, **kwargs):    # noqa: E501
        """Add a new pet to the store  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_pet(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_pet_with_http_info(body, **kwargs)  # noqa: E501

    def add_pet_with_http_info(self, body, **kwargs):    # noqa: E501
        """Add a new pet to the store  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_pet_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'body',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_pet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_pet`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}

        body_params = None
        body_params = params['body']
        header_params = {
            'Accept': self.api_client.select_header_accept(
                ['application/xml', 'application/json']
            )
        }

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/pet', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_pet(self, pet_id, **kwargs):    # noqa: E501
        """Deletes a pet  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pet(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: Pet id to delete (required)
        :param str api_key:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_pet_with_http_info(pet_id, **kwargs)  # noqa: E501

    def delete_pet_with_http_info(self, pet_id, **kwargs):    # noqa: E501
        """Deletes a pet  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pet_with_http_info(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: Pet id to delete (required)
        :param str api_key:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'pet_id',
            'api_key',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params or
                params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `delete_pet`")  # noqa: E501

        collection_formats = {}

        path_params = {'petId': params['pet_id']}
        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/pet/{petId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_pets_by_status(self, status, **kwargs):    # noqa: E501
        """Finds Pets by status  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_pets_by_status(status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_pets_by_status_with_http_info(status, **kwargs)  # noqa: E501

    def find_pets_by_status_with_http_info(self, status, **kwargs):    # noqa: E501
        """Finds Pets by status  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_pets_by_status_with_http_info(status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'status',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_pets_by_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `find_pets_by_status`")  # noqa: E501

        path_params = {}

        query_params = [('status', params['status'])]
        collection_formats = {'status': 'csv'}
        form_params = []
        local_var_files = {}

        body_params = None
        header_params = {
            'Accept': self.api_client.select_header_accept(
                ['application/xml', 'application/json']
            )
        }

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/pet/findByStatus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Pet]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_pets_by_tags(self, tags, **kwargs):    # noqa: E501
        """Finds Pets by tags  # noqa: E501

        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_pets_by_tags(tags, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] tags: Tags to filter by (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_pets_by_tags_with_http_info(tags, **kwargs)  # noqa: E501

    def find_pets_by_tags_with_http_info(self, tags, **kwargs):    # noqa: E501
        """Finds Pets by tags  # noqa: E501

        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_pets_by_tags_with_http_info(tags, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] tags: Tags to filter by (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'tags',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_pets_by_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tags' is set
        if ('tags' not in params or
                params['tags'] is None):
            raise ValueError("Missing the required parameter `tags` when calling `find_pets_by_tags`")  # noqa: E501

        path_params = {}

        query_params = [('tags', params['tags'])]
        collection_formats = {'tags': 'csv'}
        form_params = []
        local_var_files = {}

        body_params = None
        header_params = {
            'Accept': self.api_client.select_header_accept(
                ['application/xml', 'application/json']
            )
        }

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/pet/findByTags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Pet]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pet_by_id(self, pet_id, **kwargs):    # noqa: E501
        """Find pet by ID  # noqa: E501

        Returns a single pet  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pet_by_id(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: ID of pet to return (required)
        :return: Pet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_pet_by_id_with_http_info(pet_id, **kwargs)  # noqa: E501

    def get_pet_by_id_with_http_info(self, pet_id, **kwargs):    # noqa: E501
        """Find pet by ID  # noqa: E501

        Returns a single pet  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pet_by_id_with_http_info(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: ID of pet to return (required)
        :return: Pet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'pet_id',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pet_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params or
                params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `get_pet_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {'petId': params['pet_id']}
        query_params = []

        form_params = []
        local_var_files = {}

        body_params = None
        header_params = {
            'Accept': self.api_client.select_header_accept(
                ['application/xml', 'application/json']
            )
        }

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/pet/{petId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Pet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_pet(self, body, **kwargs):    # noqa: E501
        """Update an existing pet  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pet(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_pet_with_http_info(body, **kwargs)  # noqa: E501

    def update_pet_with_http_info(self, body, **kwargs):    # noqa: E501
        """Update an existing pet  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pet_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'body',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_pet`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}

        body_params = None
        body_params = params['body']
        header_params = {
            'Accept': self.api_client.select_header_accept(
                ['application/xml', 'application/json']
            )
        }

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/pet', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_pet_with_form(self, pet_id, **kwargs):    # noqa: E501
        """Updates a pet in the store with form data  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pet_with_form(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: ID of pet that needs to be updated (required)
        :param str name: Updated name of the pet
        :param str status: Updated status of the pet
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_pet_with_form_with_http_info(pet_id, **kwargs)  # noqa: E501

    def update_pet_with_form_with_http_info(self, pet_id, **kwargs):    # noqa: E501
        """Updates a pet in the store with form data  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pet_with_form_with_http_info(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: ID of pet that needs to be updated (required)
        :param str name: Updated name of the pet
        :param str status: Updated status of the pet
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'pet_id',
            'name',
            'status',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pet_with_form" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params or
                params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `update_pet_with_form`")  # noqa: E501

        collection_formats = {}

        path_params = {'petId': params['pet_id']}
        query_params = []

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'status' in params:
            form_params.append(('status', params['status']))  # noqa: E501

        body_params = None
        header_params = {
            'Accept': self.api_client.select_header_accept(
                ['application/xml', 'application/json']
            )
        }

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/pet/{petId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_file(self, pet_id, **kwargs):    # noqa: E501
        """uploads an image  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: ID of pet to update (required)
        :param str additional_metadata: Additional data to pass to server
        :param file file: file to upload
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_file_with_http_info(pet_id, **kwargs)  # noqa: E501

    def upload_file_with_http_info(self, pet_id, **kwargs):    # noqa: E501
        """uploads an image  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file_with_http_info(pet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pet_id: ID of pet to update (required)
        :param str additional_metadata: Additional data to pass to server
        :param file file: file to upload
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'pet_id',
            'additional_metadata',
            'file',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params or
                params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `upload_file`")  # noqa: E501

        collection_formats = {}

        path_params = {'petId': params['pet_id']}
        query_params = []

        form_params = []
        local_var_files = {}
        if 'additional_metadata' in params:
            form_params.append(('additionalMetadata', params['additional_metadata']))  # noqa: E501
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        header_params = {
            'Accept': self.api_client.select_header_accept(['application/json'])
        }

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/pet/{petId}/uploadImage', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
