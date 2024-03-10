# titanic

VIDEO DEMO LINK: https://youtu.be/HIa8i2dJIHw

1) Open pgAdmin 4
2) Create a database called a3_q1
3) Using the Query Tool, run the below SQL statement to create the db table:

```
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);
```

4) Using the Query Tool, run the below SQL statement (provided in the question) to populate the table:

```
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

5) In command prompt (on Windows), run "pip install psycopg2"

6) Comment out the functions that you don't want to be run in the "if __name__ == "__main__":" block.

7) In command prompt (on Windows), run "python a3q1.py"
