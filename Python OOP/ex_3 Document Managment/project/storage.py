class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        filtered = [c for c in self.categories if c.id == category_id][0]
        filtered.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        filtered = [t for t in self.topics if t.id == topic_id][0]
        filtered.topic = new_topic
        filtered.storage_folder = new_storage_folder

    def delete_document(self, document_id):
        filtered = [d for d in self.documents if d.id == document_id][0]
        if filtered:
            self.documents.remove(filtered)

    def edit_document(self, document_id: int, new_file_name: str):
        filtered = [d for d in self.documents if d.id == document_id][0]
        filtered.file_name = new_file_name

    def delete_category(self, category_id):
        filtered = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(filtered)

    def delete_topic(self, topic_id):
        filtered = [t for t in self.topics if t.id == topic_id][0]
        if filtered:
            self.topics.remove(filtered)

    def get_document(self, document_id):
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self):
        result = ""
        for x in self.documents:
            result += "".join(str(x))
        return result

from project.category import Category
from project.document import Document
# from project.storage import Storage
from project.topic import Topic
c1 = Category(1, 'work')
t1 = Topic(1, 'daily tasks', 'C:\\work_documents')
d1 = Document(1, 1, 1, 'finilize project')
d1.add_tag('urgent')
d1.add_tag('work')
storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)
print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
