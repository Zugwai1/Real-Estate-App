let addPropertiesForIndexPage = async () => {
    checkRole();
    let properties = await fetch(`${baseUrl}api/v1/properties/`)
        .then(response => response.json())
        .then(data => {
            return data.properties
        }).catch(e => {
            console.log(`${e}`)
        })
    try {
        let innerHtml = ``
        properties.forEach(property => {
            innerHtml += `
         <div class="slider-item" style="background-image:url(${property.images[0]});">
            <div class="overlay"></div>
            <div class="container">
                <div class="row no-gutters slider-text align-items-md-end align-items-center justify-content-end">
                    <div class="col-md-6 text p-4 ftco-animate">
                        <h1 class="mb-3">${property.name}</h1>
                        <span class="location d-block mb-3"><i class="icon-my_location"></i>${property.address.number_line}, ${property.address.street},
                            ${property.address.city}, ${property.address.state}, ${property.address.country}</span>
                        <p>${property.description}</p>
                        <span class="price">€${Number(property.price).toFixed(2)}</span>
                        <a href="${baseUrl}property/single/${property.id}" class="btn-custom p-3 px-4 bg-primary">View Details <span
                                class="icon-plus ml-1"></span></a>
                    </div>
                </div>
            </div>
        </div>
    `
        })
        document.getElementById("propSection").innerHTML = innerHtml;
        let innerListHtml = ``;
        properties.forEach(property => {
            innerListHtml += `<div class="item">
                            <div class="properties">
                                <a href="${baseUrl}property/single/${property.id}" class="img d-flex justify-content-center align-items-center"
                                   style="background-image: url(${property.images[0]});">
                                    <div class="icon d-flex justify-content-center align-items-center">
                                        <span class="icon-search2"></span>
                                    </div>
                                </a>
                                <div class="text p-3">
                                    <span class="status sale">${property.type}</span>
                                    <div class="d-flex">
                                        <div class="one">
                                            <h3><a href="#">${property.name}</a></h3>
                                            <p>${property.type}</p>
                                        </div>
                                        <div class="two">
                                            <span class="price">€${Number(property.price).toFixed(2)}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>`
        });
        document.getElementById("properties").innerHTML = innerListHtml;
    } catch (e) {
        console.log(`${e}, occurred here`)
    }
};

