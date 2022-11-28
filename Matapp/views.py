from django.shortcuts import HttpResponse
from Matapp.funcs import transpose

def main(request):
    cols = request.GET.get("cols")  #ввод кол-ва столбцов
    rows = request.GET.get("rows")  #ввод кол-ва строк
    args = request.GET.get("args")  #ввод значений
    t = transpose(cols=cols, rows=rows, args=args)
    return HttpResponse(f"Транспонированная матрица {t}")  # ввывод матрицы