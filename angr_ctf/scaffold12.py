# When you construct a simulation manager, you will want to enable Veritesting:
# project.factory.simgr(initial_state, veritesting=True)
# Hint: use one of the first few levels' solutions as a reference.
import angr
import claripy
import sys


def main(argv):
    project = angr.Project(argv)

    initial_state = project.factory.entry_state()

    simulation = project.factory.simgr(initial_state, veritesting=True)

    def is_successful(state):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return 'Good Job.' in stdout_output  # :boolean

    def should_abort(state):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return 'Try again.' in stdout_output  # :boolean

    simulation.explore(find=is_successful, avoid=should_abort)

    if simulation.found:
        solution_state = simulation.found[0]
        print solution_state.posix.dumps(sys.stdin.fileno())
    else:
        raise Exception('Could not find the solution')


if __name__ == "__main__":
    main(sys.argv[1])
