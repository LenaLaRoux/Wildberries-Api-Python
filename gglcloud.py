import gspread
import gspread_dataframe as gd


# gc = gspread.service_account(filename='C:/Users/LenaLaRoux/Documents/WB/Прог/wbtable-2debd38a3bfe.json')
# sh = gc.open("WbTableTest")
# ws = sh.get_worksheet(0)

class GGLExport:
    worksheet = None

    def __init__(self, table_name, worksheet_name=None):
        ggl_cloud = gspread.service_account(filename='C:/Users/LenaLaRoux/Documents/WB/Прог/wbtable-2debd38a3bfe.json')
        spread_sheet = ggl_cloud.open(table_name)
        if worksheet_name is None:
            self.worksheet = spread_sheet.get_worksheet(0)
        else:
            self.worksheet = spread_sheet.worksheet(worksheet_name)

    def export_to_sheets(self, df, mode='r'):
        # write
        if (mode == 'w'):
            self.worksheet.clear()
            self.worksheet.update([df.columns.values.tolist()] + df.values.tolist())
            return True
        # append
        elif (mode == 'a'):
            self.worksheet.append_rows(df.values.tolist())
            return True
        else:
            return gd.get_as_dataframe(worksheet=self.worksheet)
