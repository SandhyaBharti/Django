{% comment %} <!DOCTYPE html>
<html>
<head>
    <title>Student Table</title>
</head>

<body>

    <h1>Student Information</h1>

    <table border="1" cellpadding="10">

        <tr>
            <th>Roll No</th>
            <th>Name</th>
            <th>Course</th>
            <th>CGPA</th>
        </tr>

        {% for student in students %}
        <tr>
            <td>{{ student.roll }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.course }}</td>
            <td>{{ student.cgpa }}</td>
        </tr>
        {% endfor %}

    </table>

</body>
</html> {% endcomment %}




<!DOCTYPE html>
<html>
<head>
    <title>Student Information</title>
</head>

<body>

    <h1>Student Information</h1>

    <p>Name: {{ name }}</p>
    <p>Age: {{ age }}</p>
    <p>Course: {{ course }}</p>
    <p>College: {{ college }}</p>
    <p>CGPA: {{ cgpa }}</p>

</body>
</html>