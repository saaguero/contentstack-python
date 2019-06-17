"""
 * MIT License
 *
 * Copyright (c) 2012 - 2019 Contentstack
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 """

import logging


class Config(object):

    SDK_VERSION = 'contentstack-python[0.0.1]'

    def __init__(self):
        self.host_url = 'cdn.contentstack.io'
        self.api_version = 'v3'
        self.environment = None
        self.SDK_VERSION = "0.0.1"
        self.SDK_NAME = 'contentstack-python'

    def set_host(self, host_url='cdn.contentstack.io'):
        logging.info("set host")
        if host_url != None:
            self.url = host_url
            return self

    def set_environment(self, environment):
        logging.info("set environment")
        if environment != None:
            self.environment = environment
            return self

    def get_host(self):
        logging.info('getting host url')
        return self.host_url

    def get_version(self):
        logging.info('getting api version')
        return self.api_version

    def get_environment(self):
        logging.info('get invironment')
        return self.environment
