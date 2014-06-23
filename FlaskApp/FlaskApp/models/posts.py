from sqlobject import SQLObject, StringCol


class Post(SQLObject):

    author = StringCol()
    content = StringCol()
    title = StringCol()
    date = StringCol()


    def to_dict(self):
        return {
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date
        }





