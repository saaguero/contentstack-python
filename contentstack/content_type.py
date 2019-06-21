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
from contentstack import stack
from config import Config


class ContentType(object):

    def __init__(self, content_type_uid):
        self.stack_instance = stack
        self.content_type_id = content_type_uid
        self.local_header = dict()

    def set_stack_instance(self, stack):
        self.stack_instance = stack
        self.local_header = stack.__local_headers__

    def set_header(self, key, value):
        """
        headers can be added by key and respected values
        :returns self
        """
        self.local_header.update({key: value})

    def remove_header(self, header_key):
        """
        headers can be removed by key
        """
        if header_key in self.local_header:
            self.local_header.pop(header_key)

    def entry(self, entry_uid=None, content_type_id=None):

        '''
        [About]: An entry is the actual piece of content created 
        using one of the defined content types. Read more about Entries.
        
        [Single Entry] -->
        The Get a single entry request fetches a particular entry of a content type.
        [API Reference] : https://www.contentstack.com/docs/apis/content-delivery-api/#single-entry
        Implementation: 
        single_entry = stack.content_type('product').entry('entry_uid')
        
        [All Entries] : -->
        The Get all entries call fetches the list of all the entries 
        of a particular content type. It also returns the content of 
        each entry in JSON format. You can also specify the environment 
        and locale of which you wish to get the entries.
        [API Reference] : https://www.contentstack.com/docs/apis/content-delivery-api/#entries

        Implementation:
        entries = entry = stack.content_type('product').entry()
        '''
        if content_type_id != None:
            self.content_type_id = content_type_id
        if entry_uid != None:
            entry.set_uid(entry_uid)

        entry = entry.Entry(entry_uid=entry_uid, content_type_id=self.content_type_id)
        entry.set_content_type_instance(self)
        return entry

    def query(self):
        '''
        You can add queries to extend the functionality of this API call. 
        Under the URI Parameters section, insert a parameter named query 
        and provide a query in JSON format as the value.
        To learn more about the queries, refer to the Queries section.
        '''
        query = query.Query(self.content_type_id)
        # query.formHead =
        # query.setContentTypeInstance(this)
        return query

    def fetch(self, callback):

        return self.get_url()

    def get_url(self):
        self.__configs = Config()
        VERSION = self.__configs.get_version()
        http_schema = self.__configs.get_host()
        url = "/{0}/{1}/content_types/{2}".format(http_schema, VERSION, self.content_type_id)
        return url
