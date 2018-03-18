Bingo generator
===

Overwiew
----
A Bingo generator written in python using a PIL. 

The main purpose of this module is to generate randomized bingo, just for the delight of the crowd.

#### Usage
Just simply install the package using `python -m pip install .` in folder with setup.py.

##### Script
Use CLI script directly from your shell with `bingo.py`. Format input fields like CSV (just use `\"` for quotes).

Sample usage:

`bingo.py example Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce,\"Jan, Maria, Rokita\",8,9,10,12,15,17,20,25,here is \"very very very very very very very very very very long string\",56,89,235, bingo input, 1, 2, 3, 4, 5, 3, 2, 1`

Will generate similar image in your current directory:

![image.png](https://res.cloudinary.com/hpiynhbhq/image/upload/v1521391685/bwohlcjewuuimacuw6q0.png)

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
- width - int 
- height - int
- padding - int
- fontpath - path to your fonpath if you don't want to use default one
- fontsize - int - size of your font

After generating Bingo you can use any graphics software to check the appropriate boxes (or just print it and check boxes manually). 

Have fun!

### Resources
All used resources belongs to respective owners.

Font taken from https://github.com/google/fonts/blob/master/ofl/archivo/Archivo-Bold.ttf

### License
MIT

Roadmap
---------
- Make proper tests 
- Add image support as bingo fields
- Write stand-alone `.exe` client for windows users
 
Contributing
---------
Just make pull request. If you have any questions feel free to contact me via email - it is linked to my github account.
