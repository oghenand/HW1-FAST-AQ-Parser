# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # test case 1: simple parsing
    test_file = 'data/test.fa'
    fasta_obj = FastaParser(test_file)
    # check that it properly reads a fasta file:
    list_records = list(fasta_obj) # list of fasta records
    assert len(list_records) > 0, 'Parser should return at least one record'
    for record in list_records:
        assert len(record) == 2, "Parser should return (header, sequence)"
        
        for value in record:
            assert isinstance(value, str) and len(value) > 0, "headers and sequence should be strings and of non-zero positive length"
    
    # test case 2: blank and corrupted files -- expected result of ValueError
    edge_case_files = ['tests/bad.fa', 'tests/blank.fa']
    for edge_case in edge_case_files:
        with pytest.raises(ValueError):
            fasta_obj = FastaParser(edge_case)
            list(fasta_obj)


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    test_file = 'data/test.fq'
    fasta_obj = FastaParser(test_file)
    list_records = list(fasta_obj)
    first_record = list_records[0]
    assert first_record[0] is None, 'header should be None if fastq file is read'


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # test case 1: simple parsing
    test_file = 'data/test.fq'
    fastq_obj = FastqParser(test_file)
    # check that it properly reads a fastq file:
    list_records = list(fastq_obj) # list of fastq records
    assert len(list_records) > 0, 'Parser should return at least one record'
    for record in list_records:
        assert len(record) == 3, "Parser should return (header, sequence, quality)"
        
        for value in record:
            assert isinstance(value, str) and len(value) > 0, "headers, sequence and quality, should be strings and of non-zero positive length"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    test_file = 'data/test.fa'
    fastq_obj = FastqParser(test_file)
    list_records = list(fastq_obj)
    first_record = list_records[0]
    assert first_record[0] is None, 'header should be None if fasta file is read'