"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Use paddle bounce ball to remove brick. When ball drop to the paddle, losing one live.
No live or no brick will end the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks`
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
        self.window = GWindow(width=window_width, height=window_height, title="Break_Out Game")

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
        # Draw a wall
        self.line = GLine(0,self.bricks_off-5, self.window.width, self.bricks_off-5)
        self.window.add(self.line)

        # Draw bricks
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

        # Draw Score
        self.score_num = 0
        self.label_score = GLabel("Score: " + str(self.score_num))
        self.label_score.font = "Verdana-30-bold-italic"
        self.window.add(self.label_score, x=0, y=self.label_score.height+5)

        self.label_miss = GLabel("Oops")
        self.label_miss.color = "red"
        self.label_miss.font = "-50"
        self.img_dead = GImage("dead.png")

        self.label_game_end = GLabel("GAME OVER")
        self.label_game_end.color = "red"
        self.label_game_end.font = "-60"

        self.label_win = GLabel("YOU WIN !")
        self.label_win.color = "green"
        self.label_win.font = "-60"
        self.img_win = GImage("team.png")

        self.level_s = True
        self.level_num = 0

    def miss_live(self):
        self.window.add(self.label_miss, x=(self.window.width-self.label_miss.width) / 2, y=self.window.height/2+100)
        self.window.add(self.img_dead, x=(self.window.width-self.img_dead.width) / 2,
                        y=self.window.height/2+self.img_dead.height+50)
        self.level_num = 0

    def remove_miss(self):
        label_miss = self.window.get_object_at(x=self.window.width / 2, y=self.window.height / 2 + 100)
        img_dead = self.window.get_object_at(x=(self.window.width-self.img_dead.width) / 2,
                                             y=self.window.height/2+self.img_dead.height+50)
        self.window.remove(label_miss)
        self.window.remove(img_dead)

    def game_win(self):
        self.window.add(self.label_win, x=(self.window.width-self.label_win.width) / 2, y=self.window.height/2+100)
        self.window.add(self.img_win, x=(self.window.width-self.img_win.width) / 2,
                        y=self.window.height/2-self.label_win.height*2)

    def game_end(self):
        self.window.add(self.label_game_end, x=(self.window.width-self.label_game_end.width) / 2,
                        y=self.window.height/2 + 100)

    def count_score(self):
        self.score_num += 1
        self.label_score.text = "Score: " + str(self.score_num)

    # Default initial velocity for the ball
    def reset_ball(self):
        if self.switch is False:
            self.__dx = 0
            self.__dy = 0

    def ball_bouncing(self, event):
        self.switch = True
        if self.ball.x == self.window.width / 2 - self.ball_radius:
            if self.ball.y == self.window.height / 2 - self.ball_radius:
                self.__dx = random.randint(1, 3)
                self.__dy = 3  # begin speed minimum is 3 ,next level plus 2
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def level_up(self):
        if self.level_num == 0:
            self.level_num += 1
            if self.__dy > 0:
                self.__dy += 2
                self.__dx += 1
                print(self.__dx, self.__dy)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def paddle_follow(self, mouse):
        if mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2
