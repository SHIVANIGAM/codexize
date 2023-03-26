from flask import Flask, jsonify

app = Flask(__name__)

banks = [
    {
        "bank_id": 1,
        "bank_name": "ABC Bank"
    },
    {
        "bank_id": 2,
        "bank_name": "XYZ Bank"
    }
]

branches = [
    {
        "branch_id": 1,
        "branch_name": "ABC Bank - Branch 1",
        "bank_id": 1,
        "location": "New York"
    },
    {
        "branch_id": 2,
        "branch_name": "ABC Bank - Branch 2",
        "bank_id": 1,
        "location": "Chicago"
    },
    {
        "branch_id": 3,
        "branch_name": "XYZ Bank - Branch 1",
        "bank_id": 2,
        "location": "San Francisco"
    }
]

@app.route("/banks", methods=["GET"])
def get_bank_list():
    return jsonify(banks)

@app.route("/branches/<int:branch_id>", methods=["GET"])
def get_branch_details(branch_id):
    branch = next((b for b in branches if b["branch_id"] == branch_id), None)
    if branch:
        bank = next((b for b in banks if b["bank_id"] == branch["bank_id"]), None)
        return jsonify({"branch": branch, "bank": bank})
    else:
        return jsonify({"message": "Branch not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
