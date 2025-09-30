#!/usr/bin/env python3
"""Simple judge runner:
Usage: python3 run_tests.py problems/practice/sample_problem
It runs the `solution` executable (if exists) or solution.py file and compares output.
"""
import sys
import subprocess
import pathlib
import difflib

def run(problem_dir):
    problem_dir = pathlib.Path(problem_dir)
    input_files = list(problem_dir.glob('input/*.txt'))
    expected_files = list(problem_dir.glob('output/*.txt'))
    if not input_files:
        print('No input files found in', problem_dir)
        return 1
    # choose first input/expected pair if present
    inp = input_files[0]
    exp = expected_files[0] if expected_files else None

    # try python solution
    py = problem_dir / 'solution.py'
    exe = problem_dir / 'solution'
    if py.exists():
        proc = subprocess.run(['python3', str(py)], input=inp.read_bytes(), stdout=subprocess.PIPE)
        out = proc.stdout.decode()
    elif exe.exists():
        proc = subprocess.run([str(exe)], input=inp.read_bytes(), stdout=subprocess.PIPE)
        out = proc.stdout.decode()
    else:
        print('No solution found (place solution.py or an executable named "solution")')
        return 2

    if exp:
        want = exp.read_text()
        if out.strip() == want.strip():
            print('OK')
            return 0
        else:
            print('Wrong answer — diff:')
            for line in difflib.unified_diff(want.splitlines(True), out.splitlines(True), fromfile='expected', tofile='got'):
                sys.stdout.write(line)
            return 3
    else:
        print('Output:')
        print(out)
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: run_tests.py <problem-dir>')
        sys.exit(1)
    raise SystemExit(run(sys.argv[1]))
