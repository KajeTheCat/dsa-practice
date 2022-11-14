import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()

    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()

    linked.linked_list_insert("apple")

    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.linked_list_insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.linked_list_insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.linked_list_insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.linked_list_insert("apple")
    linked_list.linked_list_insert("banana")

    assert linked_list.linked_list_includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.linked_list_insert("apple")
    linked_list.linked_list_insert("banana")

    assert not linked_list.linked_list_includes("cucumber")

# @pytest.mark.skip("TODO")
def test_reversed_two():
    linked = LinkedList()

    linked.linked_list_insert("banana")
    linked.linked_list_insert("apple")
    linked.linked_list_reverse()

    assert str(linked) == "{ banana } -> { apple } -> NULL"

# @pytest.mark.skip("TODO")
def test_reversed_five():
    linked = LinkedList()

    linked.linked_list_insert("explanation")
    linked.linked_list_insert("dog")
    linked.linked_list_insert("cantaloupe")
    linked.linked_list_insert("bronco")
    linked.linked_list_insert("apple")
    linked.linked_list_reverse()

    assert str(linked) == "{ explanation } -> { dog } -> { cantaloupe } -> { bronco } -> { apple } -> NULL"
