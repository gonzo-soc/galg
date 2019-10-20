#! /usr/bin/env python3.7

from sys import argv

TAIL_LIST_GALG = None
HEAD_LIST_GALG = None


def getTail_LIST_GALG():
    global TAIL_LIST_GALG
    global HEAD_LIST_GALG

    # debug_prefix = f"Debug [ {getTail_LIST_GALG.__name__} ] "
    if not TAIL_LIST_GALG:
        TAIL_LIST_GALG = {
            'data': None,
            'next': None
        }
        HEAD_LIST_GALG = TAIL_LIST_GALG
    return TAIL_LIST_GALG


def getHead_LIST_GALG():
    return HEAD_LIST_GALG


def setTail_LIST_GALG(in_cur):
    debug_prefix = f"Debug [ {setTail_LIST_GALG.__name__} ] "
    global TAIL_LIST_GALG
    if not in_cur:
        print(debug_prefix + " Error: invalid cursor has been passed \n")
        return False
    TAIL_LIST_GALG = in_cur
    return True


def setHead_LIST_GALG(in_cur):
    debug_prefix = f"Debug [ {setHead_LIST_GALG.__name__} ] "
    global HEAD_LIST_GALG
    if not in_cur:
        print(debug_prefix + " Error: invalid cursor has been passed \n")
        return False
    HEAD_LIST_GALG = in_cur
    return True


def add_LIST_GALG(in_data):
    '''
    Add a node to the list
    '''
    debug_prefix = f"Debug [ {add_LIST_GALG.__name__} ] "
    if not in_data:
        print(debug_prefix + " Error: invalid data has been passed \n")
        return False

    empty_node = {
        'data': None,
        'next': None
    }
    cur = getTail_LIST_GALG()

    cur['data'] = in_data
    cur['next'] = empty_node
    setTail_LIST_GALG(in_cur=cur['next'])

    print(
        debug_prefix
        + f'''
Info: cur {cur} head {getHead_LIST_GALG()} tail {getTail_LIST_GALG()}
            '''
        )
    return True


def isListEmpty():
    tail = getTail_LIST_GALG()
    head = getHead_LIST_GALG()
    return head == tail and not head['data']


def remove_LIST_GALG(rm_data):
    '''
    Remove a node from the list
    '''
    debug_prefix = f"Debug [ {remove_LIST_GALG.__name__} ] "
    if not rm_data:
        print(debug_prefix + " Error: invalid data has been passed \n")
        return False
    if isListEmpty():
        print(debug_prefix + "Info: the list is EMPTY\n")
        return True

    cur = getHead_LIST_GALG()
    prev = cur
    while cur:
        if cur['data'] == rm_data:
            if cur == getHead_LIST_GALG():
                setHead_LIST_GALG(cur['next'])
            prev['next'] = cur['next']
            cur['data'] = None
            cur = None
            print(debug_prefix + f"Info: head {getHead_LIST_GALG()} \n")
            break
        else:
            prev = cur
            cur = cur['next']
    if not prev['next']:
        setTail_LIST_GALG(prev)

    return True


def print_LIST_GALG():
    '''
    Print the list
    '''
    debug_prefix = f"Debug [ {print_LIST_GALG.__name__} ] "
    print(debug_prefix + "Info: print the list\n" + '-' * 80 + "\n")
    cur = getHead_LIST_GALG()
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


def main_LIST_GALG(args):
    '''
    Print the list
    '''
    add_LIST_GALG("orange")
    add_LIST_GALG("apple")
    add_LIST_GALG("pineapple")
    remove_LIST_GALG("orange")
    remove_LIST_GALG("apple")
    add_LIST_GALG("tomato")
    add_LIST_GALG("blackberry")
    print_LIST_GALG()
    remove_LIST_GALG("tomato")
    print_LIST_GALG()
    remove_LIST_GALG("pineapple")
    print_LIST_GALG()
    remove_LIST_GALG("blackberry")
    print_LIST_GALG()
    remove_LIST_GALG("blackberry")
    return True


main_LIST_GALG(argv)
