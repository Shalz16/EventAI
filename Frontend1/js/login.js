document.getElementById("loginForm").addEventListener("submit", loginUser);

async function loginUser(e){

    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    try{

        const response = await fetch(API_URL + "/auth/login",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                email,
                password
            })

        });

        const data = await response.json();

        if(response.ok && data.access_token){

            localStorage.setItem("token", data.access_token);

            alert("Login Successful!");

            window.location.href = "dashboard.html";

        }
        else{

            document.getElementById("message").innerHTML =
                data.message || "Invalid Email or Password";

        }

    }
    catch(error){

        console.error(error);

        document.getElementById("message").innerHTML =
            "Cannot connect to backend.";

    }

}