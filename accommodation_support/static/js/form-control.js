let count = 2;
(function () {
    'use strict';
    window.addEventListener('load', function () {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

document.getElementById("qul-btn").addEventListener("click", (event) => {
    event.preventDefault();
    let qal_space = document.getElementById("qul-space")
    qal_space.insertAdjacentHTML("afterend", `  <div class="form-row">
                                <div class="col-md-6 mb-3">
                                    <label for="qualification">Qualification</label>
                                    <select id="qualification" class="form-control" name="qualification${count}">
                                        <option selected value="Primary">Primary</option>
                                        <option value="Secondary">Secondary</option>
                                        <option value="OND">OND</option>
                                        <option value="HND">HND</option>
                                        <option value="B.Sc/B.Agric">B.Sc/B.Agric</option>
                                        <option value="M.Sc/M.Agric">M.Sc/M.Agric</option>
                                        <option value="PhD">PhD</option>
                                    </select>
                                </div>
                                <div class="col-md-6 mb-3">
                                    <label for="year">Year</label>
                                    <input type="date" class="form-control" id="year"
                                           placeholder="Year" name="year${count}"
                                    >
                                </div>
                            </div>`)
    count++;
})

document.getElementById("is_member").addEventListener("change", (event) => {
    event.preventDefault();
    const val = document.getElementById("is_member").value;
    if (val === "True") {
        document.getElementById("will_register_div").style.display = "none"
        document.getElementById("mc").style.display = "block"
        document.getElementById("date_of_registration_div").removeAttribute("class")
        document.getElementById("date_of_registration_div").setAttribute("class", "col-md-6 mb-3")
        document.getElementById("is_member_div").removeAttribute("class")
        document.getElementById("is_member_div").setAttribute("class", "col-md-6 mb-3")
    } else if (val === "False") {
        document.getElementById("will_register_div").style.display = "block"
        document.getElementById("mc").style.display = "none"
        document.getElementById("date_of_registration_div").removeAttribute("class")
        document.getElementById("date_of_registration_div").setAttribute("class", "col-md-4 mb-3")
        document.getElementById("is_member_div").removeAttribute("class")
        document.getElementById("is_member_div").setAttribute("class", "col-md-4 mb-3")
    }
})

document.getElementById("attend_conference").addEventListener("change", (event) => {
    event.preventDefault();
    const val = document.getElementById("attend_conference").value;
    if (val === "Ture"){
        document.getElementById("mode_of_sponsorship_div").style.display = "block"
        document.getElementById("attend_conference_div").removeAttribute("class")
        document.getElementById("attend_conference_div").setAttribute("class", "col-md-6 mb-3")
    }
    else if (val === "False"){
        document.getElementById("mode_of_sponsorship_div").style.display = "none"
        document.getElementById("attend_conference_div").removeAttribute("class")
        document.getElementById("attend_conference_div").setAttribute("class", "col-md-12 mb-3")
    }
})
