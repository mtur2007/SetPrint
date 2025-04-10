import numpy as np

def update_numpy_scalars_and_get_depth(obj):
    if isinstance(obj, np.generic):
        return obj.item(), 0

    if isinstance(obj, np.ndarray):
        if obj.ndim == 0:
            return obj.item(), 0
        if obj.dtype != np.object_:
            return obj, obj.ndim
        else:
            new_obj = obj.copy()
            max_sub_depth = 0
            for idx, value in np.ndenumerate(new_obj):
                updated_val, sub_depth = update_numpy_scalars_and_get_depth(value)
                new_obj[idx] = updated_val
                if sub_depth > max_sub_depth:
                    max_sub_depth = sub_depth
            return new_obj, 1 + max_sub_depth if new_obj.size > 0 else 1

    if isinstance(obj, dict):
        if not obj:
            return obj, 1
        new_dict = {}
        max_sub_depth = 0
        for key, value in obj.items():
            updated_val, sub_depth = update_numpy_scalars_and_get_depth(value)
            new_dict[key] = updated_val
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return new_dict, 1 + max_sub_depth

    if isinstance(obj, list):
        if not obj:
            return obj, 1
        new_list = []
        max_sub_depth = 0
        for item in obj:
            updated_item, sub_depth = update_numpy_scalars_and_get_depth(item)
            new_list.append(updated_item)
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return new_list, 1 + max_sub_depth

    if isinstance(obj, tuple):
        if not obj:
            return obj, 1
        new_tuple = []
        max_sub_depth = 0
        for item in obj:
            updated_item, sub_depth = update_numpy_scalars_and_get_depth(item)
            new_tuple.append(updated_item)
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return tuple(new_tuple), 1 + max_sub_depth

    return obj, 0


# テストケース
test_cases = [
    (np.int32(5), 5, 0),
    (np.float64(3.14), 3.14, 0),
    (np.array(7), 7, 0),
    (np.array([[1, 2], [3, 4]]), np.array([[1, 2], [3, 4]]), 2),
    (np.array([[np.int64(1), 2], [3, 4]], dtype=object), [[1, 2], [3, 4]], 2),
    ([1, 2, [3, 4]], [1, 2, [3, 4]], 3),
    ({'a': 1, 'b': {'c': np.float64(2.2)}}, {'a': 1, 'b': {'c': 2.2}}, 3),
    ((1, (2, (3,))), (1, (2, (3,))), 3),
    ([], [], 1),
    ({}, {}, 1),
    ((), (), 1),
]

# 実行
def run_tests():
    for i, (input_val, expected_val, expected_depth) in enumerate(test_cases, 1):
        updated, depth = update_numpy_scalars_and_get_depth(input_val)
        print(f"Test {i}:")
        print(f"  Input:         {input_val}")
        print(f"  Updated:       {updated}")
        print(f"  Expected Val:  {expected_val}")
        print(f"  Depth:         {depth}")
        print(f"  Expected Depth:{expected_depth}")
        
        if isinstance(updated, np.ndarray) and isinstance(expected_val, (np.ndarray, list)):
            # NumPy配列同士 または listとの比較（期待値が list の場合も許容）
            passed = np.array_equal(updated, np.array(expected_val)) and depth == expected_depth
        else:
            passed = updated == expected_val and depth == expected_depth

        print(f"  {'✔️ PASS' if passed else '❌ FAIL'}")
        print("-" * 60)

if __name__ == "__main__":
    run_tests()
