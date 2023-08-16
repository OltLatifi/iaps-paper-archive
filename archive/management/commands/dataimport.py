from django.core.management.base import BaseCommand
from archive.models import Paper, Author, Category
import json

class Command(BaseCommand):
    filename = "sample-data.json"
    help = "This command loads data from json to the database"

    def generate_flat_author_list(self, author_list: list) -> list:
        """ 
        Input: Matrix of authors first name and last name
        Output: Flat list of authors full name
        """
        if not author_list:
            return []
        
        author_flat_list = []
        for author in author_list:
            author_flat_list.append(f"{author[1]} {author[0]}")
        return author_flat_list
    
    def insert_author(self, name: str) -> Author:
        """
        Gets an existing author or creates a new one
        """
        try:
            author = Author.objects.get(name=name)
        except Author.DoesNotExist:
            author = Author(name=name)
            author.save()
        return author
    
    def insert_category(self, name: str) -> Category:
        """
        Gets an existing category or creates a new one
        """
        try:
            category = Category.objects.get(name=name)
        except Category.DoesNotExist:
            category = Category(name=name)
            category.save()
        return category
    
    def get_first_version_publication_date(self, versions: list[dict]) -> str:
        """
        Returns the first publication date of the paper
        """
        return versions[0].get("created")
    
    def insert_paper(self, data: dict, authors: list[Author], categories: list[Category]) -> Paper:
        """
        Inserts paper and assign m2m fields
        """
        original_id = data.get("id")
        title = data.get("title")
        abstract = data.get("abstract")
        publication_date = self.get_first_version_publication_date(data.get("versions"))

        try:
            paper = Paper.objects.get(id=original_id)
        except Paper.DoesNotExist:
            paper = Paper(id=original_id, title=title, abstract=abstract, publication_date=publication_date)
            paper.save()

            for author in authors:
                paper.authors.add(author)
            for category in categories:
                paper.categories.add(category)

    def handle(self, *args, **options):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = json.loads(line)

                    """
                    the m2m entities refrenced in this json line
                    so we don't look them up again for the paper
                    """
                    line_authors: list[Author] = []
                    line_categories: list[Category] = []
                    
                    author_list = self.generate_flat_author_list(data.get("authors_parsed"))
                    for author in author_list:
                        line_authors.append(self.insert_author(author))

                    categories_list = data.get("categories").split(" ")
                    for category in categories_list:
                        line_categories.append(self.insert_category(category))
                    
                    self.insert_paper(data, line_authors, line_categories)

        except FileNotFoundError:
            print("The file could not be found.")
