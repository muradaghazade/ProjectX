// document.querySelector('.show').style.background = "red"

document.querySelectorAll('.accordion-click-me').forEach(e => {
    e.addEventListener('click', () => {
        document.querySelectorAll('.card-header').forEach(elem => {
                elem.style.borderBottom = '1px solid #828282'
            
        })
        if (e.ariaExpanded == "false") {
           
                e.parentElement.parentElement.style.borderBottom = 'none'
        
        }
    })
})