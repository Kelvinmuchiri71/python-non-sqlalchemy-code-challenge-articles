class Article:
    all = []                    #Tracks all articles

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

        #Ensures articles are added to author and magazine lists

        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise Exception("Can't reassign title")
        elif isinstance(title, str) and 5 <=len(title) <=50:
            self._title = title
        else:
            raise ValueError("Title must be a string with 5 to 50 characters")
        
    @property
    def author(self):
        return self._author

    #@author.setter
    #def author(self, new_author):
    #    if isinstance(new_author, Author):
    #        self._author = new_author
    #    else:
    #        raise Exception("Author must be an instance of Author class")

    @property
    def magazine(self):
        return self._magazine

    #@magazine.setter
    #def magazine(self, new_magazine):
    #    if isinstance(new_magazine, Magazine):
    #        self._magazine = new_magazine
    #    else:
    #        raise Exception("Magazine must be an instance of Magazine class")


class Author:
    all_authors = []

    def __init__(self, name):
        self._name = name
        self._articles = []                #Ensures articles are tracked at instance level

    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Can't reassign the name")
        elif isinstance(name, str) and len(name) > 0:
            self._name = name
 
    def articles(self):
    #Returns a list of articles written by the author

        return self._articles             # Returns tracked articles

    def magazines(self):
    #Returns a unique list of magazines the author has written for

        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
    #Creates and returns a new article, ensuring proper tracking

        article = Article(self, magazine, title)
        return article

    #def topic_areas(self):
    #    categories = list(set(magazine.category for magazine in self.magazines()))
    #    return categories if categories else None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []                  #Ensures articles are tracked per magazine

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise Exception("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise Exception("Category must be a non-empty string")
   
    def articles(self):
    #Returns all articles published in this magazine

        return self._articles

    def authors(self):
    #Returns unique authors who have written for the magazine

        return list(set(article.author for article in self._articles))

    def article_titles(self):
    #Returns a list of article titles, or None if no articles exist

        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
    #Returns a list of authors who have written more than two articles
    
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None
