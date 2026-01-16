# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # test: test for transcribe function
    SEQUENCE_BEFORE = 'AGCATAGCTACGTA'
    SEQUENCE_TRANSCRIBED = 'UCGUAUCGAUGCAU'
    sequence_from_function = transcribe(SEQUENCE_BEFORE)
    assert sequence_from_function == SEQUENCE_TRANSCRIBED, "Transcribe function does not return correct transcribed sequence."

    # test for empty strings
    assert transcribe('') == '', 'Transcribe does not handle empty strings correctly-- output is not empty string (but should be)'

    # test for single
    assert transcribe('A') == 'U', 'Transcribe does not handle single-length strings. Must return string of length 1 that is transcribed correctly!'

    # test for repeated nucleotides
    assert transcribe('A'*4) == 'U'*4, 'Transcribe does not handle repeated strings. Must return string of same length as input that is transcribed correctly.'

    # test for invalid nucleotides
    with pytest.raises(ValueError):
        transcribe('AR')



def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # test: test for transcribe function
    SEQUENCE_BEFORE = 'AGCATAGCTACGTA'
    SEQUENCE_TRANSCRIBED = 'UCGUAUCGAUGCAU'
    SEQUENCE_REVERSED = 'UACGUAGCUAUGCU'
    sequence_from_function = reverse_transcribe(SEQUENCE_BEFORE)
    assert sequence_from_function == SEQUENCE_REVERSED, "Reverse transcribe function does not return correct reverse sequence."

    # test for empty strings
    assert transcribe('') == '', 'Reverse transcribe does not handle empty strings correctly-- output is not empty string (but should be)'

    # test for single
    assert transcribe('A') == 'U', 'Reverse transcribe does not handle single-length strings. Must return string of length 1 that is transcribed correctly!'

    # test for repeated nucleotides
    assert transcribe('A'*4) == 'U'*4, 'Reverse transcribe does not handle repeated strings. Must return string of same length as input that is transcribed correctly.'

    # test for invalid nucleotides
    with pytest.raises(ValueError):
        transcribe('AR')