class Container:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, key, value):
        self.tags[key] = value

    def __len__(self):
        return len(self.tags)


container = Container()
container.add('Python')
container.add('python')
container.add('python')

container['javascript'] = 10


print(container.tags)
print(container['python'])
print(len(container))
