from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            },
        ]
        self._next_id = len(self._members) + 1

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member['last_name'] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member['id'] == id:
                del self._members[i]
                break

    def update_member(self, id, new_member_data):
        for member in self._members:
            if member['id'] == id:
                for key, value in new_member_data.items():
                    member[key] = value
                break

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                member['name'] = f"{member['first_name']} {member['last_name']}"
                return member
        return None

    def get_all_members(self):
        return self._members
