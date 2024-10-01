```python
...
from math import sqrt
class RunawayGame:
    def __init__(self, canvas, runner, chaser, user, catch_radius=50):
        ...
        self.user = user        # runner를 잡고 chaser에게서 도망가는것이 목표
        self.elapsed_time = 0   # 타이머
        self.score = 0          # 스코어
        self.prevPos = (0,0)    # 스코어를 계산할 때 필요한 이전 좌표

        ...

        # Initialize 'user'
        self.user.shape('turtle')
        self.user.color('purple')
        self.user.penup()

        ...

    def is_catched(self, runner, chaser):   # 오브젝트 두개를 받아서 확인할 수 있도록 변경
        p = runner.pos()
        q = chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    ...

    def step(self):
        self.score+=sqrt(abs(self.user.pos()[0]-self.prevPos[0])**2+abs(self.user.pos()[1]-self.prevPos[1])**2)/10  # 이동한 거리/10 만큼 스코어 증가
        self.prevPos = self.user.pos()                  # 이전 좌표 갱신 
        self.elapsed_time += self.ai_timer_msec/1000    # 타이머 갱신
        
        ...

        # TODO) You can do something here and follows.
        is_catched = self.is_catched(self.runner, self.user) and not self.is_catched(self.user, self.chaser)    # chaser 에게 잡히지 않고 runner를 잡으면 True
        self.drawer.clear()     # 이전 정보 지우기
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(f'Is catched? {is_catched}', font=("Arial", 12, "normal"))

        # show timer
        self.drawer.setpos(-300, 270)
        self.drawer.write(f'Time Elapsed: {self.elapsed_time:0.1f} seconds', font=("Arial", 12, "normal"))  # 타이머 표시 갱신

        # show score
        self.drawer.setpos(-300, 240)
        self.drawer.write(f'Score: {int(self.score)}', font=("Arial", 12, "normal"))    # 스코어 표시 갱신

        # Note) The following line should be the last of this function to keep the game playing
        self.canvas.ontimer(self.step, self.ai_timer_msec)

...

if __name__ == '__main__':
    ...
    user = ManualMover(screen) # 유저 거북이 추가

    game = RunawayGame(screen, runner, chaser, user) # 함께 넘겨준다.
    game.start()
    screen.mainloop()
```
*위 코드에서 변경점을 간단하게 나타내고 있습니다.*

### Add a timer (5 points): You can freely choose an up/down timer for your purpose.
타이머의 시작을 0으로 놓고 100ms마다 호출되는 step 함수를 통해서 타이머를 함께 업데이트 하였습니다.<br>
타이머의 표시는 기존의 성공 여부를 표시하는 turtle을 활용하였습니다.
### Add your Turtle (8 points): You can assign a role, runner or chaser or both.
chaser 에게서는 도망치고 runner 를 잡아야 게임을 클리어할 수 있는 user turtle 를 추가하였습니다.
### Add your concept of score (7 points): You can define the score by yourself.
prevPos 를 저장하여 이동한 거리만큼 스코어를 증가시키는 방법을 사용하였습니다.<br>
스코어의 표시는 기존의 drawer를 활용하였습니다.

#### **게임 사진**
Blue : Runner<br>
Red : Chaser<br>
Purple : User<br>
![turtle_runaway](https://github.com/user-attachments/assets/6a861bae-1dca-4c14-badb-8bc94729b8ed)