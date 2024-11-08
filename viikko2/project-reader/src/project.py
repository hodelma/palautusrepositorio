class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors
    
    def _stringify_(self, authors):
        return "\n - ".join(authors) if len(authors) > 0 else "-"
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: \n - {self._stringify_(self.authors)}"
            f"\n\nDependencies: \n - {self._stringify_(self.dependencies)}"
            f"\n\nDevelopment dependencies: \n - {self._stringify_(self.dev_dependencies)}"
        )
