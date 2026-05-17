from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


def test_add_new_book_success():
    collector = BooksCollector()
    collector.add_new_book('Новая книга')
    assert 'Новая книга' in collector.get_books_genre()

def test_add_new_book_duplicate():
    collector = BooksCollector()
    collector.add_new_book('Дублирующая книга')
    collector.add_new_book('Дублирующая книга')  # Второе добавление
    books_count = len(collector.get_books_genre())
    assert books_count == 1  # Должна быть только одна запись

def test_set_book_genre_success():
    collector = BooksCollector()
    collector.add_new_book('Книга с жанром')
    collector.set_book_genre('Книга с жанром', 'Фантастика')
    genre = collector.get_book_genre('Книга с жанром')
    assert genre == 'Фантастика'

def test_get_book_genre():
    collector = BooksCollector()
    collector.add_new_book('Ищущая книга')
    collector.set_book_genre('Ищущая книга', 'Комедии')
    genre = collector.get_book_genre('Ищущая книга')
    assert genre == 'Комедии'

def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book('Детектив')
    collector.set_book_genre('Детектив', 'Детективы')
    books = collector.get_books_with_specific_genre('Детективы')
    assert 'Детектив' in books

def test_get_all_books_genres():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    all_books = collector.get_books_genre()
    assert len(all_books) == 2

def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book('Детская книга')
    collector.set_book_genre('Детская книга', 'Мультфильмы')
    child_books = collector.get_books_for_children()
    assert 'Детская книга' in child_books

def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book('Любимая книга')
    collector.add_book_in_favorites('Любимая книга')
    favorites = collector.get_list_of_favorites_books()
    assert 'Любимая книга' in favorites

def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book('Удаляемая книга')
    collector.add_book_in_favorites('Удаляемая книга')
    collector.delete_book_from_favorites('Удаляемая книга')
    favorites = collector.get_list_of_favorites_books()
    assert 'Удаляемая книга' not in favorites

def test_empty_favorites_list():
    collector = BooksCollector()
    empty_favorites = collector.get_list_of_favorites_books()
    assert empty_favorites == []


# Тесты граничных условий


def test_add_empty_book_name():
    collector = BooksCollector()
    collector.add_new_book('')
    books = collector.get_books_genre()
    assert not books

def test_add_long_book_name():
    collector = BooksCollector()
    long_title = 'СлишкомДлинноеНазваниеДляКниги' * 5
    collector.add_new_book(long_title)
    books = collector.get_books_genre()
    assert long_title not in books
