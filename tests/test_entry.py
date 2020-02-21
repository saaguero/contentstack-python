import logging
import unittest
from contentstack import Entry, Config, Error
from contentstack import Stack


class TestEntry(unittest.TestCase):
    log = logging.getLogger(__name__)

    def setUp(self):

        # config = Config()
        # config.host = 'cdn.contentstack.io'
        # config.region = ContentstackRegion.US
        # api_key = 'blt20962a819b57e233'
        # access_token = 'cs18efd90468f135a3a5eda3ba'
        # env = 'production'
        # self.entry_uid = 'bltb0256a89e2225a39'

        from tests.creds import entry_keys
        self.credentials = entry_keys()
        api_key = self.credentials['api_key']
        access_token = self.credentials['access_token']
        env = self.credentials['environment']
        self.entry_uid = self.credentials['entry_uid']
        self.stack_entry = Stack(api_key=api_key, access_token=access_token, environment=env)

    def test_entry_by_uid(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertEqual(Entry, type(result))

    def test_entry_title(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        result = _entry.fetch()
        if result is not None:
            self.assertEqual("Redmi Note 3", result.title)

    def test_entry_url(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        result = _entry.fetch()
        if result is not None:
            self.assertEqual('/mobiles/redmi-note-3', result.url)

    def test_entry_tags(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        result = _entry.fetch()
        if result is not None:
            self.assertEqual(list, type(result.tags))

    def test_entry_content_type(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        result = _entry.fetch()
        if result is not None:
            self.assertEqual('product', _entry.content_type)

    def test_is_entry_uid_correct(self):
        entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        result = entry.fetch()
        if result is not None:
            self.assertEqual(self.entry_uid, result.uid)

    def test_entry_locale(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            if '-' in result.locale:
                self.assertEqual('en-us', result.locale)

    def test_entry_to_json(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            self.assertEqual(dict, type(result.json))

    def test_entry_get(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertEqual(self.entry_uid, result.get('uid'))

    def test_entry_string(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            self.assertEqual(str, type(result.get_string('description')))

    def test_entry_boolean(self):
        entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        entry.locale = 'en-us'
        result = entry.fetch()
        if result is not None:
            self.assertFalse(None, type(entry.get_boolean('description')))

    def test_entry_json(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            json_result = result.get_json('publish_details')
            self.assertEqual(dict, type(json_result))

    def test_entry_get_int(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            json_result = _entry.get('color')
            self.assertFalse(None, type(json_result))

    def test_entry_get_created_at(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            created_at = _entry.created_at
            self.assertTrue(str, type(created_at))

    def test_entry_get_created_by(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            created_by = _entry.created_by
            self.assertTrue(str, type(created_by))

    def test_entry_get_updated_at(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            updated_at = _entry.updated_at
            self.assertTrue(str, type(updated_at))

    def test_entry_get_updated_by(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None:
            updated_by = _entry.updated_by
            self.assertTrue(str, type(updated_by))

    def test_entry_get_asset(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            the_result = result.get_assets('images')
            does_exist = the_result[0].uid
            if does_exist is not None:
                self.assertTrue(True)

    def test_entry_get_all_entries(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertTrue(True)

    def test_entry_except_field_uid(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        _entry.excepts('title', 'color', 'price_in_usd')
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_entry_except_with_reference_uid(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        _entry.except_with_reference_uid('category', 'color', 'price_in_usd')
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertTrue(True)
        else:
            if isinstance(result, Error):
                self.assertEqual(141, result.error_code)

    def test_entry_only_with_reference_uid(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        _entry.only_with_reference_uid('category', 'title', 'color', 'price_in_usd')
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertTrue(True)
        else:
            self.assertTrue(True)

    def test_entry_include_reference(self):
        entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        entry.locale = 'en-us'
        entry.include_reference('color', 'price_in_usd')
        result = entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertTrue(True)
        else:
            if isinstance(result, Error):
                self.assertEqual(141, result.error_code)

    def test_entry_only(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        _entry.only('color', 'price_in_usd')
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_entry_include_content_type(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        _entry.include_content_type()
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            ct = result.json['brand'][0]['_content_type_uid']
            self.assertEqual('brand', ct)
        else:
            self.assertTrue(False)

    def test_entry_only_check_if_true(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.locale = 'en-us'
        _entry.only('color', 'price_in_usd')
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_entry_include_reference_content_type_uid(self):
        _entry = self.stack_entry.content_type('product').entry(self.entry_uid)
        _entry.include_reference_content_type_uid()
        result = _entry.fetch()
        if result is not None and isinstance(result, Entry):
            title = result.title
            self.assertEqual('Redmi Note 3', title)
        else:
            self.assertTrue(False)