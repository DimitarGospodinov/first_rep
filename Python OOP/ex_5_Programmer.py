class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if self.language != new_language:
            if self.skills >= skills_needed:
                text = f"{self.name} switched from {self.language} to {new_language}"
                self.language = new_language
                return text
            return f"{self.name} needs {abs(skills_needed - self.skills)} more skills"

        else:
            return f"{self.name} already knows {new_language}"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        programmer = Programmer("Lemmy", "Python", 100)
        self.assertEqual(programmer.name, "Lemmy")
        self.assertEqual(programmer.language, "Python")
        self.assertEqual(programmer.skills, 100)

    def test_watch_course_successfull(self):
        programmer = Programmer("Lemmy", "Python", 100)
        res = programmer.watch_course("Django Fundamentals", "Python", 50)
        self.assertEqual(res, "Lemmy watched Django Fundamentals")
        self.assertEqual(programmer.skills, 150)

    def test_watch_course_unsuccessfull(self):
        programmer = Programmer("Lemmy", "Python", 100)
        res = programmer.watch_course("Best C#", "C#", 20)
        self.assertEqual(res, "Lemmy does not know C#")
        self.assertEqual(programmer.skills, 100)

    def test_change_language_unsuccessful(self):
        programmer = Programmer("Lemmy", "Java", 100)
        res = programmer.change_language("Python", 150)
        self.assertEqual(res, "Lemmy needs 50 more skills")
        self.assertEqual(programmer.language, "Java")

    def test_change_language_successful(self):
        programmer = Programmer("Lemmy", "Java", 100)
        res = programmer.change_language("Python", 50)
        self.assertEqual(res, "Lemmy switched from Java to Python")
        self.assertEqual(programmer.language, "Python")

    def test_change_language_same_language(self):
        programmer = Programmer("Lemmy", "Python", 100)
        res = programmer.change_language("Python", 50)
        self.assertEqual(res, "Lemmy already knows Python")
        self.assertEqual(programmer.language, "Python")


if __name__ == "__main__":
    unittest.main()