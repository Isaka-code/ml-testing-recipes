import random


def test_random_seed():
    random.seed(42)
    seq1 = [random.random() for _ in range(10)]

    random.seed(42)
    seq2 = [random.random() for _ in range(10)]

    assert seq1 == seq2, "同じseedでも結果が再現できません"
