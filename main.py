import gglcloud as cloud
import wbreport as wb

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_wb_service():

    wb_tool = wb.WBExtract('https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod',
                        'ZTkwNDM4ODgtYjEzZi00MDJiLWJkMzktZjE1OTg2MmNlNTY5',
                           150)
    worksheet = cloud.GGLExport("WbTableTest")
    wb_tool.open_session()

    mode = 'w'
    while wb_tool.has_more_data():
        batch = wb_tool.read_data()
        worksheet.export_to_sheets(batch, mode)
        mode = 'a'

    wb_tool.close_session()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    read_wb_service()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
