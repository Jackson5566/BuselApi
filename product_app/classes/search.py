import re
from product_app.models import ProductModel


def get_coincidences(element_list: list, search: list) -> int:
    count_number = sum(1 for element in search if element.lower() in element_list)
    return count_number


class Processor(object):
    vowel_separator = re.compile(r'[aeiou]+')

    def separate_by_vowels(self, string: str) -> list[str]:
        lista = self.vowel_separator.split(string)
        if not lista[-1] or lista[-1] is 's':
            lista.pop()
        return lista


class SearchAlgorithm():
    def __init__(self, request):
        self.request = request
        self.search_processor = Processor()
        self.search = self.request.query_params.get('search')
        self.list_coincidence = []

    def start_process(self):
        self.convert_search_to_work_string()
        self.set_coincidences_list()
        self.sort_coincidence_list()
        self.queryset = self.get_searched_posts()

    def set_coincidences_list(self):
        posts = ProductModel.objects.select_related('user')

        user_id = self.request.query_params.get('user__id')
        posts = (posts.filter(user__id=user_id) if user_id else posts.all()).order_by('-created')

        for element in posts:
            list_description = self.search_processor.separate_by_vowels(element.description.lower())
            list_name = self.search_processor.separate_by_vowels(element.name.lower())
            coincidences = (get_coincidences(list_name, search=self.search) + get_coincidences(list_description,
                                                                                                search=self.search))
            if coincidences > 0:
                self.list_coincidence.append([coincidences, element])

    def convert_search_to_work_string(self):
        self.search = self.search.strip().lower()
        self.search = self.search_processor.separate_by_vowels(self.search)
        self.search = self.delete_repetitive_words()

    def sort_coincidence_list(self):
        self.list_coincidence.sort(key=lambda item: item[0], reverse=True)

    def delete_repetitive_words(self):
        return list(set(self.search))

    def get_searched_posts(self):
        list_unidimensional = [element[1] for element in self.list_coincidence]
        print(list_unidimensional)
        return list_unidimensional
