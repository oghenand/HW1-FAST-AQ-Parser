# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcribed_seq = ''
    for nuceleotide in seq:
        if nuceleotide not in ALLOWED_NUC:
            raise ValueError(f'Invalid nucleotide: {nuceleotide}')
        transcribed_seq += TRANSCRIPTION_MAPPING[nuceleotide]
    if reverse:
        return transcribed_seq[::-1]
    return transcribed_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse=True)