from unittest.mock import patch
from tests.test_Bookkeeping.bookkeeping_data import people, documents, directories, shelf, list_, add_shelf, move, add, delete


class TestSomething:  # unlike unittest, we do not inherit from anyone
    documents = documents
    directories = directories

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print("method setup")

    @patch('builtins.input')
    def test_1_people(self, m_input):
        m_input.side_effect = ['11-2']
        assert people() == 'Владельцем этого документа является Геннадий Покемонов.'

    @patch('builtins.input')
    def test_2_shelf(self, m_input):
        m_input.side_effect = ['10006']
        assert shelf() == 'Этот документ находится на полке № 2.'

    @patch('builtins.input')
    def test_3_list_(self, m_input):
        m_input.side_effect = ['2207 876234']
        assert list_() == 'Тип документа - passport, номер - 2207 876234, ' \
                          'владелец - Василий Гупкин.'

    @patch('builtins.input')
    def test_4_add_shelf(self, m_input):
        m_input.side_effect = ['4']
        assert add_shelf() == f'\nВы успешно создали новую полку № 4. \nВот ' \
                              f'обновленный список полок: {directories}'

    @patch('builtins.input')
    def test_5_move(self, m_input):
        m_input.side_effect = ['11-2', '3']
        assert move() == f'\nВот так сейчас выглядит текущий список ' \
                         f'полок с содержимым: \n{directories}'

    @patch('builtins.input')
    def test_6_add(self, m_input):
        m_input.side_effect = ['Visa', '333', 'Bob Love', '3']
        assert add() == f'\nВот обновленная информация по полкам. Вы добавили объект на полку ' \
                        f'№3: \n{directories} \n\nВот обновленная информация по каталогу. ' \
                        f'Новый объект находится в конце списка: \n{documents}'

    @patch('builtins.input')
    def test_7_delete(self, m_input):
        m_input.side_effect = ['3335']
        assert delete() == '\nВы указали несуществующий номер документа. ' \
                           'Пожалуйста, будьте внимательней и попробуйте еще раз.'

    def teardown_class(self):
        print('method teardown_class')

    def teardown(self):
        print("method teardown")
