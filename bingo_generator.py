from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import shuffle


class Bingo:
    def __init__(self, entries, title="test", freespace="", size=5, randomize=True,
                 bgcolor='#FFF', fontcolor= '#000',
                 width=1600, height=900, padding=20,
                 fontpath=None, fontsize = 13):
        self.title = title
        self.font = ImageFont.load_default() if not fontpath else ImageFont.truetype(fontpath, fontsize)
        self.img = Image.new("RGBA", (width, height), bgcolor)
        self.draw = ImageDraw.Draw(self.img)
        self.entries = entries

        self.p = padding
        self.size = size
        self.color = fontcolor
        marign_bottom = int(height * 0.05)
        self.width, self.height = width, height - marign_bottom


        self.line_width = (self.width // (self.size - 1) ) - (self.size + 1)  * self.p
        self.line_height = (self.height // (self.size -1)) - self.size * self.p

        if randomize:
            shuffle(entries)

        if freespace:
            freespace_index = (self.size // 2) * self.size + self.size // 2 + 1
            self.entries.insert(freespace_index - 1, freespace)

    def draw_title(self):
        title_font = self.font.font_variant(size=self.font.size*2)

        height = (self.line_height - title_font.getsize(self.title)[1]) // 2
        self.draw.text(((self.width - title_font.getsize(self.title)[0]) // 2,
                        height),
                       self.title, self.color, font=title_font)

    def split_entry(self, entry):
        entry = entry.split(' ')
        output = entry[0]
        
        for i in entry[1:]:
            last_line_width = self.font.getsize(output.split('\n')[-1] + i)[0]
            if last_line_width > (self.line_width + self.p):
                output += '\n' + i
            else:
                output += ' ' + i
        return output

    def split_entries(self):
        for i, entry in enumerate(self.entries):
            if self.font.getsize(entry)[0] > self.line_width:
                self.entries[i] = self.split_entry(entry)

    def draw_entry(self, entry, x, y):
        current_x = x
        for line in entry.split('\n'):
            line_width = self.font.getsize(line)[0]
            if line_width < self.line_width:
                current_x += (self.line_width - line_width) // 2
            self.draw.text((current_x, y),
                           line, self.color, font=self.font)

            y += self.font.getsize(line)[1]
            current_x = x

    def generate_bingo(self):
        x, y = self.p, self.line_height
        for i, entry in enumerate(self.entries, 1):
            self.draw_entry(entry, x, y)

            x += self.line_width + self.p

            if not i % self.size:

                y += self.line_height + self.p
                x = self.p

            if i > ((self.size * 5)):
                break

    def save_bingo(self):
        self.img.save('{0}.png'.format(self.title))


if __name__ == '__main__':
    #example usage
    fields = [str(i) for i in range(30)]
    bing = Bingo(fields, freespace='Example bingo \n (freespace)',
                 title='Example bingo!', fontsize=22, height=1200, fontpath='/usr/share/fonts/TTF/LibreFranklin-Bold.ttf')
    bing.split_entries()
    bing.draw_title()
    bing.generate_bingo()
    bing.save_bingo()
