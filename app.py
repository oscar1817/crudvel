from flask import Flask, jsonify, request, send_file
import mysql.connector
import xlsxwriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="",
    database="clientes_db"
)
cursor = db.cursor()

# ruta para obtener clientes
@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return jsonify(clientes)

# ruta para agregar clientes
@app.route('/clientes', methods=['POST'])
def agregar_cliente():
    datos = request.json
    query = """INSERT INTO clientes 
               (nombre, apellido, tipo_documento, numero_documento, ciudad, direccion, telefono, email) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (
        datos['nombre'], datos['apellido'], datos['tipoDocumento'],
        datos['numeroDocumento'], datos['ciudad'], datos['direccion'],
        datos['telefono'], datos['email']
    ))
    db.commit()
    return jsonify({"mensaje": "Cliente agregado"}), 201

# ruta para exportar a Excel
@app.route('/exportar/xlsx', methods=['GET'])
def exportar_xlsx():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    archivo = "clientes.xlsx"
    workbook = xlsxwriter.Workbook(archivo)
    sheet = workbook.add_worksheet()

    # encabezados de la tabla
    headers = ["ID", "Nombre", "Apellido", "Tipo Documento", "Número Documento", "Ciudad", "Dirección", "Teléfono", "Email"]
    for col, header in enumerate(headers):
        sheet.write(0, col, header)

    # llenado de datos
    for row, cliente in enumerate(clientes, start=1):  
        for col, dato in enumerate(cliente):
            sheet.write(row, col, dato)

    workbook.close()
    return send_file(archivo, as_attachment=True)

# ruta para eliminar clientes
@app.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    db.commit()
    return jsonify({"mensaje": "Cliente eliminado"})


# ruta para exportar a PDF
@app.route('/exportar/pdf', methods=['GET'])
def exportar_pdf():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    archivo = "clientes.pdf"
    pdf = canvas.Canvas(archivo, pagesize=letter)
    pdf.drawString(100, 750, "Lista de Clientes")

    y = 730
    for cliente in clientes:
        pdf.drawString(50, y, f"{cliente}")
        y -= 20
        if y < 50:  
            pdf.showPage()
            y = 750

    pdf.save()
    return send_file(archivo, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
