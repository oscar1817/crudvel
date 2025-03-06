document.getElementById("clienteForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    let cliente = {
        nombre: document.getElementById("nombre").value,
        apellido: document.getElementById("apellido").value,
        tipoDocumento: document.getElementById("tipoDocumento").value,
        numeroDocumento: document.getElementById("numeroDocumento").value,
        ciudad: document.getElementById("ciudad").value,
        direccion: document.getElementById("direccion").value,
        telefono: document.getElementById("telefono").value,
        email: document.getElementById("email").value
    };

    await fetch("http://127.0.0.1:5000/clientes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(cliente)
    });

    mostrarClientes();
    document.getElementById("clienteForm").reset();
});

async function mostrarClientes() {
    let response = await fetch("http://127.0.0.1:5000/clientes");
    let clientes = await response.json();

    let tabla = document.getElementById("clientesTabla");
    tabla.innerHTML = "";

    clientes.forEach(cliente => {
        let fila = `<tr>
            <td>${cliente[1]}</td>
            <td>${cliente[2]}</td>
            <td>${cliente[3]}</td>
            <td>${cliente[4]}</td>
            <td>${cliente[5]}</td>
            <td>${cliente[6]}</td>
            <td>${cliente[7]}</td>
            <td>${cliente[8]}</td>
            <td><button class="btn-eliminar" data-id="${cliente[0]}">Eliminar</button></td>
        </tr>`;
        tabla.innerHTML += fila;
    });

    document.querySelectorAll(".btn-eliminar").forEach(button => {
        button.addEventListener("click", function() {
            let id = this.getAttribute("data-id");
            eliminarCliente(id);
        });
    });
}

document.addEventListener("DOMContentLoaded", mostrarClientes);

async function eliminarCliente(id) {
    if (confirm("¿Estás seguro de que deseas eliminar este cliente?")) {
        await fetch(`http://127.0.0.1:5000/clientes/${id}`, {
            method: "DELETE"
        });
        mostrarClientes();
    }
}

function exportToXLSX() {
    window.location.href = "http://127.0.0.1:5000/exportar/xlsx";
}

function exportToPDF() {
    window.location.href = "http://127.0.0.1:5000/exportar/pdf";
}
