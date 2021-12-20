from django.shortcuts import render

# Create your views here.
from webapp_cows_and_bulls.check import Check

SECRET_NUMBERS = Check.generate_numbers(4)
ANSWERS = []
OPTIONS = []
context = {
        'options': OPTIONS,
        'answers': ANSWERS,
        'win': 0,
        'secret_nums': Check.generate_numbers(4),
    }


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        context['numbers'] = list(map(int, request.POST.get('numbers').split()))
        try:
            check = Check(context['numbers'], context['secret_nums'])
            error = check.validation()
            if error:
                context['massage'] = error
                return render(request, 'index.html', context)
            else:
                result = check.get_result()
                if result == "Win":
                    context['win'] += 1
                    context['secret_nums'] = Check.generate_numbers(4)
                context['massage'] = result
                OPTIONS.append(request.POST.get('numbers'))
                ANSWERS.append(context['massage'])
                return render(request, 'index.html', context)
        except ValueError:
            context['massage'] = 'Value should be integers'
            return render(request, 'index.html', context)


def log_view(request):
    return render(request, 'result.html', context)
