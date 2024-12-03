import subprocess
import sys

from pathlib import Path
from typing import List


def run(args: List[str]):
    command = [f'{Path(__file__).parent}/docker-compose'] + args[1:]
    result = subprocess.run(command, stdout=sys.stdout, stderr=sys.stderr)


def docker_compose():
    run(sys.argv)


if __name__ == '__main__':
    docker_compose()
