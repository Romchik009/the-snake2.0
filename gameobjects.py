from random import randrange
from pygame import Entity, Vec3, color  # Импортируем необходимые модули из pygame

class Apple(Entity):  # Класс для создания яблок
    def __init__(self, MAP_SIZE, **kwargs):
        super().__init__(**kwargs)
        self.MAP_SIZE = MAP_SIZE
        self.new_position()

    def new_position(self):  # Устанавливаем новую позицию яблока
        self.position = (randrange(self.MAP_SIZE) + 0.5, randrange(self.MAP_SIZE) + 0.5, -0.5)


class Snake:  # Класс для создания змеи
    def __init__(self, MAP_SIZE):
        self.MAP_SIZE = MAP_SIZE
        self.segment_length = 1
        self.segment_positions = [Vec3(randrange(MAP_SIZE) + 0.5, randrange(MAP_SIZE) + 0.5, -0.5)]
        self.segment_entities = []
        self.create_segment(self.segment_positions[0])
        self.directions = {'a': Vec3(-1, 0, 0), 'd': Vec3(1, 0, 0), 'w': Vec3(0, 1, 0), 's': Vec3(0, -1, 0)}
        self.direction = Vec3(0, 0, 0)
        self.permissions = {'a': 1, 'd': 1, 'w': 1, 's': 1}
        self.taboo_movement = {'a': 'd', 'd': 'a', 'w': 's', 's': 'w'}
        self.speed, self.score = 12, 0
        self.frame_counter = 0

    def add_segment(self):  # Добавляем новый сегмент змеи
        self.segment_length += 1
        self.score += 1
        self.speed = max(self.speed - 1, 5)
        self.create_segment(self.segment_positions[-1])

    def create_segment(self, position):  # Создаем сегмент змеи
        entity = Entity(model='sphere', color=color.green, position=position)
        self.segment_entities.append(entity)

    def run(self):  # Обновляем позиции сегментов змеи
        self.frame_counter += 1
        if not self.frame_counter % self.speed:
            new_position = self.segment_positions[-1] + self.direction
            # Проверяем, не вышла ли змея за пределы карты
            if 0 <= new_position.x < self.MAP_SIZE and 0 <= new_position.y < self.MAP_SIZE:
                self.segment_positions.append(new_position)
                self.segment_positions = self.segment_positions[-self.segment_length:]
                for segment, segment_position in zip(self.segment_entities, self.segment_positions):
                    segment.position = segment_position

    def control(self, key):  # Управление змеей
        if key in self.directions and self.permissions[key]:
            # Запрещаем движение в противоположном направлении
            if self.direction != -self.directions[self.taboo_movement[key]]:
                self.direction = self.directions[key]
                self.permissions = dict.fromkeys(self.permissions, 1)
                self.permissions[self.taboo_movement[key]] = 0
