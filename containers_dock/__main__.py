import sys

from containers_dock.app import App


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    app = App()
    app.run()


if __name__ == "__main__":
    main()
