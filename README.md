Bingo generator
===

Overwiew
----
A Bingo generator written in python using a PIL. 

The main purpose of this module is to generate randomized bingo, just for the delight of the crowd.

#### Usage
Just simply install the package using `python -m pip install .` in folder with setup.py.

##### Script
You use CLI script directly from your shell with `bingo.py`. Format them like CSV (just use `\"` for quotes).

Sample usage:
`bingo.py example Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce,\"Jan, Maria, Rokita\",8,9,10,12,15,17,20,25,"very very very long string",56,89,235,23,56,88,123,5,3,4,4,4,4`

will generate following image:

![example](./example.png)


Use `bingo.py --help` for more info.

##### Package
You can also use bingo-generator as package. 

Sample usage:

```python
import Bingo


entries = [
    'Brzęczyszczykiewicz',
    'Grzegorz',
    'Chrząszczyżewoszyce',
    '"Jan, Maria, Rokita"',
    '8',
    '9',
    '10',
    '12',
    '15',
    '17',
    '20',
    '25',
    ''"very very very long string"'',
    '56',
    '89',
    '235',
    '23',
    '56',
    '88',
    '123',
    '5',
    '3',
    '4',
    '4',
    '4',
    '4'
    ]
    
bing = Bingo.make_bingo_from_scratch(entries=entries, title='Example')

```

Will generate bingo simillar to previous one.

Bingo values:
- entries - list of strings - Bingo entries.
- title - str  - Bingo title
- freespace - str - Bingo freespace (the central square) 
- size - int - width and height of the Bingo
- randomize - boolean - determines whether or not to determine bingo fields
- bgcolor 
- fontcolor
- width - int -1600
- height - int = 900
- padding - int - 20
- fontpath - path to your fonpath if you don't want to use default one
- fontsize - int - size of your font


### Resources
All used resources belongs to respective owners.

Font taken from https://github.com/google/fonts/blob/master/ofl/archivo/Archivo-Bold.ttf