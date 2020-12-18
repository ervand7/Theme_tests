# Пример теста с помощью pytest
import pytest
from tests.test_Yandex_disk_create_folder.Yandex import creating_folder_on_yd, YANDEX_TOKEN


class TestSomething:  # unlike unittest, we do not inherit from anyone

    def setup_class(self):  # this preparatory method runs only 1 time
        print('method setup_class')

    def setup(self):  # we write setup instead setUp
        print("method setup")

    def teardown(self):  # we write teardown instead tearDown
        print("method teardown")

    # def test_yandex(self):
    #     assert creating_folder_on_yd('ziumn', YANDEX_TOKEN) == 201  # we already don't dave assertEqual, only assert

    # we also can check our functions at some parameters
    @pytest.mark.parametrize('first, second, result',
                             [('qwertyuio', YANDEX_TOKEN, 201), ('asdfghjkl', YANDEX_TOKEN, 201),
                              ('zxcvbnm,.', YANDEX_TOKEN, 201), ('.loikdmju', YANDEX_TOKEN, 201)])
    def test_yandex_parametrize(self, first, second, result):
        assert creating_folder_on_yd(first, second) == result

    def teardown_class(self):  # this final method runs only 1 time
        print('method teardown_class')
