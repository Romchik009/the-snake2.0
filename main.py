import pygame
import gameobject 


class Game(pygame.Surface):
    def __init__(self):
        super().__init__()
        self.init_window() = color.black
        self.window.borderless = False
        # window.fullscreen_size = 1920, 1080
        # window.fullscreen = True
        type='ambient', color=(0.5, 0.5, 0.5, 1)
        type='directional', color=(0.5, 0.5, 0.5, 1), direction=(1, 1, 1)
        self.MAP_SIZE = 20
        self.new_game()
        self.camera.position = (self.MAP_SIZE // 2, -20.5, -20)
        self.camera.rotation_x = -57

    def create_map(self, MAP_SIZE):
       model='quad', scale=MAP_SIZE, position=(MAP_SIZE // 2, MAP_SIZE // 2, 0), color=color.dark_gray
       model= Grid(MAP_SIZE, MAP_SIZE), scale=MAP_SIZE,
       position=(MAP_SIZE // 2, MAP_SIZE // 2, -0.01), color=color.black

    def new_game(self):
        self.scene.clear()
        self.create_map(self.MAP_SIZE)
        self.apple = apple(self.MAP_SIZE, model='sphere', color=color.red)
        self.snake = snake(self.MAP_SIZE)

    def input(self, key, is_raw=False):
        super().input(key)
        self.snake.control(key)
        if key == '2':
            self.camera.rotation_x = 0
            self.camera.position = (self.MAP_SIZE // 2, self.MAP_SIZE // 2, -50)
        elif key == '3':
            self.camera.position = (self.MAP_SIZE // 2, -20.5, -20)
            self.camera.rotation_x = -57


    def check_apple_eaten(self):
        if self.snake.segment_positions[-1] == self.apple.position:
            self.snake.add_segment()
            self.apple.new_position()

    def check_game_over(self):
        snake = self.snake.segment_positions
        if 0 < snake[-1][0] < self.MAP_SIZE and 0 < snake[-1][1] < self.MAP_SIZE and len(snake) == len(set(snake)):
                return
        # print_on_screen('GAME OVER', position=(-0.7, 0.1), scale=10, duration=1)
        self.snake.direction = (0, 0, 0)
        self.snake.permissions = dict.fromkeys(self.snake.permissions, 0)
        self.new_game, delay=1

    def update(self):
        self
        print_on_screen(f'Score: {self.snake.score}', position=(-0.85, 0.45), scale=3, duration=1 / 20)
        self.check_apple_eaten()
        self.check_game_over()
        self.snake.run()


if __name__ == '__main__':
    game = Game()
    update = game.update

game.run()
