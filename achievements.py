"""Print the GitHub profile achievements and how each one is earned."""

import argparse

ACHIEVEMENTS = [
    ("Quickdraw", "Close an issue or pull request within 5 minutes of opening it.", None, True),
    ("Pull Shark", "Get pull requests merged.", [2, 16, 128, 1024], True),
    ("YOLO", "Merge a pull request without a review.", None, True),
    ("Galaxy Brain", "Have an answer accepted in a GitHub Discussion.", None, True),
    ("Pair Extraordinaire", "Co-author a commit in a merged pull request.", None, False),
    ("Starstruck", "Own a repository that reaches stars.", [16, 128, 512, 4096], False),
    ("Public Sponsor", "Sponsor another user or organisation on GitHub.", None, False),
]


def main(solo_only=False):
    print("GitHub profile achievements\n")
    for name, how, tiers, solo in ACHIEVEMENTS:
        if solo_only and not solo:
            continue
        print(f"  {name}")
        print(f"      {how}")
        if tiers:
            print(f"      Tiers: {', '.join(str(t) for t in tiers)}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--solo",
        action="store_true",
        help="only show achievements you can earn on your own repositories",
    )
    args = parser.parse_args()
    main(solo_only=args.solo)
