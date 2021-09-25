from pyamaze import maze , COLOR,agent
m=maze()
m.CreateMaze(theme=COLOR.light)
a=agent(m,filled=True)
m.tracePath({a:m.path})
m.run()











