import angr
import claripy

def main():
    p = angr.Project("elementary",load_options={'auto_load_libs':False})
    input_size = 128
    flag = claripy.BVS("flag",input_size*8)
    initial_state = p.factory.entry_state(args = ["./elementary"],stdin=flag)
    simgr = p.factory.simulation_manager(initial_state)
    simgr.explore(find=0x000000000000773+0x400000,avoid = 0x000000000000786+0x400000)
    some = simgr.found[0]

    import IPython;IPython.embed()
main()
