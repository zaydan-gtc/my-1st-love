import turtle
import random
import time

# =========================================================
# 🎮 CATCH THE STARS GAME
# =========================================================

# -----------------------------
# 1. CREATE THE GAME WINDOW
# -----------------------------

screen = turtle.Screen()
screen.title("⭐ Catch the Stars!")
screen.bgcolor("midnight blue")
screen.setup(width=800, height=600)
# Turn off automatic screen updates
screen.tracer(0)
# =========================================================
# 2. CREATE THE PLAYER
# =========================================================
player = turtle.Turtle()
player.shape("square")
player.color("lime")
player.shapesize(stretch_wid=1, stretch_len=4)

player.penup()
player.goto(0, -250)


# =========================================================
# 3. PLAYER MOVEMENT
# =========================================================

def move_left():
    x = player.xcor()

    # Prevent the player from leaving the screen
    if x > -330:
        player.setx(x - 30)
def move_right():
    x = player.xcor()

    # Prevent the player from leaving the screen
    if x < 330:
        player.setx(x + 30)


# Keyboard controls
screen.listen()

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Also allow A and D
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
# =========================================================
# 4. CREATE THE STAR
# =========================================================
star = turtle.Turtle()
star.shape("circle")
star.color("yellow")
star.penup()
# Put the star at a random starting position
star.goto(random.randint(-330, 330), 250)

# =========================================================
# 5. SCORE
# =========================================================

score = 0

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(-370, 260)

score_writer.write(
    "Score: 0",
    font=("Arial", 18, "bold")
)
# =========================================================
# 6. LIVES
# =========================================================
lives = 3
lives_writer = turtle.Turtle()
lives_writer.hideturtle()
lives_writer.color("white")
lives_writer.penup()
lives_writer.goto(250, 260)

lives_writer.write(
    "Lives: 3",
    font=("Arial", 18, "bold")
)


# =========================================================
# 7. GAME OVER MESSAGE
# =========================================================

message = turtle.Turtle()
message.hideturtle()
message.color("red")
message.penup()
# =========================================================
# 8. GAME VARIABLES
# =========================================================
star_speed = 5
game_running = True

# =========================================================
# 9. UPDATE SCORE
# =========================================================

def update_score():
    score_writer.clear()

    score_writer.write(
        "Score: " + str(score),
        font=("Arial", 18, "bold")
    )


# =========================================================
# 10. UPDATE LIVES
# =========================================================

def update_lives():
    lives_writer.clear()
    lives_writer.write(
        "Lives: " + str(lives),
        font=("Arial", 18, "bold")
    )
# =========================================================
# 11. CHECK IF PLAYER CAUGHT THE STAR
# =========================================================
def caught_star():
    # Check the distance between player and star
    distance = player.distance(star)

    if distance < 60:
        return True

    return False


# =========================================================
# 12. GAME LOOP
# =========================================================

while game_running:

    # Move the star downward
    star.sety(star.ycor() - star_speed)

    # -----------------------------------------
    # CHECK IF THE PLAYER CAUGHT THE STAR
    # -----------------------------------------

    if caught_star():

        score += 1

        update_score()

        # Move star back to the top
        star.goto(
            random.randint(-330, 330),
            250
        )

        # Make the game gradually faster
        if score % 5 == 0:
            star_speed += 1


    # -----------------------------------------
    # CHECK IF STAR REACHED THE BOTTOM
    # -----------------------------------------

    if star.ycor() < -280:

        lives -= 1

        update_lives()

        # Put star back at the top
        star.goto(
            random.randint(-330, 330),
            250
        )


    # -----------------------------------------
    # CHECK FOR GAME OVER
    # -----------------------------------------

    if lives <= 0:

        game_running = False

        message.goto(0, 0)

        message.write(
            "GAME OVER!",
            align="center",
            font=("Arial", 36, "bold")
        )

        message.goto(0, -50)

        message.color("white")

        message.write(
            "Final Score: " + str(score),
            align="center",
            font=("Arial", 22, "bold")
        )


    # Update the screen
    screen.update()

    # Small delay
    time.sleep(0.02)


# =========================================================
# 13. KEEP THE WINDOW OPEN
# =========================================================

turtle.done()