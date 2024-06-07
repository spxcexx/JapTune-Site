const button = document.querySelector('#open-button')
const popup = document.querySelector('#popup')
const bg = document.querySelector("#bg")

button.addEventListener('click', (event) => {
    popup.classList.toggle('show');
    bg.classList.toggle('show')
})

const closingModalElements = [bg]
for (let el of closingModalElements){
    el.addEventListener('click',(event) => {
        popup.classList.remove('show')
        bg.classList.remove('show')
    })
}
