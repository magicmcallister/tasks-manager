import argparse
import datetime


def main():
    parser = generate_parser()
    args = parser.parse_args()
    process_action(args)


def process_action(args):

    if args.command == "tasks":
        pass

    elif args.command == "new":
        print(args.title)
        print(args.body)
        print(args.date)
        print(args.event)


def generate_parser():
    """Generate the parser architecture"""

    # Generate the parser architecture
    parser = argparse.ArgumentParser(description="Tasks Manager Command Line")

    parser.add_argument(
        "--dryrun",
        action="store_true",
        help="Test",
    )
    subparsers = parser.add_subparsers(dest="command", title="actions")

    # Parent parser for shared args
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--dryrun",
        action="store_true",
        help="Test",
    )

    # Command: Tasks
    parser_list_tasks = subparsers.add_parser("tasks", help="List Tasks", parents=[parent_parser])
    parser_list_tasks.add_subparsers(dest="subcommand", help="List Tasks")
    parser_list_tasks.add_argument(
        "-d",
        "--date",
        help="Filter the tasks that are shown by date",
        default=datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    parser_list_tasks.add_argument(
        "-f",
        "--filter",
        metavar="LIST_TASKS_FILTER",
        choices=["all", "opened", "closed"],
        help="Filter the tasks that are shown by state",
        default="opened",
    )

    # Command: New Task
    parser_new_task = subparsers.add_parser(
        "new", help="Create a new task", parents=[parent_parser]
    )
    parser_new_task.add_subparsers(dest="subcommand", help="Create a new task")
    parser_new_task.add_argument("-t", "--title", help="Title of a new task", required=True)
    parser_new_task.add_argument(
        "-b",
        "--body",
        help="Body of a new task",
    )
    parser_new_task.add_argument(
        "-d",
        "--date",
        help="Date of a new task. Format YYYY:MM:DD",
        default=datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    parser_new_task.add_argument(
        "-e",
        "--event",
        default=False,
        action="store_true",
        help="Mark task as event",
    )

    return parser


if __name__ == "__main__":
    main()
