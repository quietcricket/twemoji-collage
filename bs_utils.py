import urllib
import re
import os
import uuid
import sys
import six

IS_LOCAL = sys.platform == 'darwin'

def save_base64(data):
    header = 'data:image/jpeg;base64,'
    fname = uuid.uuid4().hex + '.jpg'
    with open(fname, 'w') as fh:
        fh.write(data[len(header):].decode('base64'))
    return fname


def slug(input):
    return re.sub('\s+', '-', input.lower())

def add_paragraph(text, style=''):
    return ''.join(['<p %s>%s</p>' % (style, part) for part in re.split("\n+", text)])


def readable_number(num, single_thing='', plura_thing='',):
    """
    Convert numbers into human readable format e.g 1000000 to 1M
    :param num: the number
    :param single_thing: 1 apple
    :param plural_thing: 2 apples
    """
    if num is None:
        return ''

    # Add a space in front of the thing
    if single_thing:
        single_thing = ' ' + single_thing
    if plura_thing:
        plura_thing = ' ' + plura_thing

    # 0/1 thing
    if num <= 1:
        return '%i%s' % (num, single_thing)

    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    if magnitude == 0:
        return '%i%s' % (num, plura_thing)
    else:
        pattern = '%i%s%s' if str(num).endswith('0') else '%.1f%s%s'
        return pattern % (num, ['', 'K', 'M', 'B'][magnitude], plura_thing)


def init_jinja(env):
    env.globals['readable_number'] = readable_number
    env.globals['random'] = lambda: uuid.uuid4().hex
    env.filters['paragraph'] = add_paragraph
