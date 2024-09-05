import openpyxl


def get_list_from_exel():
    workbook = openpyxl.load_workbook("credentials main.xlsx")
    login_creds = workbook["login_creds"]
    credentials_list = []
    for row in range(1, 7):
        nested_creds = []
        for column in range(1, 3):
            data = login_creds.cell(row, column)
            nested_creds.append(data.value)
        credentials_list.append(nested_creds)
    return credentials_list
