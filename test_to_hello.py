#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:15:37 2019

@author: lorak
"""

import unittest
import hello_sec as hello


class Test_to_lang(unittest.TestCase):
    def test_to_print(self):
        data = ['привет', 'hello world']
        answer = ['Привет!', 'Hello world!']
        with self.subTest():
            for x in range(len(data)):
                self.assertEqual(answer[x], hello.prepare_to_print(data[x]))

    def test_to_get_hello_word(self):
        data = [([1, 2, 3, 4], 3),
                (['hi', 'my', 'dear'], 2)]
        answer = [4, 'dear']
        with self.subTest():
            for x in range(len(data)):
                self.assertEqual(answer[x], hello.get_hello_word(*data[x]))

    def test_to_hello_words_list(self):
        data = ['ru,some,words,hear', 'we,can,do,this']
        answer = [['some', 'words', 'hear'],
                  ['can', 'do', 'this']]
        with self.subTest():
            for x in range(len(data)):
                self.assertEqual(answer[x], hello.hello_words_list(data[x]))

    def test_to_hello_list_str(self):
        data = ['ru,доброй ночи,доброго утра,доброго дня,доброго вечера',
                'en,good night,good morning,good day,good evening']
        keys = ['ru', 'en']
        with self.subTest():
            for x in range(len(data)):
                self.assertEqual(data[x], hello.hello_list_str(keys[x], data))


class Negativ_Test_to_lang(unittest.TestCase):
    def test_to_print_negative(self):
        data = ['', [1, 2, 3, 4], 32, None, True]
        with self.subTest():
            for x in range(len(data)):
                self.assertEqual(None, hello.prepare_to_print(data[x]))

    def test_to_get_hello_word_negative(self):
        data = [([1, 2, 3, 4], -1),
                (['hi', 'my', 'dear'], 6),
                ([1, 2, 3, 4, 5], 'es'),
                ([1, 2, 3, 4], None),
                ([], 1)]
        with self.subTest():
            for x in range(len(data)):
                self.assertEqual(None, hello.get_hello_word(*data[x]))

    def test_to_hello_words_list_negative(self):
        data = [['list', 'item'], '', None, 198, 0, 'qwrtr']
        with self.subTest():
            for x in range(len(data)):
                self.assertEqual(None, hello.hello_words_list(data[x]))

# =============================================================================
#     def _test_to_hello_list_str_negative(self):
#         data = ['ru,доброй ночи,доброго утра,доброго дня,доброго вечера',
#                 'en,good night,good morning,good day,good evening']
#         keys = ['se', 'kor']
#         with self.subTest():
#             for x in range(len(data)):
#                 self.assertEqual(None, hello.hello_list_str(keys[x], data))
# 
# =============================================================================

if __name__ == '__main__':
    unittest.main()
