import argparse
import asyncio
from main import main as run_bot


def main():
    parser = argparse.ArgumentParser(
        description="Команды для lifemart-shift-bot")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # runbot
    subparsers.add_parser("runbot", help="Run Telegram bot")

    # add_user
    subparsers.add_parser(
        "add_user", help="Add user to a database")

    args = parser.parse_args()

    if args.command == "runbot":
        asyncio.run(run_bot())
    elif args.command == "add_user":
        pass
        # asyncio.run(add_user_interactive())
    else:
        print("Unknown command:", args.command)


if __name__ == "__main__":
    main()
