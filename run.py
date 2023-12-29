import os
import re
import signal
import subprocess
import sys
import time

import requests
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from urllib.parse import urlencode

year = sys.argv[1]
day = sys.argv[2]
day_path = os.path.join(sys.path[0], year, day.zfill(2))
parts = {
    1: {
        "part": 1,
        "path": os.path.join(day_path, '1.py'),
        "answer_path": os.path.join(day_path, '1.py.out'),
    },
    2: {
        "part": 2,
        "path": os.path.join(day_path, '2.py'),
        "answer_path": os.path.join(day_path, '2.py.out'),
    }
}
example_call_line = '\nexample_matched = aoc("example.txt", "EXAMPLE_ANSWER")  # EXAMPLE_MARKER\n'



def copy_with_replaced_example(source, dest, replacement):
    with open(source) as f:
        template = f.read()
        example_replaced = example_call_line.replace('"EXAMPLE_ANSWER"', replacement)
        template = re.sub(r'\n.*?# EXAMPLE_MARKER\n', example_replaced, template)
        with open(dest, 'w') as f2:
            f2.write(template)


def load_day():
    print(f"Loading day {year}/{day}")
    if os.path.exists(day_path):
        print("Day already prepared")
        return

    os.makedirs(day_path, exist_ok=True)

    response = request_aoc(requests.get, f"https://adventofcode.com/{year}/day/{day}/input")
    if not response.ok:
        print("Your session_cookie seems to be invalid, please double-check.")
        sys.exit()

    with open(os.path.join(day_path, 'input.txt'), 'w') as f:
        f.write(response.text.rstrip("\n"))

    print('Please enter the example content:\n')

    example_lines = []
    while True:
        example_line = input()
        if example_line:
            example_lines.append(example_line)
        else:
            break
    example = '\n'.join(example_lines)

    with open(os.path.join(day_path, 'example.txt'), 'w') as f:
        f.write(example)

    example_answer = input('Please enter the example answer: ')

    copy_with_replaced_example(os.path.join(sys.path[0], 'template', '1.py'), parts[1]["path"], example_answer)


def request_aoc(method, url, headers=None, data=None):
    cookie_path = os.path.join(sys.path[0], 'session_cookie')
    if not os.path.isfile(cookie_path):
        print("Please provide a session_cookie file next to the script to be able to use it.")
        print("The session_cookie is set by the Advent of Code website, can be retrieved via the browser and should be 96 random hexadecimal chars.")
        sys.exit()

    headers = headers or {}
    headers["cookie"] = f"session={open(cookie_path).read().strip()}"
    return method(url, headers=headers, data=data)


class SolutionChangeHandler(FileSystemEventHandler):
    def __init__(self, part):
        super().__init__()
        self.part = part
        self.running = None
        self.submitted_successfully = False

    def on_modified(self, event):
        if event.src_path == parts[self.part]["path"]:
            self.run_solution()

        if event.src_path == parts[self.part]["answer_path"]:
            self.submit_solution()


    def run_solution(self):
        if self.running:
            try:
                pid = os.getpgid(self.running.pid)
                os.killpg(pid, signal.SIGKILL)
                print("... Aborted")
            except ProcessLookupError:
                ...

        print("\nRunning solution")
        cmd = f"python {parts[self.part]['path']} {parts[self.part]['answer_path']}"
        self.running = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)


    def submit_solution(self):
        with open(parts[self.part]['answer_path']) as f:
            solution = f.read()

        print(f"Submitting solution {solution}")
        solution_data = urlencode({
            "level": self.part,
            "answer": solution
        })
        response = request_aoc(
            requests.post,
            f"https://adventofcode.com/{year}/day/{day}/answer",
            data=solution_data,
            headers={"content-type": "application/x-www-form-urlencoded"}
        )
        response_text = response.text
        right = "s the right answer" in response_text
        if right:
            print("Submission was correct")
            self.submitted_successfully = right


def run_day_solution_part(part):
    print(f"\n\nSolving day part {part}")

    solution_runner = SolutionChangeHandler(part)
    solution_observer = Observer()
    solution_observer.schedule(solution_runner, day_path)
    solution_observer.start()
    solution_runner.run_solution()

    try:
        while not solution_runner.submitted_successfully:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(1)

    solution_observer.stop()
    solution_observer.join()


def prepare_part_two():
    print("\n\nPreparing part 2")

    example_answer = input('Please enter the example answer for part 2: ')

    copy_with_replaced_example(parts[1]["path"], parts[2]["path"], example_answer)


def main():
    load_day()
    if not os.path.exists(parts[1]["answer_path"]):
        run_day_solution_part(1)
        if not os.path.exists(parts[2]["path"]):
            prepare_part_two()

    if not os.path.exists(parts[2]["answer_path"]):
        run_day_solution_part(2)

    print("\nBoth parts complete")


if __name__ == '__main__':
    main()