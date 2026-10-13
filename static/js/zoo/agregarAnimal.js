function showAlert(options) {
    if (window.Swal) {
        return window.Swal.fire(options);
    }

    window.alert(`${options.title}\n\n${options.text}`);
    return Promise.resolve();
}

function addAnimal(event){
    event.preventDefault();

    const name = document.getElementById("animal-name").value;
    const species = document.getElementById("animal-species").value;
    const age = document.getElementById("animal-age").value;
    const food = document.getElementById("animal-food").value;

    if(name === "") {
        showAlert({
            title: 'Nombre del animal no ingresado',
            text: 'Debe ingresar el nombre del animal.',
            icon: 'warning',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    if(species === "") {
        showAlert({
            title: 'Especie del animal no ingresada',
            text: 'Debe ingresar la especie del animal.',
            icon: 'warning',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    if(age === "") {
        showAlert({
            title: 'Edad del animal no ingresada',
            text: 'Debe ingresar la edad del animal.',
            icon: 'warning',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    if(food === "") {
        showAlert({
            title: 'Comida favorita del animal no ingresada',
            text: 'Debe ingresar la comida favorita del animal.',
            icon: 'warning',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    const data = {
        name: name,
        species: species,
        age: age,
        food: food
    };

    //endpoint
    fetch('api/animals', {
        method:"POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(data)
    }). then(response => response.json())
    .then(result =>  {
        showAlert({
            title: result.success ? 'Animal agregado' : 'Error al agregar el animal',
            text: result.message,
            icon: result.success ? 'success' : 'error',
            confirmButtonText: 'Aceptar'
        }).then(() => {
            if(result.success){
                window.location.href = "/";
            }
        });
    })
    .catch(error => {
        console.error(error);
    })

}

document.getElementById("animal-form").addEventListener("submit", addAnimal);
