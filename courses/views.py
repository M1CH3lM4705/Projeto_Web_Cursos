from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Enrollment
from .forms import ContacCourse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
    #    enrollment.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso.')
    else:
        messages.info(request, 'Você já está inscrito no curso.')
    return redirect('accounts:dashboard')

