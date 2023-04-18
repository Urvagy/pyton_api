from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/view")
def view():
    con = sqlite3.connect("hambi.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Hambi")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        nev = data["nev"]
        husi = data["husi"]
        suly = data["suly"]
        ar = data["ar"]
        daarabszam = data["daarabszam"]
        with sqlite3.connect("hambi.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into Hambi (nev, husi, suly, ar, daarabszam) values (?,?,?,?,?)", (nev, husi, suly, ar, daarabszam))
            con.commit()
            msg = "Hambi hozzáadva"
    except:
        con.rollback()
        msg = "Nem tudjuk hozzáadni a hambit a listához"
    finally:
        return nev
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("hambi.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Hambi where id = ?", id)
            msg = "Sikeres törlés"
        except:
            msg = "Nem lehet törölni"

@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["id"]
        nev = data["nev"]
        husi = data["husi"]
        suly = data["suly"]
        ar = data["ar"]
        daarabszam = data["daarabszam"]

        with sqlite3.connect("hambi.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE Hambi SET nev=?, husi=?, suly=?, ar=?, daarabszam=? WHERE id=?", (nev, husi, suly,ar, daarabszam, id))
            con.commit()
            msg = "A hambit sikeresen hozzáadtad az adatbázishoz"
    except:
        con.rollback()
        msg = "Nem lehet frissiteni a hambit a listában"
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)
