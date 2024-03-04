import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.add_new_book('Винни Пух')
    collector.set_book_genre('Винни Пух', 'Мультфильмы')
    collector.add_new_book('Горе от ума')
    collector.set_book_genre('Горе от ума', 'Комедии')
    collector.add_new_book('Пуаро')
    collector.set_book_genre('Пуаро', 'Детективы')
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    return collector
