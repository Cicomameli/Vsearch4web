#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def search4vowels(phrase: str) -> set:
    """Return any vowels found in supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of th 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
