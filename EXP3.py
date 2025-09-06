def transition(state, char):
    if state == 'A':
        if char == 'a':
            return 'B'
        else:
            return 'A'
    elif state == 'B':
        if char == 'a':
            return 'C'
        else:
            return 'A'
    elif state == 'C':
        if char == 'a':
            return 'D'
        else:
            return 'A'
    elif state == 'D':
        return 'D'  # Stay in accepting state
    return state

def is_accepting(state):
    return state == 'D'

def run_dfa(input_string):
    state = 'A'
    for char in input_string:
        state = transition(state, char)
    return is_accepting(state)

# Main code
input_string = input("Enter String: ")
if run_dfa(input_string):
    print(f"The string '{input_string}' is accepted (contains 3 consecutive a's).")
else:
    print(f"The string '{input_string}' is not accepted.")