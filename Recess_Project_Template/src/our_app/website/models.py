from django.db import models


class InstructorFeedback(models.Model):
    instructorName = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    courseUnit = models.CharField(max_length=100)
    knowledge = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    communication = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    teachingStyle = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    responsiveness = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    additional_comments = models.TextField()

    def __str__(self):
        return f"Feedback by {self.instructorName}"


class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseCode = models.CharField(max_length=100)
    courseDescription = models.CharField(max_length=1000)
    effectiveness = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    interest = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    improvement = models.TextField()