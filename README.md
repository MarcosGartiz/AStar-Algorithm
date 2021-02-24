# AStar-Algorithm
<h2>A* Algorithm</h2>
it is a graph search algorithm and use a heuristic function to evaluate each node. When the heuristic is admissible, ensure that the found solution it is optimal.<br>
It uses two auxiliary structures:<br>
 Open: it is a priority queue for nodes not visited.<br>
 Closed: is the set of visited nodes.<br>
<strong>Expand(u)</strong><br>
Function to explore the best possible states on the system, same that need to create a temporal list of numbers that I copied from the original list<br>. It could evaluate the puzzle previously created and each node to create the new list to show simulating the best move to resolve the puzzle 8.<br>
  
<strong>Manhattan Heuristic</strong><br>
consists of the sum of the distance from Manhattan of all the boxes.<br>
It is based on the sequence that the final state.<br>
  For each tile on the board<br>
  if the token is different from 0:<br>
  if it is in the center → 1<br>
  if he is not in the center and his successor in the sequence is not the corresponding → 2<br>

