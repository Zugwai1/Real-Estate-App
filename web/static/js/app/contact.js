document.addEventListener("DOMContentLoaded", async () => {
    checkRole();
    let id = document.getElementById("keep").innerText
    let property = await fetch(`${baseUrl}api/v1/properties/${id}`, {
        headers: {
            'Authorization': localStorage.getItem('token'),
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Oops',
                text: response.message,
                confirmButtonText: 'Login',
                showConfirmButton: true,
                timer: 50000,
            })
            window.location.replace("/signin");
        }
    }).then(data => {
        return data.property;
    })
    document.getElementById("prop-info").innerHTML = `
         <div class="col-md-12 mb-4">
                    <h2 class="h3">Contact Information</h2>
                </div>
                <div class="w-100"></div>
                <div class="col-md-3 d-flex">
                    <div class="info bg-white p-4">
                        <p><span>Address:</span> ${property.user.address.number_line}, ${property.user.address.street}, ${property.user.address.city}, ${property.user.address.state}, ${property.user.address.country}</p>
                    </div>
                </div>
                <div class="col-md-3 d-flex">
                    <div class="info bg-white p-4">
                        <p><span>Phone:</span> <a href="tel://1234567920">${property.user.phone_number}</a></p>
                    </div>
                </div>
                <div class="col-md-3 d-flex">
                    <div class="info bg-white p-4">
                        <p><span>Email:</span> <a href="mailto:info@yoursite.com"><p id="receiver">${property.user.email}</p></a></p>
                    </div>
                </div>
    `;
})

document.getElementById("contact-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    let data = new FormData(e.target);
    let receiver = document.getElementById("receiver").innerText;
    let property_id = document.getElementById("keep").innerText;
    await fetch(`${baseUrl}api/v1/properties/email`, {
        method: 'POST',
        body: JSON.stringify({
            'full_name': data.get('name'),
            'email': data.get('sender'),
            'sender': data.get('sender'),
            'receiver': receiver,
            'property_id': property_id,
            'subject': data.get('subject'),
            'message': data.get('message'),
        }),
        headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem('token'),
        },
    }).then(response => {
        if (!response.ok) {
            Swal.fire({
                icon: 'error',
                title: 'Message not sent',
                text: response.message,
                confirmButtonText: 'Ok',
                showConfirmButton: true,
                timer: 50000,
            })
        } else {
            Swal.fire({
                icon: 'success',
                title: 'Message sent',
                confirmButtonText: 'Ok',
                showConfirmButton: true,
                timer: 50000,
            })
        }
    })
})