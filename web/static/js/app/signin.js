document.getElementById('test').addEventListener('submit', async (e) => {
    e.preventDefault();
    let data = new FormData(e.target);
    let response = await fetch(`${baseUrl}api/v1/auth/token`, {
        method: 'POST',
        body: JSON.stringify(
            {
                'username': data.get('username'),
                'password': data.get('password')
            }
        ),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            return response.json();
        })
        .then(val => {
            return val
        })
        .catch(error => {
            return JSON.parse(JSON.stringify({
                'status': false, 'message': "An error occurred"
            }))
        })
    if (response.status) {
        localStorage.setItem('token', response.token);
        localStorage.setItem('user', JSON.stringify(response.user));
        Swal.fire({
            icon: 'success',
            title: 'Great',
            text: response.message,
        })
        if (document.referrer.includes("signup") || document.referrer.includes("activate")) {
            window.location.replace("/")
        }
        window.location = document.referrer;
    }
    else {
        Swal.fire({
            icon: 'info',
            title: 'Oops',
            text: response.message,
            showCancelButton: true,
        })
    }
})