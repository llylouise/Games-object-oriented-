import random
from typing import Any

class Node:
    def __init__(self, parent, state):
        self.parent = parent
        self.state = state
        self.applied_move = None
        self.value = None
        self.best_child = None
        self.children = None

def random_strategy(game):
    possible_moves = game.current_state.get_possible_moves()
    return possible_moves[random.randint(0, len(possible_moves) - 1)]

def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

def iterative_minimax_strategy(game):
    """
    Return the move that guarantees the highest score in this game for its
    current player by using an iterative minimax implementation.

    :param game:
    :type game:
    :return:
    :rtype:
    """
    state = game.current_state
    node_stack = [Node(None, state)]
    main_node = node_stack[0]
    current_player = state.get_current_player_name()

    while node_stack:
        current_node = node_stack[0]
        current_state = current_node.state

        # If the node's children is None, then this state hasn't been seen yet
        if current_node.children == None:
            current_moves = current_state.get_possible_moves()
            current_node.children = []

            # Add each possible move into the stack and leave the node in it
            for move in current_moves:
                new_state = current_state.make_move(move)
                new_node = Node(current_node, new_state)
                new_node.applied_move = move
                node_stack.insert(0, new_node)
                current_node.children.append(new_node)
        else:
            node_player = current_state.get_current_player_name()
            # This node was explored previously; all of its children should
            # be fully expanded and simplified now.
            if current_node.children == []:
                # It's a leaf node; the game is over at this state
                other_player = 'p2'
                if current_player == 'p2':
                    other_player = 'p1'

                # This should be replaced with a way of checking the winner
                # properly using game, but we currently can't do that with
                # states. TODO: Fix this
                if node_player == current_player:
                    current_node.value = -1
                elif node_player == other_player:
                    current_node.value = 1
                else:
                    current_node.value = 0
            else:
                # All of the children have values; find the best one
                best_child = None
                if node_player == current_player:
                    # We want the maximum value
                    best_value = -2
                else:
                    # We want the minimum value
                    best_value = 2

                for child in current_node.children:
                    if (node_player == current_player and
                        child.value > best_value):
                        best_value = child.value
                        best_child = child
                    elif (node_player != current_player and
                          child.value < best_value):
                        best_value = child.value
                        best_child = child

                current_node.value = best_value
                current_node.best_child = best_child
            node_stack.pop(0)

    # At this point, main_node should have its best_value and best_child
    # Return the move used to get to the best_child
    return main_node.best_child.applied_move


def recursive_minimax_strategy(game):
    """
    Return the move that guarantees the highest score in this game for its
    current player by using a recursive minimax implementation.

    :param game:
    :type game:
    :return:
    :rtype:
    """
    # TODO: This version uses memoization; remove it later.
    states_dictionary = {}
    current_state = game.current_state
    p1_turn = current_state.get_current_player_name() == "p1"

    moves = current_state.get_possible_moves()
    best_score = -2
    best_move = None
    for move in moves:
        new_state = current_state.make_move(move)
        score = minimax_memoization_helper(new_state, states_dictionary,
                                        not p1_turn, game) * -1
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def minimax_memoization_helper(state, states_dictionary, p1_turn, game):
    if state.__repr__() in states_dictionary:
        if states_dictionary[state.__repr__()] == None:
            # We've been to this state but it hasn't been filled in yet, so
            # there's a cycle.
            return 0

        return states_dictionary[state.__repr__()]
    else:
        states_dictionary[state.__repr__()] = None

    if game.is_over(state):
        old_state = game.current_state
        game.current_state = state

        if game.is_winner("p1" if p1_turn else "p2"):
            ret_val = 1
        elif game.is_winner("p2" if p1_turn else "p1"):
            ret_val = -1
        else:
            ret_val = 0

        game.current_state = old_state
        states_dictionary[state.__repr__()] = ret_val
        return ret_val

    moves = state.get_possible_moves()
    all_scores = []
    for move in moves:
        new_state = state.make_move(move)
        score = minimax_memoization_helper(new_state, states_dictionary,
                                        not p1_turn, game)
        all_scores.append(score * -1)

    states_dictionary[state.__repr__()] = max(all_scores)
    return max(all_scores)


def recursive_minimax_alphabeta_strategy(game):
    """
    Return the move that guarantees the highest score in this game for its
    current player by using a recursive minimax implementation.

    :param game:
    :type game:
    :return:
    :rtype:
    """
    current_player = game.current_state.get_current_player_name()
    best_score = -2
    best_move = None
    alpha = -2
    beta = 2

    for move in game.current_state.get_possible_moves():
        new_state = game.current_state.make_move(move)
        score = recursive_minimax_alphabeta_helper(new_state, current_player,
                                                   alpha, beta, game)
        if score > best_score:
            best_move = move
            best_score = score

    return best_move


def recursive_minimax_alphabeta_helper(state, current_player, alpha, beta, game):
    """
    Return the best possible score that could be obtained by current_player
    in this state.

    :param state:
    :type state:
    :param current_player:
    :type current_player:
    :return:
    :rtype:
    """
    # The game is over if there are no moves left
    if game.is_over(state):
        loser = state.get_current_player_name()
        other_player = 'p2'
        if current_player == 'p2':
            other_player = 'p1'

        if loser == current_player:
            return -1
        elif loser == other_player:
            return 1
        return 0

    # There are still moves left: Return the inversion of all of the previous
    # moves
    if current_player == state.get_current_player_name():
        # Make alpha cuts
        max_val = -2
        for move in state.get_possible_moves():
            new_state = state.make_move(move)
            result = recursive_minimax_alphabeta_helper(new_state,
                                                                 current_player,
                                                                 alpha, beta, game)
            max_val = max(result, max_val)
            alpha = max(result, alpha)
            if beta <= alpha:
                break
        return max_val
    else:
        # Make beta cuts
        min_val = 2
        for move in state.get_possible_moves():
            new_state = state.make_move(move)
            result = recursive_minimax_alphabeta_helper(new_state,
                                                                 current_player,
                                                                 alpha, beta, game)
            min_val = min(result, min_val)
            beta = min(result, beta)
            if beta <= alpha:
                break
        return min_val
