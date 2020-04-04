# Tic-Tac-Toe

Tic-Tac-Toe game implemented using Python and Turtle Graphics!

## Getting Started

Download the files above and follow the steps below.

### Installing

Open the terminal, navigate to where you want the game's files to be stored in and create a new directory:

``` bash
mkdir DIRECTORY_NAME
```

Enter the new directory:

``` bash
cd DIRECTORY_NAME
```

Create and activate a new virtual environment:

``` bash
python3 -m venv myenv
source myenv/bin/activate
```

Copy the downloaded files into the virtual environment created and enter the virtual environment:

``` bash
cd myenv
```

Run the following line to install all dependencies for the game:

``` bash
pip3 install -r requirements.txt
```

## Usage

Start the game by running this line in the terminal:

``` bash
python tic-tac-toe.py
```

A turtle graphics screen will popup which contains the game's grid. Enter in one of the following moves to place either an X or O at the corresponding position:

* centre
* top
* bottom
* left
* right
* top left
* top right
* bottom left
* bottom right

or enter in 'end' to stop the game. Good luck!

### Note

If attempting to make a move results in a NameError exception, ensure all moves (as well as 'end' to stop the game) are placed within single quotes.
