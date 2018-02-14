#!/usr/bin/env python

import click
from bingo_generator import Bingo


@click.command()
@click.argument('title', nargs=1)
@click.argument('fields', nargs=-1)
@click.option('--freespace', default='',
              help='Freespace field for your bingo')
@click.option('--size', default=5,
              help='Number of columns and rows in bingo')
@click.option('--randomize/--dont-randomize', default=True, is_flag=True,
              help="determine whether or not to shuffle bingo fields. True or False, True by default")
@click.option('--bgcolor', default='#FFF',
              help='Background color')
@click.option('--fontpath', default='./Arvo-Bold.ttf',
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
    FIELDS: Input bingo fields splitted by '##' sequence. \n
    TITLE: Title of the Bingo. \n
    """
    fields = "".join([str(i) for i in fields]).split('##')
    bing = Bingo(fields, title=title, freespace=freespace, size=size, randomize=randomize,
                 bgcolor=bgcolor, fontcolor=color,
                 width=dimensions[0], height=dimensions[1], padding=padding,
                 fontpath=fontpath, fontsize = fontsize
                 )
    bing.split_entries()
    bing.draw_title()
    bing.generate_bingo()
    bing.draw_lines()
    bing.save_bingo()


if __name__ == '__main__':
    cli()
