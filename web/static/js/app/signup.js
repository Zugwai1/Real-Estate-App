document.getElementById('country').addEventListener('click', async () => {
    let data = []
    data = await fetch('https://countriesnow.space/api/v0.1/countries/iso').then(response => response
        .json())
        .then(val => {
            return val.data
        }).catch(() => console.log("An error occurred"))
    data.forEach(el => {
        let option = document.createElement('option')
        option.value = el.name
        option.text = el.name
        document.getElementById('country').add(option)
    })
})

document.getElementById('country').addEventListener('change', async () => {
    $("#state").empty();
    let country = document.getElementById('country').value
    let data = []
    data = await fetch('https://countriesnow.space/api/v0.1/countries/states', {
        method: 'POST', body: JSON.stringify({
            "country": country
        }), headers: {
            'Content-Type': 'application/json'
        },
    }).then(response => response.json()).then(val => {
        return val.data.states
    })
    data.forEach(el => {
        let option = document.createElement('option')
        option.value = el.name
        option.text = el.name
        document.getElementById('state').add(option)
    })
})

document.getElementById('country').addEventListener('change', async () => {
    let country = document.getElementById('country').value
    let data = await fetch('https://countriesnow.space/api/v0.1/countries/codes', {
        method: 'POST', body: JSON.stringify({
            "country": country
        }), headers: {
            'Content-Type': 'application/json'
        },
    }).then(response => response.json()).then(val => {
        return val.data
    })
    document.getElementById('code').value = data.dial_code
})

document.getElementById('registration-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    let isValid = document.getElementById('registration-form').checkValidity() ? [true, "Form validated"] : [false, "Please ensure you fill all forms correctly"]
    let isPasswordValid =
        validatePassword(document.getElementById('password'), document.getElementById('confirm_password')) ? [true, "Password validated"] : [false, "Password dose not match"]
    let data = new FormData(e.target)
    if (isValid[0] && isPasswordValid[0]) {
        let response = await fetch(`${baseUrl}api/v1/users/`, {
            method: 'POST', body: JSON.stringify({
                'first_name': data.get('first_name'),
                'middle_name': data.get('middle_name'),
                'last_name': data.get('last_name'),
                'email': data.get('email'),
                'phone_number': data.get('phone_number'),
                'nationality': data.get('nationality'),
                'dob': data.get('dob'),
                'groups': data.get('group'),
                'password': data.get('password'),
                'country': data.get('country'),
                'state': data.get('state'),
                'city': data.get('city'),
                'number_line': data.get('number_line'),
                'postal_code': data.get('postal_code'),
                'street': data.get('street')
            }), headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => response.json()).then(val => {
            return val
        }).catch(error => {
            return JSON.parse(JSON.stringify({
                'status': false, 'message': "An error occurred"
            }))
        })
        if (response.status) {
            Swal.fire({
                icon: 'success',
                title: 'Great',
                text: 'Sign Up Successful!, Check Your Mail To Activate your account',
                showConfirmButton: false,
                 timer: 5000
            })
            window.location.replace("/signin")
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Oops',
                text: response.message,
                footer: '<a href="">Try again</a>'
            })
        }
    } else {
        if (!isValid[0]) {
            Swal.fire({
                icon: 'error',
                title: 'Oops',
                text: isValid[1],
                footer: '<a href="">Try again</a>'
            })
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Oops',
                text: isPasswordValid[1],
                footer: '<a href="">Try again</a>'
            })
        }

    }
})


function validatePassword(password, confirm_password) {
    let isvalid;
    isvalid = password.value === confirm_password.value;
    if (!isvalid) {
        password.style.borderColor = 'red'
        confirm_password.style.borderColor = 'red'
        document.querySelector('#submit-btn').setAttribute('disabled', '')
    } else {
        password.style.borderColor = 'green'
        confirm_password.style.borderColor = 'green'
        document.querySelector('#submit-btn').setAttribute('enabled', '')
    }
    return isvalid;
}


