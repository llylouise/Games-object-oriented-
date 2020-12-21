from GameState import GameState

class SubtractSquareState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn, current_total):
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        :param is_p1_turn:
        :type is_p1_turn:
        """
        self.p1_turn = is_p1_turn
        self.current_total = current_total

    def __str__(self):
        """
        Return a string representation of the current state of the game.

        :return: A string representation of this GameState.
        :rtype: str
        """
        return "Current total: {}".format(self.current_total)

    def get_possible_moves(self):
        """
        Return all possible moves that can be applied to this state.

        :return: A list of moves that can be applied to this state.
        :rtype: List
        """
        moves = []
        for i in range(1, self.current_total + 1):
            if i ** 2 <= self.current_total:
                moves.append(i ** 2)

        return moves

    def make_move(self, move):
        """
        Return the GameState that results from applying move to this GameState.

        :param move: The move to apply.
        :type move: Object
        :return: The resulting GameState after applying move to this GameState.
        :rtype: GameState
        """
        if type(move) == str:
            move = int(move)

        new_state = SubtractSquareState(not self.p1_turn,
                                        self.current_total - move)
        return new_state

    def is_valid_move(self, move):
        """
        Return whether move is a valid move for this GameState.

        :param move: The move to verify.
        :type move: Object
        :return: Whether move is a valid move or not.
        :rtype: bool
        """
        if type(move) == str:
            move = int(move)

        return move in self.get_possible_moves()

    def __repr__(self):
        """
        Return a representation of this state (which can be used for
        equality testing).

        :return:
        :rtype:
        """
        return "P1's Turn: {} - Total: {}".format(self.p1_turn,
                                                  self.current_total)
