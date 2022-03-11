async def safe_pop(array: list, index: int):
    if index >= len(array):
        return array
    else:
        res = array.pop(index)
        if res == "":
            return None
        return res


async def safe_get(array: list, index: int):
    if array is None:
        return None
    if index >= len(array):
        return None
    else:
        return array[index]


async def safe_get_dict(array: dict, key: str):
    if type(array) == dict:
        return array.get(key)
    else:
        return None


def columns_to_pydantic(result, model):
    dict_ = {}
    for key in result.__mapper__.c.keys():
        dict_[key] = getattr(result, key)

    return model(**dict_)