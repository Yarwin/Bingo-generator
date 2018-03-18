#!/usr/bin/env python
import csv

import click
from io import StringIO

from bingo_generator import Bingo


@click.command()
@click.argument('title', nargs=1)
@click.argument('fields', nargs=-1, type=click.UNPROCESSED)
@click.option('--freespace', default='',
              help='Freespace field for your bingo')
@click.option('--size', default=5,
              help='Number of columns and rows in bingo')
@click.option('--randomize/--dont-randomize', default=True, is_flag=True,
              help="determine whether or not to shuffle bingo fields. True or False, True by default")
@click.option('--bgcolor', default='#FFF',
              help='Background color')
@click.option('--fontpath',
              help='Path to font of your choice')
@click.option('--color', default='#000',
              help='Font color')
@click.option('--fontsize', default=22,
              help='Font size')
@click.option('--padding', default=20,
              help='Padding of squares in your bingo')
@click.option('--dimensions', nargs=2, type=click.Tuple([int, int]), default=(1600, 900),
              help='Bingo dimensions - first value determines width, second one - height')
def cli(title, fields, freespace, size, randomize, bgcolor, fontpath, color, fontsize, padding, dimensions):
    """
    Bingo generator. \n
    FIELDS: Input bingo fields formatted as CSV string \n
    TITLE: Title of the Bingo. \n
    """

    entries = list(csv.reader(StringIO(" ".join(i for i in fields))))[0]
    Bingo.make_bingo_from_scratch(entries=entries, title=title, freespace=freespace, size=size, randomize=randomize,
                 bgcolor=bgcolor, fontcolor=color,
                 width=dimensions[0], height=dimensions[1], padding=padding,
                 fontpath=fontpath, fontsize = fontsize)


if __name__ == '__main__':
    cli()
