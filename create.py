# coding: utf-8
import os

DOC_DIR = 'doc'
BLOG_DIR_INDEX = 'doc/blog'
BLOG_DIR_SEN = 'blog'
BLOG_RST = '{}/blog.rst'.format(DOC_DIR)
BLANK = '    '

# .. gdb
# .. toctree::
#    :maxdepth: 2
#    :caption: gdb
#    :glob:
#
#    doc/gdb


def write(data_str, file_name, model='w',):
	with open(file_name, model) as f:
		f.writelines(data_str)


def index_conf(caption, file_dir, name,  max_depth=2):
	assert file_dir
	title = '{}\n====================\n\n'.format(name)
	body_line1 = '.. toctree::\n'
	body_line2 = '{}:maxdepth: {}\n'.format(BLANK, max_depth)
	body_line3 = '{}:caption: {}\n'.format(BLANK, name)
	body_line4 = '{}:glob: \n\n'.format(BLANK)
	body_line5 = '{}{}\n\n'.format(BLANK, file_dir)

	return title + body_line1 + body_line2 + body_line3 + body_line4 + body_line5


def find_blog(file_dir):
	data_str = ''
	for f_dir in os.listdir(file_dir):
		one_dir = '{}/{}/*'.format(BLOG_DIR_SEN, f_dir)
		data_str += index_conf(f_dir, one_dir, f_dir,)
	return data_str


if __name__ == '__main__':
	rst_str = find_blog(BLOG_DIR_INDEX)
	write(rst_str, BLOG_RST)

