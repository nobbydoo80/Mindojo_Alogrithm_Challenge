from django.http import JsonResponse
from .utils import get_google_sheet, count_cells_with_flow_to_oceans
from django.shortcuts import render

def calculate_flow(request):
    sheet = get_google_sheet()
    tab_name = request.GET.get('tab', 'case 1')  # Default to 'Sheet1' if no tab specified
    worksheet = sheet.worksheet(tab_name)
    sheet_data = worksheet.get_all_values()
    sheet_data = [[int(cell) for cell in row] for row in sheet_data]
    result = count_cells_with_flow_to_oceans(sheet_data)
    return JsonResponse({
        "result": result,
        "tab": tab_name,
        "sheet_data": sheet_data  # Include the raw sheet data in the response
    })

def index(request):
    return render(request, 'analysis/index.html')

