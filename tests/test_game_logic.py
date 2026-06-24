# from logic_utils import check_guess

# def test_winning_guess():
#     # If the secret is 50 and guess is 50, it should be a win
#     result = check_guess(50, 50)
#     assert result == "Win"

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     result = check_guess(60, 50)
#     assert result == "Too High"

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     result = check_guess(40, 50)
#     assert result == "Too Low"

from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

# --- check_guess tests (fixed to unpack tuple) ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# --- Bug fix verification tests ---

def test_inverted_hint_bug_fixed():
    # Secret=71, guess=72 should be Too High (was broken before)
    outcome, message = check_guess(72, 71)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_inverted_hint_bug_fixed_low():
    # Secret=71, guess=68 should be Too Low (was broken before)
    outcome, message = check_guess(68, 71)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# --- parse_guess tests ---

def test_parse_valid_guess():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42

def test_parse_empty_guess():
    ok, value, err = parse_guess("")
    assert ok == False

def test_parse_invalid_guess():
    ok, value, err = parse_guess("abc")
    assert ok == False

# --- get_range_for_difficulty tests ---

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

# --- update_score tests ---

def test_score_increases_on_win():
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_score_decreases_on_wrong_guess():
    new_score = update_score(50, "Too High", 1)
    assert new_score < 50