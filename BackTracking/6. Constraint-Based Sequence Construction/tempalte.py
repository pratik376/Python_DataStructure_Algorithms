def dfs(state):

    if complete:
        save_answer()
        return

    for choice in choices:

        if not valid(choice, state):
            continue

        # choose
        make_choice(choice)

        # explore
        dfs(new_state)

        # undo
        undo_choice(choice)