import pyglet as pg
from pyglet import shapes


N=20
WINDOW_SIZE=600
grid = [ [0 for _ in range(N)] for _ in range(N) ]
mask = [ [0 for _ in range(N)] for _ in range(N) ]
def calculate_mask():
    for i in range(N):
        for j in range(N):
            score = 0
            score += grid[(i-1)%N][(j-1)%N]
            score += grid[(i-1)%N][j]
            score += grid[(i-1)%N][(j+1)%N]
            score += grid[i][(j+1)%N]
            score += grid[i][(j-1)%N]
            score += grid[(i+1)%N][(j-1)%N]
            score += grid[(i+1)%N][j]
            score += grid[(i+1)%N][(j+1)%N]
            mask[i][j]=score
def apply_mask():
    for i in range(N):
        for j in range(N):
            if grid[i][j]==0:
                if mask[i][j]==3: grid[i][j]=1
            elif grid[i][j]==1:
                if mask[i][j]<2 or mask[i][j]>3: grid[i][j]=0
            mask[i][j]=0

window = pg.window.Window(600,600)
batch = pg.graphics.Batch()

s=WINDOW_SIZE//N
squares = [[shapes.Rectangle(x=i*s,y=j*s,width=s,height=s,color=(0,0,0),batch=batch) for i in range(N)] for j in range(N)]

# Initial Condition
grid[5][6]=1
grid[6][6]=1
grid[6][7]=1
grid[6][8]=1
grid[4][7]=1
def color_grid():
    for i in range(N):
        for j in range(N):
            if grid[i][j]==1: squares[i][j].color=(100,0,0)
            else: squares[i][j].color=(0,0,0)

def step(dt):
    calculate_mask()
    apply_mask()
    color_grid()


@window.event
def on_draw():
    window.clear()
    batch.draw()

color_grid()
pg.clock.schedule_interval(step,0.1)
pg.app.run()
