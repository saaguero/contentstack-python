#  Error
#  contentstack
#
#  Created by Shailesh Mishra on 22/06/19.
#  Copyright © 2019 Contentstack. All rights reserved.


class Error:
    """
    contentstack.error
    ~~~~~~~~~~~~~~~~~~
    This module implements the Error class.
    API Reference: https://www.contentstack.com/docs/apis/content-delivery-api/#error

    """

    def __init__(self):
        """

        """
        self.__error_dict = {}
        self.__error_code = str
        self.__msg = str
        self.__cause_err = str

    def config(self, result: dict):
        """

        :param result:
        :type result:
        :return:
        :rtype:
        """
        if result is not None and len(result) > 0:
            self.__error_dict = result
            self.__error_code = self.__error_dict['error_code']
            self.__msg = self.__error_dict['error_message']
            self.__cause_err = self.__error_dict['errors']
        return self

    @property
    def error_code(self):
        """
        It returns error code from the stack response
        :return: error_code as int
        :rtype: int

        Example. code = error.error_code

        """
        return self.__error_code

    @property
    def error_message(self):
        """
        Returns error_message from the stack response
        :return: error_message
        :rtype: str

        Example. error.error_message

        """

        return self.__msg

    @property
    def error(self):
        """
        This returns error code and error_message in dict formats
        :return: error dict
        :rtype: dict

        Example. error = error.error
        """

        return self.__cause_err

    @property
    def error_info(self) -> dict:
        """
        error information
        :return: error information
        :rtype: dict

        Example. error.error_info

        """
        return self.__error_dict

    errors_str = {

        'invalid_json': "Please provide valid JSON.",
        'api_key_is_none': "Stack api key can not be None.",
        'empty_content_type': "Please set contentType name.",
        'access_token_error': "Access token can not be None.",
        'environment_error': "Environment can not be None.",
        'connection_error': "Connection error",
        'auth_failure': "Authentication Not present.",
        'parse_error': "Parsing Error.",
        'server_error': "Server interaction went wrong, Please try again.",
        'error_default': "Oops! Something went wrong. Please try again.",
        'no_network': "Network not available.",
        'query_error': "Please provide valid params."
    }

    __error_code = {

        400: "The request was incorrect or corrupted.",
        401: "The login credentials are invalid.",
        403: "The page or resource that is being accessed is forbidden.",
        404: "The requested page or resource could not be found.",
        412: "The entered API key is invalid.",
        422: "The request is syntactically correct but contains semantic errors",
        429: "The number of requests exceeds the allowed limit for the given time period.",
        500: "The server is malfunctioning and is not specific on what the problem is.",
        502: "A server received an invalid response from another server.",
        504: "A server did not receive a timely response from another server that it was accessing while attempting "
             "to load the web page or fill another request by the browser. "
    }

    @staticmethod
    def logging_config(level):
        print('level ' + level)


class ConfigError(Exception):
    pass


class StackException(Exception):
    pass


class ContentstackError(Exception):
    pass


class NotSupportedException(Exception):
    pass


class RequestsWarning(Warning):
    """Base warning for Requests."""
    pass


class FileModeWarning(RequestsWarning, DeprecationWarning):
    """A file was opened in text mode, but Requests determined its binary length."""
    pass
