let next = parseInt(document.getElementById('from-pagination').innerText)+1
let numPages = parseInt(document.getElementById('num_pages').innerText)
if (next<=numPages) {
    document.getElementById('last-pagination').href = `?page=${next}`
    document.getElementById('last-pagination').innerText = next
    
}
else {
    document.getElementById('last-pagination').style.display = 'none'
}