"""Minimal example for ConnectFour."""

from connectfour import connectfour


def main():
 runner = connectfour({"name": "ConnectFour", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()