#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:14:54 2019

@author: lorak

"""
import argparse
import time
from os.path import isfile
from re import match


def deco(message=''):
    def new_arg(message):
        return input(f'{message}\n')

    def counter(func, count_max=5):
        '''decorator. if return == None - want to input another 1st arg'''
        def wrapper(*args):
            args = [*args]
            count = 0
            while count < count_max:
                count += 1
                if args[0].lower() == 'exit':
                    return
                answer = func(*args)
                if answer:
                    return answer
                args[0] = new_arg(message)
        return wrapper
    return counter


def test_type(*test_type):
    '''function test for type args'''
    def f(func):
        def wrap(*args):
            x = 0
            for i in args:
                if type(i) == test_type[x] and i:
                    x += 1
                    continue
                return
            return func(*args)
        return wrap
    return f


def get_args():
    '''function to get args from terminal'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lang', type=str, default='ru')
    parser.add_argument('-d', '--dict', type=str,
                        default='./library/languages.txt')
    return parser.parse_args()


def get_time():
    return int(time.strftime('%H', time.localtime()))//6


@deco(message='input another dict')
@test_type(str)
def data_test(data):
    ''' function test to file in sistem'''
    data = data.rstrip()
    answer = isfile(data)
    if answer:
        return data


def read_file(data):
    with open(data, 'r') as f:
        data = f.readlines()
    return data


@deco(message='input another lang')
@test_type(str, list)
def hello_list_str(lang, data):
    ''' function seek key in datafile'''
    pattern = r'{},'.format(lang)
    for item in data:
        if match(pattern, item):
            return item


@test_type(str)
def hello_words_list(data):
    '''function return list from string'''
    data = [x for x in data.split(',')[1:]]
    return data if data else None


@test_type(list, int)
def get_hello_word(data, key):
    if 0 <= key <= len(data):
        return data[key]


@test_type(str)
def prepare_to_print(mess):
    mess = '{}!'.format(mess.capitalize().rstrip())
    return mess


if __name__ == '__main__':
    args = get_args()
    key = get_time()
    data = data_test(args.dict)
    if data:
        read_data = read_file(data)
        hello_list = hello_list_str(args.lang, read_data)
        words_list = hello_words_list(hello_list)
        final_word = get_hello_word(words_list, key)
        message = prepare_to_print(final_word)
        print(message or 'Nothing to print')
    else:
        print('please, check dict')
