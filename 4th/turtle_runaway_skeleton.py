# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import tkinter as tk
import turtle, random
from math import sqrt

class RunawayGame:
    def __init__(self, canvas, runner, chaser, user, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.user = user
        self.catch_radius2 = catch_radius**2
        self.elapsed_time = 0
        self.score = 0
        self.prevPos = (0,0)

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Initialize 'user'
        self.user.shape('turtle')
        self.user.color('purple')
        self.user.penup()

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catched(self, runner, chaser):
        p = runner.pos()
        q = chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        # TODO) You can do something here and follows.
        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.score+=sqrt(abs(self.user.pos()[0]-self.prevPos[0])**2+abs(self.user.pos()[1]-self.prevPos[1])**2)/10
        self.prevPos = self.user.pos()
        self.elapsed_time += self.ai_timer_msec/1000
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        # TODO) You can do something here and follows.
        is_catched = self.is_catched(self.runner, self.user) and not self.is_catched(self.user, self.chaser)
        self.drawer.clear()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(f'Is catched? {is_catched}', font=("Arial", 12, "normal"))

        # show timer
        self.drawer.setpos(-300, 270)
        self.drawer.write(f'Time Elapsed: {self.elapsed_time:0.1f} seconds', font=("Arial", 12, "normal"))

        # show score
        self.drawer.setpos(-300, 240)
        self.drawer.write(f'Score: {int(self.score)}', font=("Arial", 12, "normal"))

        # Note) The following line should be the last of this function to keep the game playing
        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)

if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    root.title('Turtle Runaway')

    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # TODO) Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = RandomMover(screen)
    user = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser, user)
    game.start()
    screen.mainloop()
