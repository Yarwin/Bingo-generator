from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import shuffle


class Bingo:
    def __init__(self, entries, title="test", freespace="", size=5, randomize=True,
                 bgcolor='#FFF', fontcolor= '#000',
                 width=1600, height=900, padding=20,
                 fontpath=None, fontsize=22):
        self.title = title
        self.font = ImageFont.load_default() if not fontpath else ImageFont.truetype(fontpath, fontsize)
        self.color = fontcolor
        self.img = Image.new("RGBA", (width, height), bgcolor)
        self.draw = ImageDraw.Draw(self.img)
        self.size = size
        self.p = padding
        self.width, self.height = width, height
        self.line_width = (self.width // (self.size - 1) ) - (self.size + 1)  * self.p
        self.line_height = (self.height // (self.size - 1)) - self.size * self.p

        self.entries = entries
        if randomize:
            shuffle(entries)

        if freespace:
            freespace_index = (self.size // 2) * self.size + self.size // 2 + 1
            self.entries.insert(freespace_index - 1, freespace)

    def draw_lines(self):
        # draw top line bellow title
        top_height = self.line_height + self.p
        bottom_height = (self.line_height + self.p) * (self.size + 1)
        right_width = (self.line_width + self.p) * (self.size)
        self.draw.line(xy=[(self.p, top_height), (right_width, top_height)],
                       fill=(0,0,0, 255), width=4)

        # draw horizontal lines
        for i in range(1, self.size+1):
            line_height = ((i + 1) * (self.line_height+self.p))
            self.draw.line(xy=[(self.p, line_height), (right_width, line_height)],
                           fill=(0, 0, 0, 255), width=4)

        # draw vertical lines
        for i in range(0, self.size+1):
            line_width = (i * (self.line_width+self.p)) if i else self.p
            self.draw.line(xy=[(line_width, top_height), (line_width, bottom_height)],
                           fill=(0, 0, 0, 255), width=4)


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
                # center text
                current_x += (self.line_width - line_width) // 2

            self.draw.text((current_x, y),
                           line, self.color, font=self.font)

            y += self.font.getsize(line)[1]
            current_x = x

    def generate_bingo(self):
        x, y = self.p, self.line_height + self.p
        for i, entry in enumerate(self.entries, 1):
            self.draw_entry(entry, x, y)

            x += self.line_width + self.p

            if not i % self.size:
                y += self.line_height + self.p
                x = self.p

            if i == (self.size * 5):
                break

    def save_bingo(self):
        self.img.save('{0}.png'.format(self.title))
