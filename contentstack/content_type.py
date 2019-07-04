"""
   MIT License

   Copyright (c) 2012 - 2019 Contentstack
 
     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the "Software"), to deal
     in the Software without restriction, including without limitation the rights
     to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
     copies of the Software, and to permit persons to whom the Software is
     furnished to do so, subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.
 
     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
     SOFTWARE.
 """
from contentstack import http_request, Entry
from contentstack.query import Query
# from contentstack.entry import Entry
from contentstack.stack import Stack


class ContentType(Stack):

    def __init__(self, content_type_uid: str):

        self._entry_instance: Entry
        self._query_instance: Query
        self._entry_uid: str = ''
        self._content_type_uid = content_type_uid
        self._entry_instance = Entry(content_type_id=self._content_type_uid, entry_uid=self._entry_uid)
        self._query_instance = Query(self._content_type_uid)

        self._stack_headers = Stack.get_headers()
        self._local_params: dict = {}

    def set_header(self, key, value):
        if key is not None and value is not None:
            self._stack_headers[key] = value

    def remove_header(self, key):
        if key in self._stack_headers:
            self._stack_headers.pop(key)

    def entry(self, entry_uid: str = None):
        """
        An entry is the actual piece of content created using one of the defined content types.
        Read more about Entries. [ https://www.contentstack.com/docs/apis/content-delivery-api/#entries ]

        The Get all entries call fetches the list of all the entries of a particular content type.
        It also returns the content of each entry in JSON format.
        You can also specify the environment and locale of which you wish to get the entries.

        :param entry_uid:
        :return:
        """
        self._entry_uid = entry_uid
        if self._entry_uid is not None:
            self._entry_instance.set_entry_uid(self._entry_uid)
        entry_url = self._get_entry_url()
        self._entry_instance.set_content_type_instance(entry_url, self._stack_headers)
        return self._entry_instance

    def query(self):

        """
        You can add queries to extend the functionality of this API call. 
        Under the URI Parameters section, insert a parameter named query 
        and provide a query in JSON format as the value.
        To learn more about the queries, refer to the Queries section.
        """
        return self._query_instance

    def fetch(self) -> tuple:
        ct_request = http_request.HTTPRequestConnection(self._get_content_type_url(), self._local_params, self._stack_headers)
        return ct_request.http_request()

    # def find_entries(self) -> dict:
    # https_request = http_request.HTTPRequestConnection(self._get_entries_url(), self._local_params, self.stack_headers)
    # result = https_request.http_request()
    # return result

    def _get_content_type_url(self) -> str:
        return 'content_types/{0}'.format(self._content_type_uid)

    def _get_entry_url(self) -> str:
        return 'content_types/{0}/entries/{1}'.format(self._content_type_uid, self._entry_uid)

    # def _get_entries_url(self) -> str:
    #    return 'content_types/{0}/entries'.format(self.content_type_uid)
