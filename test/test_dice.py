import pytest
from dice import Die


def test_validity():
    """Test that a dice roll is valid"""

    d6 = Die()
    outcome = d6.roll()

    assert outcome in range(1, 7)


def test_always_valid():
    """Test that the dice roll is 'always' valid"""

    d6 = Die()

    for i in range(10000):
        outcome = d6.roll()
        assert outcome in range(1, 7)


def test_average_validity():
    """Test that the average dice roll is correct"""

    d6 = Die()

    # Work out the expected average roll of a dice
    expected_avg = sum(range(1, 7)) / 6

    # Running total of dice rolls
    total = 0

    # Number of rolls to perform
    rolls = 1000000

    for i in range(rolls):
        total += d6.roll()

    avg = total / rolls

    # Check equivalence +/- 1%
    assert avg == pytest.approx(expected_avg, rel=1e-2)


def test_fair():
    """ Test that a die is fair. """

    # Intialise a standard, six-sided die.
    d6 = Die()

    # Set the number of rolls.
    rolls = 1000000

    # Create a dictionary to hold the tally for each outcome.
    tally = {}
    for i in range(1, 7):
        tally[i] = 0

    # Roll the die 'rolls' times.
    for i in range(0, rolls):
        tally[d6.roll()] += 1

    # Assert that the probability is correct.
    for i in range(1, 7):
        assert tally[i] / rolls == pytest.approx(1 / 6, 1e-2)

@pytest.mark.parametrize(
    "a",
    list(range(2, 13))
)
def test_double_roll(a):
    """ Test fairness when rolling two six-sided dice """

    # Intialise a standard, six-sided die.
    d6 = Die()

    # Set the number of rolls.
    rolls = 1000000

    # Create a dictionary to hold the tally for each outcome.
    tally = {}
    for i in range(2, 13):
        tally[i] = 0

    # Roll the die 'rolls' times.
    for i in range(0, rolls):
        tally[d6.roll() + d6.roll()] += 1

    # Assert that the probability is correct.
    assert tally[a] / rolls == pytest.approx(prob_double_roll(a, 6), 1e-1)


def prob_double_roll(x, n):
    """
    Expected probabilities for the sum of two dice.
    """
    # For two n-sided dice, the probability of two rolls summing to x is
    # (n − |x−(n+1)|) / n^2, for x = 2 to 2n.

    return (n - abs(x - (n + 1))) / (n ** 2)
