"""Print the GitHub profile achievements and how each one is earned."""

ACHIEVEMENTS = [
    ("Quickdraw", "Close an issue or pull request within 5 minutes of opening it."),
    ("Pull Shark", "Get pull requests merged. Tiers at 2, 16, 128 and 1024."),
    ("YOLO", "Merge a pull request without a review."),
    ("Galaxy Brain", "Have an answer accepted in a GitHub Discussion."),
    ("Pair Extraordinaire", "Co-author a commit in a merged pull request."),
    ("Starstruck", "Own a repository that reaches 16 stars."),
    ("Public Sponsor", "Sponsor another user or organisation on GitHub."),
]


def main():
    print("GitHub profile achievements\n")
    for name, how in ACHIEVEMENTS:
        print(f"  {name}")
        print(f"      {how}\n")


if __name__ == "__main__":
    main()
