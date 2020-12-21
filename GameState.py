class GameState:
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn):
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        :param is_p1_turn:
        :type is_p1_turn:
        """
        self.p1_turn = is_p1_turn

    def __str__(self):
        """
        Return a string representation of the current state of the game.

        :return: A string representation of this GameState.
        :rtype: str
        """
        raise NotImplementedError

    def get_possible_moves(self):
        """
        Return all possible moves that can be applied to this state.

        :return: A list of moves that can be applied to this state.
        :rtype: List
        """
        raise NotImplementedError

    def get_current_player_name(self):
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.

        :return: The next player to make a move on this GameState.
        :rtype: str
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move):
        """
        Return the GameState that results from applying move to this GameState.

        :param move: The move to apply.
        :type move: Object
        :return: The resulting GameState after applying move to this GameState.
        :rtype: GameState
        """
        raise NotImplementedError

    def is_valid_move(self, move):
        """
        Return whether move is a valid move for this GameState.

        :param move: The move to verify.
        :type move: Object
        :return: Whether move is a valid move or not.
        :rtype: bool
        """
        raise NotImplementedError

    def __repr__(self):
        """
        Return a representation of this state (which can be used for
        equality testing).

        :return:
        :rtype:
        """
        raise NotImplementedError
