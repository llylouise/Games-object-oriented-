from GameState import GameState

class ChopsticksState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn, p1_hand, p2_hand):
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        :param is_p1_turn:
        :type is_p1_turn:
        """
        self.p1_turn = is_p1_turn
        self.p1_hand = p1_hand
        self.p2_hand = p2_hand

    def __str__(self):
        """
        Return a string representation of the current state of the game.

        :return: A string representation of this GameState.
        :rtype: str
        """
        return "Player 1: {} - {}; Player 2: {} - {}".format(self.p1_hand[0],
                                                             self.p1_hand[1],
                                                             self.p2_hand[0],
                                                             self.p2_hand[1],)

    def get_possible_moves(self):
        """
        Return all possible moves that can be applied to this state.

        :return: A list of moves that can be applied to this state.
        :rtype: List
        """
        current_hands, other_hands = self.p2_hand, self.p1_hand
        if self.p1_turn:
            current_hands, other_hands = self.p1_hand, self.p2_hand

        hands = 'lr'
        moves = []

        for i in range(len(hands)):
            if current_hands[i] != 0:
                for j in range(len(hands)):
                    if other_hands[j] != 0:
                        moves.append(hands[i] + hands[j])

        return moves

    def make_move(self, move):
        """
        Return the GameState that results from applying move to this GameState.

        :param move: The move to apply.
        :type move: Object
        :return: The resulting GameState after applying move to this GameState.
        :rtype: GameState
        """
        current_hands, other_hands = list(self.p2_hand), list(self.p1_hand)
        if self.p1_turn:
            current_hands, other_hands = list(self.p1_hand), list(self.p2_hand)

        hand_to_modify = 0
        hand_to_use = 0

        if move[0] == 'r':
            hand_to_use = 1
        if move[1] == 'r':
            hand_to_modify = 1

        other_hands[hand_to_modify] += current_hands[hand_to_use]
        other_hands[hand_to_modify] %= 5

        new_p1_hand, new_p2_hand = tuple(other_hands), tuple(current_hands)
        if self.p1_turn:
            new_p1_hand, new_p2_hand = tuple(current_hands), tuple(other_hands)

        new_state = ChopsticksState(not self.p1_turn,
                                        new_p1_hand, new_p2_hand)
        return new_state

    def is_valid_move(self, move):
        """
        Return whether move is a valid move for this GameState.

        :param move: The move to verify.
        :type move: Object
        :return: Whether move is a valid move or not.
        :rtype: bool
        """

        return move in self.get_possible_moves()

    def __repr__(self):
        """
        Return a representation of this state (which can be used for
        equality testing).

        :return:
        :rtype:
        """
        p1_hand_sorted = (min(self.p1_hand), max(self.p1_hand))
        p2_hand_sorted = (min(self.p2_hand), max(self.p2_hand))

        return "P1's Turn: {} - P1's Hand: {} - P2's Hand: {}".format(
            self.p1_turn, p1_hand_sorted, p2_hand_sorted)
