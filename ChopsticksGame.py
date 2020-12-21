from Game import Game
from ChopsticksState import ChopsticksState

class ChopsticksGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        self.current_state = ChopsticksState(p1_starts, (1, 1), (1, 1))

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        instructions = ("Players take turns adding the values of one of their" +
                        " hands to one of their opponents (modulo 5). A hand" +
                        " with a total of 5 (or 0; 5 modulo 5) is considered " +
                        "'dead'. The first player to have 2 dead hands is the" +
                        "loser.")
        return instructions

    def is_over(self, state):
        """
        Return whether or not this game is over at state.

        :return: True if the game is over at state, False otherwise.
        :rtype: bool
        """
        return state.p1_hand == (0, 0) or \
               state.p2_hand == (0, 0)

    def is_winner(self, player):
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        return self.current_state.get_current_player_name() != player and \
               self.is_over(self.current_state)

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        :param string:
        :type string:
        :return:
        :rtype:
        """
        return string.strip().lower()
