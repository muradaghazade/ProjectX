document.addEventListener('click', (el) => {
        if (el.target.getAttribute('class') == 'storages') {
            el.target.childNodes[1].checked = true;
            document.querySelectorAll('.storages').forEach(e => {
                e.style.backgroundColor = "#F2F2F2"
                e.style.color = "black"
            })
            el.target.style.backgroundColor = "#4F4F4F"
            el.target.style.color = "white"

            
        }
    })

document.addEventListener('click', (el) => {
    if (el.target.getAttribute('class') == 'storage-item') {
        el.target.previousElementSibling.checked = true;
        document.querySelectorAll('.storages').forEach(e => {
            e.style.backgroundColor = "#F2F2F2"
            e.style.color = "black"
        })
        el.target.parentElement.style.backgroundColor = "#4F4F4F"
        el.target.parentElement.style.color = "white"
    }
})