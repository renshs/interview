import pytest


from src.generators import pairs_generator_short
from src.generators import pairs_generator_fast
from src.generators import pairs_generator_m_e


def test_fast_wrong_type():
    with pytest.raises(TypeError):
        pairs_generator_fast("hello")


def test_short_wrong_type():
    with pytest.raises(TypeError):
        pairs_generator_short("hello")


def test_m_e_wrong_type():
    with pytest.raises(TypeError):
        pairs_generator_m_e("hello")


def test_fast_bad_arg():
    with pytest.raises(ValueError):
        pairs_generator_fast(-5)


def test_short_bad_arg():
    with pytest.raises(ValueError):
        pairs_generator_short(-5)


def test_m_e_bad_arg():
    with pytest.raises(ValueError):
        pairs_generator_m_e(-5)
