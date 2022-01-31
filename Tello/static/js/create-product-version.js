let productVersioonURL = '/api/v1/core/create-product-version/'
let addToCartUrl2 = '/api/v1/add-to-cart/'
let color;
let storage;
let quantity;

document.getElementById('product-version-form').addEventListener('submit', (e) => {
    e.preventDefault();
    document.querySelectorAll('.color-input').forEach(elem => {
        if (elem.checked) {
            color = elem.getAttribute('id')
        }
    })
    document.querySelectorAll('.storage-input').forEach(elem => {
        if (elem.checked) {
            storage = elem.getAttribute('id')
        }
    })

    quantity = document.querySelector('.count').value;
    product = document.getElementById('pk').innerText;
    category = document.getElementById('category').innerText;

    data = {
        color: color,
        storage: storage,
        quantity: quantity,
        product: product
    }

    if (category == 'Accessories') {
        data.storage = "default"
    }



    fetch(productVersioonURL, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
      })
        .then((resp) => resp.json())
        .then((data) => {
            console.log(data.color)
            if (typeof(data.color) == 'object') {
                document.getElementById('color-error').innerText = "*Zəhmət olmasa rəng secin."
            }
            else {
                console.log("Mehsul sebete atildi!");
                cartData = {
                    product: data.id,
                    user: user_id
                }
                fetch(addToCartUrl2, {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify(cartData),
                  })
                    .then((resp) => resp.json())
                    .then((cart) => {
                        document.getElementById('submit-div').innerHTML = `
                        <button type="submit" class="basket-add" style="border: none; border-radius: 8px; width: 197px; height: 48px; background-color: #FF708D; color: white; margin-right: 28px; font-size: 14px;"><img src="/static/img/check.svg" style="margin-right: 16px; width: 20px; margin-top: -2px;" alt=""> Səbətə əlavə edildi!</button>

                        `
                    })

            }
            if (typeof(data.storage) == 'object') {
                document.getElementById('storage-error').innerText = "*Zəhmət olmasa yaddaş secin."
            }
            else {
                console.log("Mehsul sebete atildi!");
            }
        })

})