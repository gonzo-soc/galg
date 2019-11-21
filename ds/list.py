#! /usr/bin/env python3.7

from sys import argv

TAIL_LIST = None
HEAD_LIST = None


def get_tail():
    global TAIL_LIST
    global HEAD_LIST

    # debug_prefix = f"Debug [ {getTail_LIST_GALG.__name__} ] "
    if not TAIL_LIST:
        TAIL_LIST = {
            'data': None,
            'next': None
        }
        HEAD_LIST = TAIL_LIST
    return TAIL_LIST


def get_head():
    return HEAD_LIST


def set_tail(in_cur):
    debug_prefix = f"Debug [ {set_tail.__name__} ] "
    global TAIL_LIST
    if not in_cur:
        print(debug_prefix + " Error: invalid cursor has been passed \n")
        return False
    TAIL_LIST = in_cur
    return True


def set_head(in_cur):
    debug_prefix = f"Debug [ {set_head.__name__} ] "
    global HEAD_LIST
    if not in_cur:
        print(debug_prefix + " Error: invalid cursor has been passed \n")
        return False
    HEAD_LIST = in_cur
    return True


def add(in_data):
    '''
    Add a node to the list
    '''
    debug_prefix = f"Debug [ {add.__name__} ] "
    if not in_data:
        print(debug_prefix + " Error: invalid data has been passed \n")
        return False

    empty_node = {
        'data': None,
        'next': None
    }
    cur = get_tail()

    cur['data'] = in_data
    cur['next'] = empty_node
    set_tail(in_cur=cur['next'])

    print(
        debug_prefix
        + f'''
Info: cur {cur} head {get_head()} tail {get_tail()}
            '''
        )
    return True


def is_list_empty():
    tail = get_tail()
    head = get_head()
    return head == tail and not head['data']


def remove(rm_data):
    '''
    Remove a node from the list
    '''
    debug_prefix = f"Debug [ {remove.__name__} ] "
    if not rm_data:
        print(debug_prefix + " Error: invalid data has been passed \n")
        return False
    if is_list_empty():
        print(debug_prefix + "Info: the list is EMPTY\n")
        return True

    cur = get_head()
    prev = cur
    while cur:
        if cur['data'] == rm_data:
            if cur == get_head():
                set_head(cur['next'])
            prev['next'] = cur['next']
            cur['data'] = None
            cur = None
            print(debug_prefix + f"Info: head {get_head()} \n")
            break
        else:
            prev = cur
            cur = cur['next']
    if not prev['next']:
        set_tail(prev)

    return True


def print():
    '''
    Print the list
    '''
    debug_prefix = f"Debug [ {print_LIST_GALG.__name__} ] "
    print(debug_prefix + "Info: print the list\n" + '-' * 80 + "\n")
    cur = get_head()
    if not cur['data']:
        print(debug_prefix + " Info: EMPTY list\n")
    else:
        i = 0
        while cur['data']:
            print(
                debug_prefix +
                f'''
Info: Node # {i} has the following appended data: {cur['data']}
                '''
            )
            cur = cur['next']
            i += 1

    return True


def main(args):
    '''
    Print the list
    '''
    add("orange")
    add("apple")
    add("pineapple")
    remove("orange")
    remove("apple")
    add("tomato")
    add("blackberry")
    print()
    remove("tomato")
    print()
    remove("pineapple")
    print()
    remove("blackberry")
    print()
    remove("blackberry")
    return True


if __name__ == "__main__":
    main(argv)
