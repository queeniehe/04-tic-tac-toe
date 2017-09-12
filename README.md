# Homework 4: Tic Tac Toe

Tic Tac Toe -- child's play, right?  You probably know that perfectly played games will always result in a draw.  In this assignment you will implement a computer's strategy for the game.

You will play against a random player -- a "monkey."  Let's call him Harry.  Since Harry plays randomly, you will beat him most of the time.  But here's the thing: he's going to pull a lot of antics things you might not expect, and you can _never_ lose.  You will each start about half the matches.

You may work in pairs for this 

## Your Task

In this repository, you will find `t3.py`, `human_match.py`, and `monkey_match.py`.

Check out the documentation by doing `pydoc t3` from the command line.  In `t3.py`, you will find, a `player` class that is inherited by a `monkey`, a `human`, and a `computer`.

The file also includes the `game` class, which includes a board and defines the game play.  The board is defined as a list 9 elements long that initially consists of copies of `None` and is filled in with X's and O's with each move.  If you print the game, it will convert the board to string, and should be readily comprehensible.  The `game` also takes care of switching back and forth between the two players, rejecting invalid moves (filled squares), and ultimately declaring a winner.  

You will implement the computer's `move()` function.  Note that this is part of a class (woohoo!), but all of your work should be oconfided to the function.  I suggest that you implement the strategy from the Newell & Simon strategy from the Wikipedia page on Tic-Tac-Toe (listed 1-8, [here](https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy)). 

1. Win if possible
2. Block your opponent from winning.
3. Create a fork
4. Force your opponent to play defense, if it does not result in a fork.
5. Block your opponent from taking a fork.
6. Take the center.
7. Take a corner opposite your opponent.
8. Take an empty corner.
9. Take a side.

Though your computer will start all its matches in the center, this is a self-consistent strategy that will never lose.

This approach is laid out in `t3.py`.  Fortunately for you, `game` also defines `check_for_wins()` and `check_for_twos()`, which should prove useful to you in evaluating the conditions.  You can use other strategies if you want, but TAs will issue partial credit for the following defined strategies.

Of these strategies, #4 may be particularly difficult.  You can see code for it below, if you get stuck.
&nbsp;<details><summary>Strategy for #4, "Force Defense"</summary>
We're interested in forcing your opponent to play defense, but _only it does not result in a fork_ for them.  The first condition just means that we create a two that they have have to block.  The second piece means that that two must not give them a fork -- a sure-win.
```python
# Get posible squares to play for a "two"
self_twos = match.check_for_twos(self.mark)
  
# We'll now consider hypothetical games, 
# where we play in each of the "two" positions.
for i in self_twos:                 # For each of these
    hypo_match = dc(match)          # create a copy of the game.
    hypo_match.board[i] = self.mark # try playing there.
    
    # Now look for the win implied by your "two".
    # Your opponent would have to play here.
    w = hypo_match.check_for_wins(self.mark) 
    
    # For your OPPPONENT, get any potential twos.
    hypo_twos = hypo_match.check_for_twos(self.other_mark)
    
    # If your potential win is not just a two for them,
    # but in fact a DOUBLE two -- a fork -- don't move here!
    if w in hypo_twos and hypo_twos[w] > 1: continue
    
    # Otherwise, it meets the condition.  Do it!!
    return i
```
</details></br></br>


With `./human_match.py`, you can play against the computer.  Alternatively, `./monkey_match.py` launches 10000 games against a random player.  The former will probably prove useful for debugging; the latter will serve for your grade.

<img src="img/monkey_computer.jpg" width=600px>
Game on!
