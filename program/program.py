
import os
import io
import sys
import argparse


path = '/home/vlad/Documents/python/Homeworks/program/'
files = os.listdir('/home/vlad/Documents/python/Homeworks/program/')
txt = list(filter(lambda x: x.endswith('.txt'), files))
word = 'hello world'


def search(txt, path, word):
	index = 0
	for i in txt:
		with io.open(i, 'r') as file:
			for index, line in enumerate(file):
				if word in line:
					print(path + i, ':  ', line,end ='')
					print('number_string: ', index)


search(txt, path, word)
