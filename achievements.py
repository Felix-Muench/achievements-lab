"""Print the GitHub profile achievements and how each one is earned."""

ACHIEVEMENTS = [
    ("Quickdraw", "Close an issue or pull request within 5 minutes of opening it.", None),
    ("Pull Shark", "Get pull requests merged.", [2, 16, 128, 1024]),
    ("YOLO", "Merge a pull request without a review.", None),
    ("Galaxy Brain", "Have an answer accepted in a GitHub Discussion.", None),
    ("Pair Extraordinaire", "Co-author a commit in a merged pull request.", None),
    ("Starstruck", "Own a repository that reaches stars.", [16, 128, 512, 4096]),
    ("Public Sponsor", "Sponsor another user or organisation on GitHub.", None),
]


def main():
    print("GitHub profile achievements\n")
    for name, how, tiers in ACHIEVEMENTS:
        print(f"  {name}")
        print(f"      {how}")
        if tiers:
            print(f"      Tiers: {', '.join(str(t) for t in tiers)}")
        print()


if __name__ == "__main__":
    main()
