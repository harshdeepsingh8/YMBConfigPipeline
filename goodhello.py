"""YMB greeting module — used for CI pipeline testing."""


def hello():
    """Print a greeting from the YMB banking app."""
    print("Hello, DevOps learner!")


def bye():
    """Print a farewell from the YMB banking app."""
    print("Goodbye!")


if __name__ == "__main__":
    hello()
    bye()