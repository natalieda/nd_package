#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the nd_package module.
"""
import pytest

from nd_package import nd_package


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_nd_package(an_object):
    assert an_object == {}
