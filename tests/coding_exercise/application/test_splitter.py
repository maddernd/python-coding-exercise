import pytest
from assertpy import assert_that
from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable

def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()

# Additional test cases to gain 100% coverage

def test_should_split_evenly():
    result = Splitter().split(Cable(10, "coconuts"), 2)
    assert_that([c.length for c in result]).is_equal_to([5, 5])
    assert_that([c.name for c in result]).is_equal_to(["coconuts-00", "coconuts-01"])

def test_should_split_with_remainder():
    result = Splitter().split(Cable(10, "coconuts"), 3)
    assert_that([c.length for c in result]).is_equal_to([4, 3, 3])
    assert_that([c.name for c in result]).is_equal_to(["coconuts-00", "coconuts-01", "coconuts-02"])

def test_should_split_minimum_length():
    result = Splitter().split(Cable(2, "coconuts"), 1)
    assert_that([c.length for c in result]).is_equal_to([2])
    assert_that([c.name for c in result]).is_equal_to(["coconuts-00"])

def test_should_raise_error_for_invalid_split():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 0)
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(1, "coconuts"), 2)

def test_should_handle_maximum_splits():
    result = Splitter().split(Cable(64, "coconuts"), 64)
    assert_that(result).is_length(64)
    assert_that(set([c.length for c in result])).is_equal_to({1})

def test_should_handle_large_number_of_splits():
    result = Splitter().split(Cable(100, "coconuts"), 7)
    assert_that([c.length for c in result]).is_equal_to([15, 15, 14, 14, 14, 14, 14])
    assert_that([c.name for c in result]).is_equal_to(
        ["coconuts-00", "coconuts-01", "coconuts-02", "coconuts-03", 
         "coconuts-04", "coconuts-05", "coconuts-06"]
    )

def test_should_raise_error_for_split_length_less_than_1():
    with pytest.raises(ValueError, match="Cannot split the cable segments less than 1"):
        Splitter().split(Cable(2, "coconuts"), 3)
