"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Use paddle bounce ball to remove brick. When ball drop to the paddle, losing one live.
No live or no brick will end the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extentions import BreakoutGraphics
from campy.graphics.gimage import GImage

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    global NUM_LIVES
    graphics = BreakoutGraphics()
    img_live = GImage("heart (2).png")

    # Draw how many lives
    for i in range(NUM_LIVES):
        img_live = GImage("heart (2).png")
        graphics.window.add(img_live, x=graphics.window.width - (i + 1) * img_live.width, y=5)
    # Add the animation loop here!
    brick_number = graphics.bricks_r * graphics.bricks_c
    while True:
        if graphics.switch or NUM_LIVES != 0 or brick_number > 0:
            while True:
                # Check if no live, end the game
                if NUM_LIVES == 0:
                    graphics.game_end()
                    graphics.switch = False
                    break
                if brick_number <= 0:
                    graphics.game_win()
                    graphics.switch = False
                    break

                vx = graphics.get_dx()
                vy = graphics.get_dy()
                graphics.ball.move(vx, vy)
                if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                    graphics.set_dx()
                if graphics.ball.y <= graphics.bricks_off:
                    if vy < 0:
                        graphics.set_dy()

                # Level up, speed up
                if graphics.score_num >= 30:
                    graphics.level_up()

                # check ball success bounce on the paddle or not
                if graphics.ball.y >= graphics.window.height:
                    pause(300)
                    graphics.miss_live()
                    pause(500)
                    graphics.remove_miss()
                    graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
                    graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
                    NUM_LIVES -= 1
                    # Remove one lives
                    lives = graphics.window.get_object_at(x=graphics.window.width -
                                                            (NUM_LIVES+1-1)*img_live.width, y=5)
                    graphics.window.remove(lives)
                    graphics.switch = False
                    graphics.reset_ball()
                    break

                # if ball hit to the brick, then remove the brick and change direction.
                # ball left top.
                if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not None:
                    brick = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                    # not remove paddle
                    if brick.x != graphics.paddle.x or brick.y != graphics.paddle.y:
                        if brick.x != graphics.line.x or brick.y != graphics.line.y:
                            graphics.window.remove(brick)
                            graphics.count_score()
                            brick_number -= 1
                            graphics.set_dy()
                    elif vy > 0:
                        # ball at paddle then bouncing
                        graphics.set_dy()
                # ball right top
                elif graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y) is not None:
                    brick = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                    # not remove paddle
                    if brick.x != graphics.paddle.x or brick.y != graphics.paddle.y:
                        if brick.x != graphics.line.x or brick.y != graphics.line.y:
                            graphics.window.remove(brick)
                            graphics.count_score()
                            brick_number -= 1
                            graphics.set_dy()
                    # ball at paddle then bouncing
                    elif vy > 0:
                        graphics.set_dy()
                # ball left bottom
                elif graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height) is not None:
                    brick = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                    # not remove paddle
                    if brick.x != graphics.paddle.x or brick.y != graphics.paddle.y:
                        if brick.x != graphics.line.x or brick.y != graphics.line.y:
                            graphics.window.remove(brick)
                            graphics.count_score()
                            brick_number -= 1
                            graphics.set_dy()
                    # ball at paddle then bouncing
                    elif vy > 0:
                        graphics.set_dy()
                # ball right bottom
                elif graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                   graphics.ball.y + graphics.ball.height) is not None:
                    brick = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                          graphics.ball.y + graphics.ball.height)
                    # not remove paddle
                    if brick.x != graphics.paddle.x or brick.y != graphics.paddle.y:
                        if brick.x != graphics.line.x or brick.y != graphics.line.y:
                            graphics.window.remove(brick)
                            graphics.count_score()
                            brick_number -= 1
                            graphics.set_dy()
                    # ball at paddle then bouncing
                    elif vy > 0:
                        graphics.set_dy()
                pause(FRAME_RATE)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
