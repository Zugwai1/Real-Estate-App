 let addElementForSinglePage = async () => {
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
        try{
            document.getElementById("property-single").innerHTML = `
                <div class="col-md-12 ftco-animate">
                            <div class="single-slider owl-carousel">
                                <div class="item">
                                    <div class="properties-img"
                                         style="background-image: url(${property.images[0]});"></div>
                                </div>
                                <div class="item">
                                    <div class="properties-img"
                                         style="background-image: url(${property.images[1]});"></div>
                                </div>
                                <div class="item">
                                    <div class="properties-img"
                                         style="background-image: url(${property.images[2]});"></div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-12 Properties-single mt-4 mb-5">
                            <h2>${property.name}</h2>
                            <p class="rate mb-4">
                                <span class="loc"><a href="#"><i class="icon-map"></i>${property.address.number_line}, 
                                    ${property.address.street}, ${property.address.city}, ${property.address.state}, ${property.address.country}</a></span>
                            </p>
                            <p>${property.description}</p>
                            <div class="d-md-flex mt-5 mb-5">
                                <ul>
                                    <li><span>Price: </span>€${Number(property.price).toFixed(2)}</li>
                                    <li><span>Bed Rooms: </span> ${property.number_of_bedrooms}</li>
                                    <li><span>Bath Rooms: </span> ${property.number_of_bathrooms}</li>
                                    <li><span>Status: </span>${property.status}</li>
                                </ul>
                                <ul class="ml-md-5">
                                    <li><span>Type: </span>${property.type}</li>
                                    <li><span>Year Build:: </span> 2018</li>
                                    <li><span>Stories: </span> 1</li>
                                    <li><span>Roofing: </span> New</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-md-12 properties-single mb-5 mt-4">
                            <h3 class="mb-4">Take A Tour</h3>
                            <div class="block-16">
                                <figure>
                                    <img src="images/properties-6.jpg" alt="Image placeholder" class="img-fluid">
                                    <a href="https://vimeo.com/45830194" class="play-button popup-vimeo"><span
                                            class="icon-play"></span></a>
                                </figure>
                            </div>
                        </div>
                        <a href="${baseUrl}property/contact/${property.id}" class="btn btn-primary">I am Intrested!</a>
            `;
        }catch (e) {
            console.log(`${e}, occurred in file`)
        }
    }