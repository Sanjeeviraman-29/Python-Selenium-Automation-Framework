from utils.excel_reader import ExcelReader


def test_read_excel():

    reader = ExcelReader(
        "resources/data/LoginData.xlsx",
        "LoginData"
    )

    print("Rows:", reader.get_row_count())
    print("Columns:", reader.get_column_count())

    print(reader.get_cell_data(2, 1))
    print(reader.get_cell_data(2, 2))