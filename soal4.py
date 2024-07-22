class DataList:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self, index):
        if index < len(self.data):
            return self.data[index]
        else:
            return None

    def get_all_data(self):
        return self.data

    def remove_data(self, index):
        if index < len(self.data):
            del self.data[index]

    def __str__(self):
        return str(self.data)

my_list = DataList()
my_list.add_data("irma")
print("All data:", my_list.get_all_data())
print("Data at index 1:", my_list.get_data(1))
my_list.remove_data(1)
print("Updated list:", my_list.get_all_data())
print("Data at index 1:", my_list.get_data(1))