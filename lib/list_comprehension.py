#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if not num % 2]

def make_exclamation(sentence_list):
    return [word + "!" for word in sentence_list]