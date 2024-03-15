#import "tem.typ":*
#import "template.typ":*
#let i = {h(2em)}
#set page(numbering: "1", paper: "a4")
#init("Mid term", "Nguyễn Khánh Toàn", student_number: "22127418")
//#init("Chapter 1", "Nguyễn Khánh Hoàng", student_number: "22127418")


// #show: project.with(
//     title: "Homework ",
//     authors:("Nguyễn Khánh Toàn","s"),
//     student_number: ("22127418"),
//     class: ("22CLC01"),
// )

#answer(
  [*Resources*
  - Algorithm: 
    + ChatGPT
    + My available project : #link("https://github.com/KTNguyen04/SearchyVisualization.git")
  - Visualization:
    + My available project : #link("https://github.com/KTNguyen04/SearchyVisualization.git")
  - Tools:
    + IDE: VisualStudioCode with environment
    + Language: Python with Pygame
  - Source for this project:
  

  ],
  
)

#answer(


 
    [*Q1*
//     Some notations: 
// -  #rect(fill:rgb("D5E8D4"),stroke:rgb("82B366"))[Picked nodes]
// -  #rect(fill:rgb("ffffff"),stroke:rgb("000000"))[Expanded nodes]
// -  #rect(fill:rgb("DAE8FC"),stroke:rgb("6C8EBF"))[Heuristic value]
// -  #rect(fill:rgb("FFF2CC"),stroke:rgb("D6B656"))[Cost]
// -  #rect(fill:rgb("F8CECC"),stroke:rgb("B85450"))[F( node )]
    
    ],

    [ #figure(
       image("maze.png",width: 70%),
       caption:"Maze")
       #figure(
       image("matrix.png",width: 50%),
       caption:"Matrix input in file cost.txt")],
    [],[],[]
 
)

#answer(
  [*Q2. DFS ,BFS, AStar*],
  [
  #figure(
       image("dfs.png",width: 70%),
       caption:"DFS")
  ],
  [

        #figure(
       image("bfs.png",width: 70%),
       caption:"BFS")],
  
  [    #figure(
       image("astar.png",width: 70%),
       caption:"AStar")],
       [*Compare*
       #figure(
       image("compare.png"),
       caption:"Executed time ")


       ]
)

#answer(
  [*Q3. Hill-climbing search*],
  [*My implement for Hill-climbing search*
  #figure(
       image("hccode.png",width: 70%),
       caption:"Hill-climbing search implementation")

        #figure(
       image("shccode.png",width: 70%),
       caption:"Stochastic Hill-climbing search implementation")

  ],
  [*Hill-climbing search*
  #figure(
       image("hcv.png",width: 70%),
       caption:"Pure Hill-climbing search which get stuck in my maze")
  
    #figure(
        image("shcv.png",width: 70%),
        caption:"Stochastic Hill-climbing search which take more than 5min in my maze")


  ],
  [*Compare*
   #figure(
        image("compare2.png"),
        caption:"Searched time")
  ]

)

