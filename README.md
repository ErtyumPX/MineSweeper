# MineSweeper

Good old Mine Sweeper game in python, made with Tkinter, using object-oriented programming.

![Image of the Game](https://github.com/ErtyumPX/MineSweeper/blob/main/image_game.jpeg)

<p align="center">
  <img width="460" height="300" src="http://www.fillmurray.com/460/300">
</p>


Algorithm:

The game starts when the user clicks any node (which is a tkinter.Button object) of the board.

Then algorithm creates the mine field according to the first node user clicked in such a way that there will not be any mine near the first node.

In the rest of the game, whenever user clicks a node, that node reveals itself.

- If the node is a mine, it's game over.

- If the nodes value is 0, which means that there is no mine covers that node, it will reveal the nodes next to it as well.
