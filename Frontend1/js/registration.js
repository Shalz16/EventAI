const API_URL = "http://127.0.0.1:8000";

window.onload = function () {
    loadRegistrations();
};

// =========================
// CREATE
// =========================

async function createRegistration() {

    const registration = {

        participant_name: document.getElementById("participant_name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        event_id: document.getElementById("event_id").value

    };

    const response = await fetch(API_URL + "/registration/register", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(registration)

    });

    if (response.ok) {

        alert("Registration Successful");

        clearForm();

        loadRegistrations();

    } else {

        const data = await response.json();

        alert(JSON.stringify(data));

    }

}

// =========================
// READ
// =========================

async function loadRegistrations() {

    const response = await fetch(API_URL + "/registration/");

    const registrations = await response.json();

    const table = document.getElementById("registrationTable");

    table.innerHTML = "";

    registrations.forEach(r => {

        table.innerHTML += `

        <tr>

            <td>${r.participant_name}</td>
            <td>${r.email}</td>
            <td>${r.phone}</td>
            <td>${r.event_id}</td>

            <td>

                <button onclick="generateQR('${r._id}')">
                    Generate QR
                </button>

            </td>

            <td>

                <button onclick="deleteRegistration('${r._id}')">
                    Delete
                </button>

            </td>

        </tr>

        `;

    });

}

// =========================
// QR GENERATION
// =========================

async function generateQR(id){

    const response = await fetch(
        API_URL + "/registration/" + id + "/generate-qr",
        {
            method:"POST"
        }
    );

    const data = await response.json();

    alert("QR Code Generated");

    console.log(data);

}

// =========================
// DELETE
// =========================

async function deleteRegistration(id){

    if(!confirm("Delete Registration?"))
        return;

    const response = await fetch(
        API_URL + "/registration/" + id,
        {
            method:"DELETE"
        }
    );

    if(response.ok){

        loadRegistrations();

    }

}

// =========================
// CLEAR FORM
// =========================

function clearForm(){

    document.getElementById("participant_name").value="";
    document.getElementById("email").value="";
    document.getElementById("phone").value="";
    document.getElementById("event_id").value="";

}