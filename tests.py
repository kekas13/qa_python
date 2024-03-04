import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        lenght = len(collector.get_books_genre())
        collector.add_new_book('Дети капитана Гранта')
        collector.add_new_book('Капитанская дочка')
        assert lenght != len(collector.get_books_genre())

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Винни Пух',
                                      'Горе от ума', 'Пуаро', 'Гарри Поттер'])
    def test_get_book_genre_check_genre(self, collector, name):
        assert collector.get_book_genre(name)

    def test_get_books_genre(self, collector):
        assert collector.get_books_genre()

    @pytest.mark.parametrize('genre, name', [('Фантастика', 'Гарри Поттер'),
                                             ('Ужасы', 'Гордость и предубеждение и зомби'),
                                             ('Детективы', 'Пуаро'),
                                             ('Мультфильмы', 'Винни Пух'),
                                             ('Комедии', 'Горе от ума')])
    def test_get_books_with_specific_genre(self, collector, genre, name):
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_for_children(self, collector):
        assert collector.get_books_for_children() == ['Винни Пух', 'Горе от ума', 'Гарри Поттер']

    def test_add_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Пуаро')
        collector.add_book_in_favorites('Гарри Поттер')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites(self, collector):
        collector.add_book_in_favorites('Пуаро')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.add_book_in_favorites('Пуаро')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Пуаро', 'Гарри Поттер']
