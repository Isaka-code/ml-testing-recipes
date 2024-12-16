from src.data_processing import convert_data


def test_convert_data_type():
    input_data = (1, 2, 3)
    output = convert_data(input_data)
    assert isinstance(output, list), "返り値がlistではありません"
    assert output == [1, 2, 3], "変換結果が期待と異なります"
