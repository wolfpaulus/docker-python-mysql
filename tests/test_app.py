""" Unit test for the database number count."""
from app import create_random_numbers, CONFIG
from db_utils import initialize_db, fetch_numbers, insert_random_numbers


def test_number_count():
    """Test the number count generation."""
    assert len(create_random_numbers()) == 10
    assert len(create_random_numbers(5)) == 5
    assert len(create_random_numbers(0)) == 0
    assert len(create_random_numbers(-1)) == 0


def test_db_operations():
    """Test the database operations."""
    initialize_db(CONFIG)
    lol = fetch_numbers(CONFIG)
    k = len(lol[-1]) if lol else 0
    my_list = create_random_numbers(k+1)
    insert_random_numbers(CONFIG, my_list)
    lol_new = fetch_numbers(CONFIG)
    assert len(lol_new) == len(lol) + 1
    assert lol_new[-1] == my_list
