from flask import Flask, request, jsonify

app = Flask(__name__)

notes = {
    1: "Learn Flask",
    2: "Study HTTP methods"
}


@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)


@app.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    new_id = max(notes.keys()) + 1
    notes[new_id] = data['note']
    return jsonify({new_id: notes[new_id]}), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.json
    if note_id in notes:
        notes[note_id] = data['note']
        return jsonify({note_id: notes[note_id]})
    return jsonify({"error": "Note not found"}), 404

@app.route('/notes/<int:note_id>', methods=['PATCH'])
def patch_note(note_id):
    data = request.json
    if note_id in notes:
        notes[note_id] = data.get('note', notes[note_id])
        return jsonify({note_id: notes[note_id]})
    return jsonify({"error": "Note not found"}), 404


@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    if note_id in notes:
        deleted = notes.pop(note_id)
        return jsonify({"deleted": deleted})
    return jsonify({"error": "Note not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
