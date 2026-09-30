def dfs(...):

    for candidate in candidates:

        if candidate already conflicts:
            continue

        create_mapping()

        if dfs(...):
            return True

        remove_mapping()

    return False