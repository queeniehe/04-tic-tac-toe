#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is the gambit: 10k matches and no losses.
"""

from t3 import *

def monkey_match():
  """
  This is the method that you will be graded with -- you can't lose to random play.
  """

  print("Monkey Match :: ", end = "")
  for x in range(10000):
    g = game(c1 = monkey, c2 = computer)
    outcome = g.play()
    if outcome and outcome != g.vmark:
      print
      print("Game {} :: monkey {} has won!!".format(x, outcome))
      print(g)
      sys.exit()

  print("Great work -- no losses!!!")

monkey_match()

