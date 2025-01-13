import pygame
import gameobject

class Game(pygame.Surface):
    def __init__(self):
        super().__init__((800, 600))  # Указываем размер окна
        self.init_window()
        self.window_color = (0, 0, 0)  # Черный цвет фона
        self.window_borderless = False
        # self.window_fullscreen_size = (1920, 1080)
        # self.window_fullscreen = True
        self.ambient_light = {'type': 'ambient', 'color': (0.5, 0.5, 0.5, 1)}
        self.directional_light = {'type': 'directional', 'color': (0.5, 0.5, 0.5, 1), 'direction': (1, 1, 1)}
        self.MAP_SIZE = 20
        self.new_game()
        self.camera = {'position': (self.MAP_SIZE // 2, -20.5, -20), 'rotation_x': -57}

    def init_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")

    def create_map(self, MAP_SIZE):
        self.map_model = {'model': 'quad', 'scale': MAP_SIZE, 'position': (MAP_SIZE // 2, MAP_SIZE // 2, 0), 'color': (0.1, 0.1, 0.1)}
        self.grib_model = {'model': 'Grib', 'scale': MAP_SIZE, 'position': (MAP_SIZE // 2, MAP_SIZE // 2, -0.01), 'color': (0, 0, 0)}

    def new_game(self):
        self.scene = []  # Очистка сцены
        self.create_map(self.MAP_SIZE)
        self.apple = {'position': (5, 5), 'model': 'sphere', 'color': (1, 0, 0)}  # Красное яблоко
        self.snake = {'segment_positions': [(10, 10)], 'direction': (0, 0), 'score': 0}

    def input(self, key, is_raw=False):
        if key == pygame.K_2:
            self.camera['rotation_x'] = 0
            self.camera['position'] = (self.MAP_SIZE // 2, self.MAP_SIZE // 2, -50)
        elif key == pygame.K_3:
            self.camera['position'] = (self.MAP_SIZE // 2, -20.5, -20)
            self.camera['rotation_x'] = -57

    def check_apple_eaten(self):
        if self.snake['segment_positions'][-1] == self.apple['position']:
            self.snake['segment_positions'].append(self.snake['segment_positions'][-1])  # Добавляем новый сегмент
            self.apple['position'] = (self.MAP_SIZE // 2, self.MAP_SIZE // 2)  # Новое положение яблока
            self.snake['score'] += 1

    def check_game_over(self):
        snake = self.snake['segment_positions']
        head = snake[-1]
        if not (0 <= head[0] < self.MAP_SIZE and 0 <= head[1] < self.MAP_SIZE) or len(snake) != len(set(snake)):
            print("GAME OVER")
            self.snake['direction'] = (0, 0)
            self.new_game()

    def update(self):
        self.screen.fill(self.window_color)
        self.check_apple_eaten()
        self.check_game_over()
        self.snake_run()
        pygame.display.flip()

    def snake_run(self):
        # Логика движения змейки
        pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.input(event.key)
            self.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
