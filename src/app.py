from flask import Flask, jsonify, request
from datastructures import FamilyStructure

app = Flask(__name__)
family = FamilyStructure("Jackson")

@app.route('/member', methods=['POST'])
def add_member():
    member_data = request.json
    family.add_member(member_data)
    return jsonify({"message": "El miembro se agregó correctamente"}), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    family.delete_member(id)
    return jsonify({"done": True}), 200

@app.route('/members', methods=['GET'])
def get_all_members():
    members = family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = family.get_member(id)
    if member:
        corrected_member = {
            "first_name": member['first_name'],
            "id": member["id"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        return jsonify(corrected_member), 200
    else:
        return jsonify({"message": "Miembro no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
