def query_executor(query_list: list[str]) -> list[int]:
    """
    add/delete/find 쿼리 기능 프로그램

    Args:
        query_list (list[str]): _description_

    Returns:
        list[int]: _description_
    """
    set_dict = dict()
    for query in query_list:
        op, name, var = query.split()
        if op == "add":
            set_dict.get(name, set()).update(set(var))
        elif op == "delete":
            set_dict[name] = set_dict.get(name, set()) - set(var)
        else:
            expect = len(var)
            i, j = 0, len(set_dict["B"])-1
            
            

    return [0]
