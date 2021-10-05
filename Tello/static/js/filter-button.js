var intervalId;

document.getElementById('filter-show-button').addEventListener('click', () => {
    
    if(document.querySelector('.first-list-part').style.display == 'block') {
        document.querySelector('.first-list-part').style.display = "none"
    }
    else {
    document.querySelector('.first-list-part').style.display = "block"

    }
})

