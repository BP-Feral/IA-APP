### Installation
run `pip install -r requirements.txt`
used packages: `pygame-ce` for graphics and `colorama` for console colors.

### Run the app
Use python debugger to run `main.py`

### How to use
`Show Time` will display the recorded time for each problem. (empty at first)
- To record the time, choose any problem, input the board size and press `Start`.
If a solution is found, the time will be registered and updated in the graph.

The graph has dynamic updates, any board size or time will automatically scale the graph for new values
The chess board also scales dynamically based off the input size. Locked between 1 and 25.

Currently the application only runs one generation per test.

### Objectives
- [x] Backtracking (queens)
- [x] Mountainer (queens)
- [x] Tempering (queens)
- [x] Genetic (queens)
>
- [ ] N Queens (plot)
- [ ] Traveling salesman (bkt)
- [ ] Traveling salesman (neighbour)
>
- [ ] run multiple generations per test and return the average time. [not implemented]
- [ ] display all generations time in graph