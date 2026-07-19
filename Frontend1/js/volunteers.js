const API_URL = "http://127.0.0.1:8000";

window.onload = function () {
    loadVolunteers();
};

// =========================
// CREATE
// =========================

async function createVolunteer() {

    const volunteer = {

        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        department: document.getElementById("department").value,
        year: Number(document.getElementById("year").value),
        skills: document.getElementById("skills").value,
        availability: document.getElementById("availability").value,
        assigned_event: document.getElementById("assigned_event").value

    };

    const response = await fetch(API_URL + "/volunteers/create", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(volunteer)

    });

    if (response.ok) {

        alert("Volunteer Added Successfully");

        clearForm();

        loadVolunteers();

    } else {

        const data = await response.json();

        alert(JSON.stringify(data));

    }

}

// =========================
// READ
// =========================

async function loadVolunteers() {

    const response = await fetch(API_URL + "/volunteers/");

    const volunteers = await response.json();

    const table = document.getElementById("volunteerTable");

    table.innerHTML = "";

    volunteers.forEach(v => {

        table.innerHTML += `

        <tr>

            <td>${v.name}</td>
            <td>${v.email}</td>
            <td>${v.phone}</td>
            <td>${v.department}</td>
            <td>${v.year}</td>
            <td>${v.skills}</td>
            <td>${v.availability}</td>
            <td>${v.assigned_event}</td>

            <td>

                <button onclick="deleteVolunteer('${v._id}')">
                    Delete
                </button>

            </td>

        </tr>

        `;

    });

}

// =========================
// DELETE
// =========================

async function deleteVolunteer(id){

    if(!confirm("Delete Volunteer?"))
        return;

    const response = await fetch(API_URL + "/volunteers/" + id, {

        method:"DELETE"

    });

    if(response.ok){

        loadVolunteers();

    }

}

// =========================
// CLEAR FORM
// =========================

function clearForm(){

    document.getElementById("name").value="";
    document.getElementById("email").value="";
    document.getElementById("phone").value="";
    document.getElementById("department").value="";
    document.getElementById("year").value="";
    document.getElementById("skills").value="";
    document.getElementById("availability").value="";
    document.getElementById("assigned_event").value="";

}