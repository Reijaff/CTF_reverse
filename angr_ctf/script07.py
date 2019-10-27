import angr
import claripy
import sys


def main(argv):
    project = angr.Project(argv)

    start_address = 0x804893C
    initial_state = project.factory.blank_state(addr=start_address)

    password = claripy.BVS('password', 64)
    password_address = 0x804A0A0
    initial_state.memory.store(password_address, password)

    sim = project.factory.simgr(initial_state)

    def is_successful(state):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return "Good Job." in stdout_output

    def should_abort(state):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return "Try again." in stdout_output

    sim.explore(find=is_successful, avoid=should_abort)

    if sim.found:
        print sim.found[0].se.eval(password, cast_to=str)
    else:
        raise Exception(" something wrong")


if __name__ == "__main__":
    main(sys.argv[1])
