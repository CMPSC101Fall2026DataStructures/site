"""
Tutorial 4: The Guild Roster (TEACHER SOLUTION)
=================================================

This is the completed, bug-free solution for Tutorial 4. Every TODO
from the student starter file has been filled in below.

Learning Objectives:
- Practice creating sets and removing duplicates with set()
- Practice using set operations: intersection (&) and difference (-)
- Practice writing list comprehensions to transform and filter lists
- Practice writing dictionary comprehensions to build new dictionaries

Instructions:
- Run the program using: uv run roster.py
- Check the "Expected" comment next to each print() call to confirm success.
"""


def unique_attendees(sign_in_sheet):
    """
    Find every unique adventurer who signed in, ignoring duplicates.

    Args:
        sign_in_sheet (list): names of adventurers, possibly repeated

    Returns:
        set: the unique names that appear in sign_in_sheet
    """
    return set(sign_in_sheet)


def guild_overlap(guild_a, guild_b):
    """
    Find the adventurers who belong to BOTH guilds.

    Args:
        guild_a (set): members of the first guild
        guild_b (set): members of the second guild

    Returns:
        set: members present in both guild_a and guild_b
    """
    return guild_a & guild_b


def guild_a_exclusive(guild_a, guild_b):
    """
    Find the adventurers who belong ONLY to guild_a, not guild_b.

    Args:
        guild_a (set): members of the first guild
        guild_b (set): members of the second guild

    Returns:
        set: members in guild_a but not in guild_b
    """
    return guild_a - guild_b


def double_damage(attack_powers):
    """
    A power potion was used! Double every attack power in the list.

    Args:
        attack_powers (list): a list of integer attack power values

    Returns:
        list: each value doubled, in the same order
    """
    return [value * 2 for value in attack_powers]


def strong_fighters(attack_powers, threshold=50):
    """
    Keep only the attack powers that meet or exceed `threshold`.
    """
    return [power for power in attack_powers if power >= threshold]


def name_lengths(names):
    """
    Map each adventurer's name to the number of letters in it.

    Args:
        names (list): a list of adventurer name strings

    Returns:
        dict: maps each name to len(name)
    """
    return {name: len(name) for name in names}


def rank_by_level(levels):
    """
    Build a dictionary that flags which adventurers can enter the boss
    room (level 10 or higher).

    Args:
        levels (dict): maps adventurer name -> level (int)

    Returns:
        dict: maps adventurer name -> True/False (level >= 10)
    """
    return {name: level >= 10 for name, level in levels.items()}


def main():
    """
    Run every guild task and print the results.
    """
    print("\n" + "=" * 60)
    print("Tutorial 4: The Guild Roster")
    print("=" * 60)

    print("\n[Task 1] Unique attendees at the guild meeting...")
    sign_in_sheet = ["Aria", "Beck", "Aria", "Cora", "Beck", "Aria"]
    print(f"  unique_attendees(...) -> {unique_attendees(sign_in_sheet)}")
    # Expected: {'Aria', 'Beck', 'Cora'} (order may vary)

    print("\n[Task 2] Members shared between two guilds...")
    guild_a = {"Aria", "Beck", "Cora", "Devi"}
    guild_b = {"Cora", "Devi", "Elan"}
    print(f"  guild_overlap(...) -> {guild_overlap(guild_a, guild_b)}")
    # Expected: {'Cora', 'Devi'} (order may vary)

    print("\n[Task 3] Members exclusive to Guild A...")
    print(f"  guild_a_exclusive(...) -> {guild_a_exclusive(guild_a, guild_b)}")
    # Expected: {'Aria', 'Beck'} (order may vary)

    print("\n[Task 4] Doubling attack power with a power potion...")
    attack_powers = [10, 25, 40, 55, 70]
    print(f"  double_damage(...) -> {double_damage(attack_powers)}")
    # Expected: [20, 50, 80, 110, 140]

    print("\n[Task 5] Filtering for strong fighters (>= 50 power)...")
    print(f"  strong_fighters(...) -> {strong_fighters(attack_powers)}")
    # Expected: [55, 70]

    print("\n[Task 6] Mapping names to name lengths...")
    names = ["Aria", "Beck", "Cora"]
    print(f"  name_lengths(...) -> {name_lengths(names)}")
    # Expected: {'Aria': 4, 'Beck': 4, 'Cora': 4}

    print("\n[Task 7] Ranking adventurers by boss-room eligibility...")
    levels = {"Aria": 12, "Beck": 7, "Cora": 10}
    print(f"  rank_by_level(...) -> {rank_by_level(levels)}")
    # Expected: {'Aria': True, 'Beck': False, 'Cora': True}

    print("\n" + "=" * 60)
    print("If every result above matches its Expected comment, you win!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
