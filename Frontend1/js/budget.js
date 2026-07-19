const API_URL = "http://127.0.0.1:8000";

window.onload = function(){

    loadBudgets();

}

// =========================
// CREATE
// =========================

async function createBudget(){

    const budget={

        event_id:document.getElementById("event_id").value,

        total_budget:Number(document.getElementById("total_budget").value),

        food_cost:Number(document.getElementById("food_cost").value),

        decoration_cost:Number(document.getElementById("decoration_cost").value),

        equipment_cost:Number(document.getElementById("equipment_cost").value),

        miscellaneous_cost:Number(document.getElementById("miscellaneous_cost").value)

    };

    const response=await fetch(API_URL+"/budget/create",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(budget)

    });

    if(response.ok){

        alert("Budget Added Successfully");

        clearForm();

        loadBudgets();

    }

    else{

        const data=await response.json();

        alert(JSON.stringify(data));

    }

}

// =========================
// READ
// =========================

async function loadBudgets(){

    const response=await fetch(API_URL+"/budget/");

    const budgets=await response.json();

    const table=document.getElementById("budgetTable");

    table.innerHTML="";

    budgets.forEach(budget=>{

        table.innerHTML+=`

        <tr>

            <td>${budget.event_id}</td>

            <td>${budget.total_budget}</td>

            <td>${budget.food_cost}</td>

            <td>${budget.decoration_cost}</td>

            <td>${budget.equipment_cost}</td>

            <td>${budget.miscellaneous_cost}</td>

            <td>

                <button onclick="deleteBudget('${budget._id}')">

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

async function deleteBudget(id){

    if(!confirm("Delete Budget?"))
        return;

    const response=await fetch(API_URL+"/budget/"+id,{

        method:"DELETE"

    });

    if(response.ok){

        loadBudgets();

    }

}

// =========================
// CLEAR
// =========================

function clearForm(){

    document.getElementById("event_id").value="";
    document.getElementById("total_budget").value="";
    document.getElementById("food_cost").value="";
    document.getElementById("decoration_cost").value="";
    document.getElementById("equipment_cost").value="";
    document.getElementById("miscellaneous_cost").value="";

}