from pyamaze import maze,agent,COLOR,textLabel
import constants

def dijkstra(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]
            



if __name__=='__main__':
    myMaze=maze(6,6)
    myMaze.CreateMaze(loadMaze='pyamaze\Dijkstra Algorithm\dijkMaze.csv')

    h0=agent(myMaze,1,1,constants.cost1,color=COLOR.blue)
    h1=agent(myMaze,1,2,constants.cost2,color=COLOR.red)
    h2=agent(myMaze,1,3,constants.cost3,color=COLOR.green)
    h3=agent(myMaze,1,4,constants.cost4,color=COLOR.red)
    h4=agent(myMaze,1,5,constants.cost5,color=COLOR.red)
    h5=agent(myMaze,1,6,constants.cost6,color=COLOR.red)

    h10=agent(myMaze,2,1,constants.cost10,color=COLOR.red)
    h11=agent(myMaze,2,2,constants.cost11,color=COLOR.red)
    h12=agent(myMaze,2,3,constants.cost12,color=COLOR.green)
    h13=agent(myMaze,2,4,constants.cost13,color=COLOR.red)
    h14=agent(myMaze,2,5,constants.cost14,color=COLOR.red)
    h15=agent(myMaze,2,6,constants.cost15,color=COLOR.red)

    h20=agent(myMaze,3,1,constants.cost20,color=COLOR.red)
    h21=agent(myMaze,3,2,constants.cost21,color=COLOR.red)
    h22=agent(myMaze,3,3,constants.cost22,color=COLOR.green)
    h23=agent(myMaze,3,4,constants.cost23,color=COLOR.red)
    h24=agent(myMaze,3,5,constants.cost24,color=COLOR.red)
    h25=agent(myMaze,3,6,constants.cost25,color=COLOR.red)

    h29=agent(myMaze,4,1,constants.cost29,color=COLOR.red)
    h30=agent(myMaze,4,2,constants.cost30,color=COLOR.red)
    h31=agent(myMaze,4,3,constants.cost31,color=COLOR.green)
    h32=agent(myMaze,4,4,constants.cost32,color=COLOR.red)
    h33=agent(myMaze,4,5,constants.cost33,color=COLOR.red)
    h34=agent(myMaze,4,6,constants.cost34,color=COLOR.red)

    h35=agent(myMaze,5,1,constants.cost35,color=COLOR.red)
    h36=agent(myMaze,5,2,constants.cost36,color=COLOR.red)
    h37=agent(myMaze,5,3,constants.cost37,color=COLOR.green)
    h38=agent(myMaze,5,4,constants.cost38,color=COLOR.red)
    h39=agent(myMaze,5,5,constants.cost39,color=COLOR.red)
    h40=agent(myMaze,5,6,constants.cost40,color=COLOR.red)

    h41=agent(myMaze,6,1,constants.cost41,color=COLOR.red)
    h42=agent(myMaze,6,2,constants.cost42,color=COLOR.red)
    h43=agent(myMaze,6,3,constants.cost43,color=COLOR.green)
    h44=agent(myMaze,6,4,constants.cost44,color=COLOR.red)
    h45=agent(myMaze,6,5,constants.cost45,color=COLOR.red)
    h46=agent(myMaze,6,6,constants.cost46,color=COLOR.red)

    h0.cost=constants.cost1
    h1.cost=constants.cost2
    h2.cost=constants.cost3
    h3.cost=constants.cost4
    h4.cost=constants.cost5
    h5.cost=constants.cost6

    h10.cost=constants.cost10
    h11.cost=constants.cost11
    h12.cost=constants.cost12
    h13.cost=constants.cost13
    h14.cost=constants.cost14
    h15.cost=constants.cost15

    h20.cost=constants.cost20
    h21.cost=constants.cost21
    h22.cost=constants.cost22
    h23.cost=constants.cost23
    h24.cost=constants.cost24
    h25.cost=constants.cost25

    h29.cost=constants.cost29
    h30.cost=constants.cost30
    h31.cost=constants.cost31
    h32.cost=constants.cost32
    h33.cost=constants.cost33
    h34.cost=constants.cost34
    h35.cost=constants.cost35
    h36.cost=constants.cost36
    h37.cost=constants.cost37
    h38.cost=constants.cost38
    h39.cost=constants.cost39
    h40.cost=constants.cost40
    h41.cost=constants.cost41
    h42.cost=constants.cost42
    h43.cost=constants.cost43
    h44.cost=constants.cost44
    h45.cost=constants.cost45
    h46.cost=constants.cost46
    path,c=dijkstra(myMaze
                    ,h1,h2,h3,h4,h5

, h10
, h11
, h12
, h13
, h14
, h15

, h20
, h21
, h22
, h23
, h24
, h25

, h29
, h30
, h31
, h32
, h33
, h34
, h35
, h36
, h37
, h38
, h39
, h40 
, h41
, h42
, h43
, h44
, h45
, h46,
start=(6,1))

    
    textLabel(myMaze,'Total Cost',c)

    a=agent(myMaze,6,1,color=COLOR.blue,filled=True,footprints=True)
    myMaze.tracePath({a:path})


    myMaze.run()