let removeFromCartURL = '/api/v1/remove-from-cart/'
document.querySelectorAll('.delete-button').forEach(el => {
    el.addEventListener('click', (e) => {
        product_id = e.target.getAttribute('itsfor')
        data = {
            product:product_id,
            user: user_id
        }
        fetch(removeFromCartURL, {
            method: "POST",
            headers: {
                "Content-type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data),
          })
            .then((resp) => resp.json())
            .then((data) => {
                e.target.parentElement.parentElement.parentElement.parentElement.parentElement.style.display = 'none';
            })
    })
})


