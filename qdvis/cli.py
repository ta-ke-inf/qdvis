import argparse
import os
import sys

from django.core.management import execute_from_command_line


def main() -> None:
    parser = argparse.ArgumentParser(description="Launch Visualization Tool")
    parser.add_argument("--port", type=int, default=8000, help="number of port")
    parser.add_argument("--logpath", type=str, help="path to log file")
    args = parser.parse_args()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    sys.path.append(project_root)

    if args.logpath:
        os.environ["LOG_PATH"] = args.logpath
        if not os.path.isfile(args.logpath):
            print(f"Not found file: {args.logpath}")
            sys.exit(1)
    else:
        print(
            "Error: The '--logpath' argument is required. Please specify the log file path. Example usage: qdvis --logpath /path/to/logfile"
        )
        sys.exit(1)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    execute_from_command_line([sys.argv[0], "runserver", str(args.port)])


if __name__ == "__main__":
    main()
