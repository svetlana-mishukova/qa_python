import pytest

from books_collector import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book(self, books_collector):
        books_collector.add_new_book('Смех лисы')
        assert 'Смех лисы' in books_collector.books_genre
                

    def test_add_re_booking(self, books_collector):  #проверка на добавление одной и той же книги, можно добавить только один раз
        books_collector.add_new_book('Братья Карамазовы')
        books_collector.add_new_book('Братья Карамазовы')
        assert len(books_collector.books_genre) == 1

    
    def test_set_book_genre(self, books_collector):
        book_name = 'Мы'
        book_genre = 'Фантастика'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)
        assert books_collector.books_genre[book_name] == book_genre
           

    def test_get_book_genre(self, books_collector):
        name_book = 'Приключения Шерлока Холмса'
        genre = 'Детективы'
        books_collector.add_new_book(name_book)
        books_collector.set_book_genre(name_book, genre)
        assert books_collector.get_book_genre(name_book) == genre

    
    def test_get_books_with_specific_genre(self, books_collector):  #проверка на вывод списка книг с определённым жанром
        books_collector.add_new_book('Юмористические рассказы')
        books_collector.set_book_genre('Юмористические рассказы', 'Комедии')
        result = books_collector.get_books_with_specific_genre('Комедии')
        assert result == ['Юмористические рассказы']


    def test_get_books_genre(self, books_collector):  #проверка на вывод текущего словаря books_genre
        books_collector.add_new_book('Коллекционер')
        books_collector.add_new_book('Дюна')
        books_collector.set_book_genre('Коллекционер', 'Детективы')
        books_collector.set_book_genre('Дюна', 'Фантастика')
        result = {
            'Коллекционер': 'Детективы',
            'Дюна': 'Фантастика'
        }
        assert books_collector.books_genre == result


    def test_get_books_for_children(self, books_collector):
        book_name = 'Каникулы в Простоквашино'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Мультфильмы')
        result = books_collector.get_books_for_children()
        assert book_name in result

    
    def test_add_book_in_favorites(self, books_collector):
        book_name = 'Сказки-мультфильмы'
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert book_name in books_collector.favorites


    def test_delete_book_from_favorites(self, books_collector):   #проверка на удаление книги из избранного
        book = books_collector.add_new_book('Божественная Комедия')
        books_collector.add_book_in_favorites(book)
        books_collector.delete_book_from_favorites(book)
        assert book not in books_collector.favorites


    def test_get_list_of_favorites_books(self, books_collector):
        book_1 = books_collector.add_new_book('Убийство в Восточном экспрессе')
        book_2 = books_collector.add_new_book('Блуждающая Земля')
        books_collector.add_book_in_favorites(book_1)
        books_collector.add_book_in_favorites(book_2)
        favorites_list = books_collector.get_list_of_favorites_books()
        assert isinstance(favorites_list, list)