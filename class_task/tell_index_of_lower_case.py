def lowe_case_index(word) -> list:
    _lst = []
    for index in range(len(word)):
        if word[index].islower():
            _lst.append(index)
    return _lst


print(lowe_case_index("reTNAa"))
