class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return f"{self.name}"

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return f"{self.due_date}"

    def add_comment(self, comment: str):
        self.comments.append(comment)
        return comment

    def edit_comment(self, comment_number: int, new_comment: str):
        if len(self.comments) > comment_number:
            self.comments[comment_number] = new_comment
            result = ""
            result += f'{", ".join([x for x in self.comments])}'
            return result
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"



