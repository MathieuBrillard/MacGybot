def checkTimeFormat(time: str) -> bool:
    """This function is used to check if the time string passed in argument
    is from the correct format (mm:ss or ss).

    Args:
        `time`(str): The time to check.

    Returns:
        `bool`: True if the format is correct, false if not.
    """
    correct_format = True
    if time.find(":") == -1:
        if time.isnumeric() == False:
            correct_format = False
    else:
        min = time.split(":")[0]
        sec = time.split(":")[1]
        if min.isnumeric() == False:
            correct_format = False
        if sec.isnumeric() == False:
            correct_format = False
    return correct_format
