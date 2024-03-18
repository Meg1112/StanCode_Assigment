"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Use paddle bounce ball to remove brick. When ball drop to the paddle, losing one live.
No live or no brick will end the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.ball_radius = ball_radius
        self.paddle_w = paddle_width
        self.paddle_h = paddle_height
        self.pad_off = paddle_offset
        self.bricks_r = brick_rows
        self.bricks_c = brick_cols
        self.bricks_w = brick_width
        self.bricks_h = brick_height
        self.bricks_off = brick_offset
        self.bricks_s = brick_spacing

        # Create a graphical window, with some extra space
        window_width = self.bricks_c * (self.bricks_w + self.bricks_s) - self.bricks_s
        window_height = self.bricks_off + 3 * (self.bricks_r * (self.bricks_h + self.bricks_s) - self.bricks_s)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(self.paddle_w, self.paddle_h, x=self.window.width/2-paddle_width/2,
                            y=self.window.height - self.pad_off - self.paddle_h)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window.width / 2 - self.ball_radius,
                         y=self.window.height / 2 - self.ball_radius)

        # Draw bricks
        self.color = "black"
        for i in range(self.bricks_c):  # different cols different color
            if i == 0 or i == 1:
                self.color = "red"
            elif i == 2 or i == 3:
                self.color = "orange"
            elif i == 4 or i == 5:
                self.color = "yellow"
            elif i == 6 or i == 7:
                self.color = "green"
            else:
                self.color = "blue"
            for j in range(brick_rows):
                if i == 0 and j == 0:  # first bricks at top left
                    self.bricks = GRect(brick_width, brick_height, x=j,
                                        y=brick_offset)
                    self.bricks.filled = True
                    self.bricks.fill_color = self.color
                    self.bricks.color = self.color
                    self.window.add(self.bricks)
                elif i > 0 and j == 0:  # first bricks at left side
                    self.bricks = GRect(brick_width, brick_height, x=j,
                                        y=brick_offset + i * brick_height + i * brick_spacing)
                    self.bricks.filled = True
                    self.bricks.fill_color = self.color
                    self.bricks.color = self.color
                    self.window.add(self.bricks)
                else:  # other bricks
                    self.bricks = GRect(brick_width, brick_height, x=j * brick_width + j * brick_spacing,
                                        y=brick_offset + i * brick_height + i * brick_spacing)
                    self.bricks.filled = True
                    self.bricks.fill_color = self.color
                    self.bricks.color = self.color
                    self.window.add(self.bricks)

        # Initialize our mouse listeners
        self.__dx = 0
        self.__dy = 0
        self.switch = True
        onmouseclicked(self.ball_bouncing)
        onmousemoved(self.paddle_follow)

    # Default initial velocity for the ball
    def reset_ball(self):
        if self.switch is False:
            self.__dx = 0
            self.__dy = 0

    def ball_bouncing(self, event):
        self.switch = True
        if self.ball.x == self.window.width / 2 - self.ball_radius:
            if self.ball.y == self.window.height / 2 - self.ball_radius:
                self.__dx = random.randint(1, MAX_X_SPEED)
                self.__dy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def paddle_follow(self, mouse):
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2
