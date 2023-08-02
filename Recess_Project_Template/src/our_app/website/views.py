from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from .forms import InstructorForm
from .models import InstructorFeedback
from .models import StudentDetails
from django.shortcuts import render, redirect, get_object_or_404


def course(request):
    return render(request, 'course.html')


def facility(request):
    return render(request, 'facility.html')


def instructor(request):
    return render(request, 'instructor.html')


def dashboard(request):
    students = StudentDetails.objects.all()
    return render(request, 'dashboard/pages/dashboard.html', {'students': students})


def courses(request):
    return render(request, 'dashboard/pages/courses.html')


def facilities(request):
    return render(request, 'dashboard/pages/facilities.html')


def instructors(request):
    feedbacks = InstructorFeedback.objects.all()
    return render(request, 'dashboard/pages/instructors.html', {'feedbacks': feedbacks})


def delete_instructor_feedback(request, feedback_id):
    feedback = get_object_or_404(InstructorFeedback, id=feedback_id)
    if request.method == 'POST':
        feedback.delete()
        return redirect('instructors')
    return render(request, 'dashboard/pages/delete_instructor_feedback.html', {'feedback': feedback})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/pages/profile.html')
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('sign_in')


def signout(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/pages/dashboard.html')
    else:
        # Check to see if logging in
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('dashboard')
            else:
                messages.success(request, "There Was An Error Logging In, Please Try Again...")
                return redirect('home')
        else:
            return render(request, 'dashboard/pages/sign_in.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('dashboard')
    else:
        form = SignUpForm()
        return render(request, 'dashboard/pages/sign_up.html', {'form': form})

    return render(request, 'dashboard/pages/sign_up.html', {'form': form})


def instructor_feedback(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_data = form.cleaned_data
            feedback = InstructorFeedback(
                instructorName=form_data['instructorName'],
                department=form_data['department'],
                courseUnit=form_data['courseUnit'],
                knowledge=form_data['knowledge'],
                communication=form_data['communication'],
                teachingStyle=form_data['teachingStyle'],
                responsiveness=form_data['responsiveness'],
                additional_comments=form_data['additional_comments']
            )
            feedback.save()

            return redirect('home')  # Redirect to a success page after successful form submission
    else:
        form = InstructorForm()

    return render(request, 'instructor.html', {'form': form})


def studentDetails(request):
    if request.method == 'POST':
        name = request.POST['name']
        studentId = request.POST['studentId']
        emailAddress = request.POST['emailAddress']
        year_of_study = request.POST['year_of_study']

        # Save data to the database
        StudentDetails.objects.create(name=name, studentId=studentId, emailAddress=emailAddress,
                                      year_of_study=year_of_study)

        # Set a success message to display on the index.html template
        success_message = "Thank you for signing up!"

    else:
        # No success message when the form is first loaded
        success_message = None

    return render(request, 'index.html', {'success_message': success_message})
