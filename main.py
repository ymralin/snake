from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# from boundary import Boundary

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

game_is_on = True

# game tick counter for future use in generating events
game_tick = 0
# duration of one game tick, describes game speed, time of movement between neighbouring positions
tick_time = 0.1
# variable to keep track of collected food
food_eaten = 0


snek = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snek.go_up, "w")
screen.onkey(snek.go_left, "a")
screen.onkey(snek.go_right, "d")
screen.onkey(snek.go_down, "s")

# key bindings for debugging purposes, uncomment when needed
# screen.onkey(snek.add_segment, "space")
# screen.onkey(food.move_food, "q")


def game_over():
    global game_is_on
    food.ht()
    screen.update()
    game_is_on = False
    score.game_over()


def check_self_collision():
    global game_is_on
    for segment in snek.segments[1:]:
        if snek.segments[0].distance(segment) < 1:
            food.ht()
            screen.update()
            game_is_on = False
            score.game_over()


def check_wall_collision():
    if snek.segments[0].xcor() > 280 or snek.segments[0].xcor() < -280 or \
            snek.segments[0].ycor() < -280 or snek.segments[0].ycor() > 240:
        game_over()


def eat_food():
    global food_eaten
    if snek.segments[0].distance(food) < 1:
        snek.add_segment()
        food.move_food()
        food_eaten += 1
        snek.sped_up = False


def speed_up():
    global tick_time
    if not snek.sped_up:
        if food_eaten > 0:
            if food_eaten % 5 == 0:
                tick_time *= 0.9
                snek.sped_up = True


def start_game():
    screen.update()
    global food_eaten
    #food_eaten = 0
    score.clear()
    score.update_score()
    global game_tick
    while game_is_on:
        snek.move()
        eat_food()
        speed_up()
        game_tick += 1
        screen.update()
        time.sleep(tick_time)
        snek.turned = False
        score.score = food_eaten
        score.update_score()
        check_wall_collision()
        check_self_collision()


def restart_game():
    global food_eaten
    global game_is_on
    if not game_is_on:
        food_eaten = 0
        score.score = 0
        score.update_score()
        for _ in range(len(snek.segments)):
            snek.segments[-1].reset()
            snek.segments.pop(-1)
        game_is_on = True
        snek.create_snake()
        food.move_food()
        food.st()
        start_game()


screen.onkey(restart_game, "Return")


def pause_game():
    global game_is_on
    game_is_on = not game_is_on
    start_game()


screen.onkey(pause_game, "p")


def qwe():
    score.reset_score()


start_game()


screen.exitonclick()
