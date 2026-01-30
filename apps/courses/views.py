from django.shortcuts import render
from .models.course import Course

# Create your views here.

def course_list(request):

    courses = Course.objects.all()

    return render(request, "courses/courses.html", {
        'courses': courses
    })

def course_detail(request):
    course = {
        'course_title': 'Django Aplicaciones',
        'course_link': 'course_lessons',
        'course_image': 'images/curso_2.jpg',
        'info_course': {
            'lessons': 79,
            'duration': 8,
            'instructor': 'Ricardo Cuellar'
        },
        'course_content':[
            {
                'id': 1,
                'name': 'Introducción al curso',
                'lessons': [
                    {
                        'name': '¿Que aprenderás en el curso?',
                        'type': 'video'
                    },
                    {
                        'name': '¿Como usar la plataforma?',
                        'type': 'article'
                    },

                ]
            }
        ]  
    }
    return render(request, 'courses/course_detail.html',{
        'course': course
    })

def course_lessons(request):
    lesson = {
        'course_title': 'Django Aplicaciones',
        'course_progress': 30,
        'course_content':[
            {
                'id': 1,
                'name': 'Introducción al curso',
                'total_lessons': 6,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': '¿Que aprenderás en el curso?',
                        'type': 'video'
                    },
                    {
                        'name': '¿Como usar la plataforma?',
                        'type': 'article'
                    },
                ]
            },
            {
                'id': 2,
                'name': 'Django principios',
                'total_lessons': 12,
                'complete_lessons': 2,
                'lessons': [
                    {
                        'name': '¿Que aprenderás en el curso?',
                        'type': 'video'
                    },
                    {
                        'name': '¿Como usar la plataforma?',
                        'type': 'article'
                    },
                ]
            },
        ]  
    }
    return render(request, 'courses/course_lessons.html', {
        'lesson': lesson
    })