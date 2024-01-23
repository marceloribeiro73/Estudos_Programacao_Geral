#%%
"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card == 'A':
        value =  1
    elif card in ['K','Q','J']:
        value = 10
    elif int(card) >=2 and int(card) <=10:
        value = int(card)
    else:
        raise ValueError('Card is invalid or a Joker, please inform a valid card')
    
    return value
    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one == value_card_two:
        result = card_one, card_two
    elif value_card_one > value_card_two:
        result = card_one
    else:
        result = card_two
    
    return  result


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    value_card_one = value_of_card(card_one)
    value_card_one = value_card_one if value_card_one != 1 else 11
    value_card_two = value_of_card(card_two)
    value_card_two = value_card_two if value_card_two != 1 else 11

    if value_card_one + value_card_two > 10:
        value =  1
    else:
        value =  11

    return value



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    is_blackjack_var = (value_card_one in [10,'K','Q','J'] or value_card_two in [10,'K','Q','J']) and (value_card_one == 1 or value_card_two == 1)
    
    return is_blackjack_var



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    is_split = bool(value_card_one == value_card_two)
    return is_split


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    value_total = value_card_one + value_card_two
    #is_double = bool(value_total >= 9 and value_total<=11)
    is_double = bool(9 <= value_total <= 11)
    return is_double
#%%
#value_of_card('')
#higher_card('A','A')
#value_of_ace('A','7')
#is_blackjack('A','10')
#can_split_pairs('A','3')
can_double_down('A','A')