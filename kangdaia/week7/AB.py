from collections import defaultdict
def query_executor(query_list: list[str]) -> list[int]:
    """
    add/delete/find 쿼리 기능 프로그램

    Args:
        query_list (list[str]): _description_

    Returns:
        list[int]: _description_
    """
    set_dict = defaultdict(set)
    result = []
    for query in query_list:
        elem = query.split()
        if elem[0] == "add":
            name, var = elem[1:]
            set_dict[name].add(var)
        elif elem[0] == "delete":
            name, var = elem[1:]
            set_dict[name].remove(var)
        else:
            length = 1
            count = 0
            i, j = 0, len(set_dict["B"])
            ## 구현중......
            ## while length < len(elem[1]):
            ##     end_len = len(elem[1])-length
            ##     new_form = set_dict["A"][i: i+length] + set_dict["B"][j-end_len:j]
            ##     if new_form == elem[1]:
            ##         count += 1
            ##     length += 1
            result.append(count)
    return result
