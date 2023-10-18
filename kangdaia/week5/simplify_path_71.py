def canonical_path(path: str) -> str:
    """
    convert absolute path to the simplified canonical path.
    canonical path format:
    - path starts with a single slash
    - any two directories are separated by a single slash
    - the path does not end with a trailing slash
    - the path only contains the directories on the path fron the root
        directory to the target file or directory
        ex) no period or double period
    " . " ==> Continue;
    " . . " ==> Remove the before directory;
    " // " ==> make it into "/"

    1. 47ms beats 17.97% of users | 16.38 MB beats 43.26%
    - replace 제거
    2. 36ms beats 82.25% of users | 16.34 MB beats 43.26%
    - path.split을 for loop에 바로 적용
    3. 35ms beats 88.10% of users | 16.13 MB beats 94.47%

    Args:
        path (str): absoulte file path (starting w/ slash "/") to a file or
                    directory in a Unix-style file system

    Returns:
        str: canonical file path
    """
    result_path = []
    for dir in path.split("/"):
        if result_path and dir == "..":
            result_path.pop()
        elif dir not in ['.', '', '..']:
            result_path.append(dir)
    return "/" + "/".join(result_path)
