from Clock import Clock

class Spritesheet:
    def __init__(self, img, columns, rows, frame_sizes, frame_duration):
        self.img = img
        self.columns = columns
        self.rows = rows
        self.frame_sizes = frame_sizes
        self.frame_duration = frame_duration

        self.clock = Clock()
        self.frame_index = 0

    def draw(self, canvas, pos):
        self.clock.tick()
        if self.clock.transition(self.frame_duration):
            self.next_frame()

        frame_width, frame_height = self.frame_sizes[self.frame_index]
        centre_x = self.frame_index % self.columns * frame_width + frame_width / 2
        centre_y = self.frame_index // self.columns * frame_height + frame_height / 2

        source_centre = (centre_x, centre_y)
        source_size = (frame_width, frame_height)
        dest_size = (frame_width * 2, frame_height * 2)

        canvas.draw_image(self.img, source_centre, source_size, pos.get_p(), dest_size)

    def next_frame(self):
        self.frame_index = (self.frame_index + 1) % len(self.frame_sizes)