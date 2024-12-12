from random import randrange

class Snake:
    def __init__(self, MAP_SIZE):
        self.MAP_SIZE = MAP_SIZE
        self.segment_length = 1
        self.position_length = self.segment_length + 1
        self.segment_positions = [(randrange(MAP_SIZE) + 0.5, randrange(MAP_SIZE) + 0.5, -0.5)]
        self.segment_entities = []
        self.create_segment(self.segment_positions[0])
        self.directions = {'a': (-1, 0, 0), 'd': (1, 0, 0), 'w': (0, 1, 0), 's': (0, -1, 0)}
        self.direction = (0, 0, 0)
        self.permissions = {'a': 1, 'd': 1, 'w': 1, 's': 1}
        self.taboo_movement = {'a': 'd', 'd': 'a', 'w': 's', 's': 'w'}
        self.speed, self.score = 12, 0
        self.frame_counter = 0

    def add_segment(self):
        self.segment_length += 1
        self.position_length += 1
        self.score += 1
        self.speed = max(self.speed - 1, 5)
        self.create_segment(self.segment_positions[0])

    def create_segment(self, position):
        entity = position=position
        model='sphere', color=color.green, position=position.add_script(
            speed=12, target=entity, offset=(0, 0, 0))
        self.segment_entities.insert(0, entity)

    def run(self):
        self.frame_counter += 1
        if not self.frame_counter % self.speed:
            self.segment_positions.append(self.segment_positions[-1] + self.direction)
            self.segment_positions = self.segment_positions[-self.segment_length:]
            for segment, segment_position in zip(self.segment_entities, self.segment_positions):
                segment.position = segment_position

    def control(self, key):
        for pressed_key in 'wasd':
            if pressed_key == key and self.permissions[pressed_key]:
                self.direction = self.directions[pressed_key]
                self.permissions = dict.fromkeys(self.permissions, 1)
                self.permissions[self.taboo_movement[pressed_key]] = 0
                break