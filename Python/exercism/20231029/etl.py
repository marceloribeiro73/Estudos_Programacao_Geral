def transform(legacy_data):
    result_data = {}
    for key, value in legacy_data.items():
        for item in value:
            result_data.update({item.lower(): key})
    return result_data


dc = transform({1: ["A"]})
print(dc)
