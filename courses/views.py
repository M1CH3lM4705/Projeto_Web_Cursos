from django.shortcuts import render, get_object_or_404
from courses.models import Course
from .forms import ContacCourse

# Create your views here.
def index(request):#função que traz todos os objetos tabela cursos
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses':courses
    }
    return render(request, template_name, context)

def detalhe(request, slug):#funçao para trazer os detalhes dos cursos
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContacCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            #form.cleaned_data['name'] acessa o objeto no formulario
            form.send_mail(course)
            form = ContacCourse()
    else:
        form = ContacCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/detalhes.html'
    return render(request, template_name, context)

