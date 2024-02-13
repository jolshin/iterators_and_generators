#tasks 1 solution

class FlatIterator:


    def __init__(self, nested_list):
        self._list = nested_list

    def __iter__(self):
        self._index = 0
        self._nested_index = -1
        return self
    
    def __next__(self):
        self._nested_index += 1

        if self._nested_index > len(self._list[self._index])-1:
            self._index += 1
            self._nested_index = 0


        if self._index == len(self._list):
            raise StopIteration

        return self._list[self._index][self._nested_index]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()