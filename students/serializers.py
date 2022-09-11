from rest_framework import serializers
from .models import Student, School, Book

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ('__all__')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('__all__')

class StudentSerializer(serializers.ModelSerializer):
    student_full_name = serializers.ReadOnlyField()
    student_email = serializers.CharField(max_length=200,source='email')
    gender = serializers.CharField(max_length=200)
    school_name = serializers.ReadOnlyField()
    school_phone = serializers.ReadOnlyField()
    books_read = serializers.ReadOnlyField()
    book_pages_read = serializers.ReadOnlyField()


    class Meta:
        model = Student
        fields = ('student_full_name','student_email','gender','school_name','school_phone','books_read','book_pages_read')