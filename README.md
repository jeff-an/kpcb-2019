# Terminal Blackjack 
<img src="http://drive.google.com/uc?id=1amPwUOcFcWCe5GOGRG2_OeDxMNq0JMLH" width="300" height="500" />

## Instructions
### Dependencies
You must have Python 3.x installed in order to run Terminal Blackjack. To install Python, please visit [the official Python website](https://www.python.org/downloads/).

The rest of this document will assume that you have Python installed and available in your PATH.

### Quick Start
Clone the repository:
```
git clone https://github.com/jeff-an/kpcb-2019.git
```

Full screen your terminal window so that the ASCII cards can fit on a single line. This will make it easier to read your hand.
Run the program:
```
python kpcb-2019
```

## Design Choices
### Object Oriented Design
The game is designed in an object oriented fashion, with separate classes for cards, decks, and game rounds. I made this decision to group functionality into classes for a number of reasons:

 - Cards, decks, and game rounds are connected by meaningful relationships. Decks contain 52 cards that each have a unique rank and suit. Game rounds require a single deck that must be shuffled before the next round. These relationships are easy to identify for future developers when the code is factored into classes.

 - Object oriented programming allows for code-reuse. For example, all types of cards, regardless of suit or rank, can re-use the same code for pretty-printing in ASCII. 

- Customization of behavior is easy. If developers need to add to existing behavior anytime in the future the amount of work required is minimal; to use a deck that has Jokers, for example, developers need to simply subclass the existing Card class and add Joker as an available Value type.

### ASCII Art
Another important design consideration was the question of how to represent cards to the user. My initial thought was to use the simplest representation, a tuple of suit and rank. This would be extremely easy to implement but would likely be confusing to users who are accustomed to playing with real cards. As such, to make the user experience as authentic and seamless, I decided to represent cards as ASCII art.

### Non-destructive Deck
Finally, I made the decision to code the Deck class in a non-destructive manner; in other words, when asked to deal cards, the deck only returns references to cards it holds and never "pops" cards off the stack. This has two key memory and performance implications:

- Decks can be re-used instead of being reconstructed after every round of Blackjack. This means that the memory usage of the program remains constant regardless of how many rounds the player plays.

- Shuffling is easy to implement. We don't have to handle pushing cards that we dealt back onto the stack.


## Data Structures and Algorithms
The main data structures used in this program as well as their purposes are listed below:

| Data Structure        | Purpose            |
| --------------------- |:------------------:|
| Arraylist / Stack | Store the deck of cards and the hands of each player |
| Hashmap | Map suits to their ASCII representations |
| Set | Store the legal values for suit and rank to ensure no invalid cards are created |


## Tooling
I chose to use as little tooling as possible for this possible in order to make the setup process as simple as possible for the user. As such, my program only requires Python with no additional external packages.

If my Terminal Blackjack program were to grow in popularity, however, I would aim to improve the existing UI/UX and add additional functionality such as betting. These features could require additional dependencies, so I have added a Dockerfile as an example of the tooling I could use to ensure my program remains portable.