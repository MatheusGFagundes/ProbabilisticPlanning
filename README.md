# Probabilistic Planning - Value iteration
this repository contains a value iteration algorithm along with a parser for a custom  file txt


## Parser

the parser extracts all the states with their available actions and their respective costs

To parser one of those `.net` files, you need to import the `Parser`  from `parser_mdp` just like the example below
```
from parser_mdp import Parser
    f = open("RandomGoalState/navigation_10.net")
    file_txt = f.read()
    parser = Parser(file_txt)
    states = parser.get_states()
```


## Value iteration

Value iteration is a method of computing an optimal MDP policy.

The input is the parsed states acquired from the parsing process.

To execute the algorithm you need to import mdp from parser_mdp and then pass the states in the construct and call the `value_iteration()`
just like the example below

```
 Mdp(states).value_iteration()

```

Other parameters

`Epson:` this parameter is the tolerated error among the iterations and also the stopping criteria. Default value: 0.01

the output is the final policy, the time that the algorithm took to converge, and the number of iterations.


```
it took 0.09574151039123535 seconds---
policy pi 69
     State         action            value  
------------------------------------------
robot-at-x2y1   move-north   19.999999999738527
robot-at-x3y1   move-north   21.999999999040412
robot-at-x4y1   move-west   23.999999996771606
robot-at-x5y1   move-north   25.999999985993007
robot-at-x6y1   move-north   27.999999958301686
robot-at-x7y1   move-north   29.99999986457201
robot-at-x8y1   move-north   31.999999633352168
robot-at-x9y1   move-north   33.999998911317874
robot-at-x10y1   move-north   35.99999714674641
robot-at-x11y1   move-north   37.99999303026992
robot-at-x13y1   move-north   41.99995918936702
robot-at-x14y1   move-north   43.99990426316353
robot-at-x15y1   move-north   45.99977688299991
robot-at-x16y1   move-north   47.99948118842312
robot-at-x17y1   move-north   49.99888866067738
robot-at-x18y1   move-north   51.99720147147073
robot-at-x19y1   move-north   53.9942576244424
robot-at-x20y1   move-north   55.98521293150924
robot-at-x1y2   move-north   15.999999999995406
robot-at-x2y2   move-north   17.999999999962974
robot-at-x3y2   move-north   19.999999999849745
robot-at-x5y2   move-north   23.99999999742732
robot-at-x6y2   move-north   25.999999991709668
robot-at-x7y2   move-north   27.999999971773057
robot-at-x8y2   move-west   29.99999991817247
robot-at-x9y2   move-north   31.999999749790824
robot-at-x10y2   move-north   33.99999931401334
robot-at-x11y2   move-north   35.99999823033569
robot-at-x12y2   move-north   37.999995494761464
robot-at-x13y2   move-north   39.99998893655342
robot-at-x14y2   move-north   41.99997335307696
robot-at-x15y2   move-north   43.99993659333782
robot-at-x16y2   move-north   45.999849966559694
robot-at-x17y2   move-north   47.9996647671848
robot-at-x18y2   move-north   49.99916007591848
robot-at-x19y2   move-north   51.99817844121303
robot-at-x20y2   move-north   53.995291619439335
robot-at-x1y3   move-north   13.99999999999951
robot-at-x2y3   move-north   15.999999999995406
robot-at-x3y3   move-north   17.999999999979106
robot-at-x4y3   move-north   19.999999999914422
robot-at-x5y3   move-north   21.99999999957309
robot-at-x6y3   move-north   23.999999998500186
robot-at-x7y3   move-north   25.999999994609148
robot-at-x9y3   move-north   29.999999946621976
robot-at-x10y3   move-north   31.9999998460516
robot-at-x11y3   move-west   33.99999958003137
robot-at-x12y3   move-north   35.99999888755982
robot-at-x13y3   move-north   37.99999716273578
robot-at-x14y3   move-north   39.99999295381876
robot-at-x15y3   move-north   41.999982837314434
robot-at-x16y3   move-north   43.99995869026393
robot-at-x17y3   move-north   45.99990427211325
robot-at-x18y3   move-north   47.999762900348856
robot-at-x19y3   move-west   49.99946139083188
robot-at-x20y3   move-north   51.99862378268576
robot-at-x1y4   move-north   11.999999999999957
robot-at-x2y4   move-north   13.99999999999951
robot-at-x3y4   move-north   15.999999999997453
robot-at-x4y4   move-west   17.99999999998828
robot-at-x5y4   move-north   19.999999999936524
robot-at-x6y4   move-west   21.999999999754806
robot-at-x7y4   move-north   23.999999999061302
robot-at-x8y4   move-north   25.999999996726224
robot-at-x9y4   move-north   27.999999989458658
robot-at-x10y4   move-north   29.999999967811057
robot-at-x12y4   move-north   33.9999997416397
robot-at-x13y4   move-north   35.9999993117573
robot-at-x14y4   move-north   37.99999822714982
robot-at-x15y4   move-north   39.999995555306526
robot-at-x16y4   move-north   41.99998907550952
robot-at-x17y4   move-west   43.999973880990936
robot-at-x18y4   move-north   45.99993589467594
robot-at-x20y4   move-north   49.99962260047221
robot-at-x1y5   move-north   9.999999999999996
robot-at-x2y5   move-north   11.999999999999957
robot-at-x3y5   move-north   13.999999999999734
robot-at-x5y5   move-north   17.999999999991626
robot-at-x7y5   move-north   21.999999999851873
robot-at-x8y5   move-north   23.9999999994451
robot-at-x9y5   move-north   25.999999998080536
robot-at-x10y5   move-north   27.999999993750468
robot-at-x11y5   move-north   29.999999980769083
robot-at-x12y5   move-north   31.999999943707998
robot-at-x13y5   move-north   33.99999984246553
robot-at-x14y5   move-north   35.9999995763326
robot-at-x15y5   move-north   37.99999889887906
robot-at-x16y5   move-north   39.99999721669759
robot-at-x18y5   move-north   43.99998315776922
robot-at-x19y5   move-north   45.99995905555943
robot-at-x20y5   move-north   47.99990031595691
robot-at-x1y6   move-north   8.0
robot-at-x2y6   move-north   9.999999999999996
robot-at-x3y6   move-north   11.999999999999977
robot-at-x4y6   move-north   13.999999999999822
robot-at-x5y6   move-north   15.999999999999032
robot-at-x6y6   move-north   17.99999999999522
robot-at-x7y6   move-west   19.999999999978975
robot-at-x8y6   move-north   21.999999999914433
```


