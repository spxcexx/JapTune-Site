const burgerMenu  = document.querySelector('.burger_menu')
const linksDiv = document.querySelector(".burger_menu_links")
const closeMenu = document.querySelector(".close_burger")

burgerMenu.addEventListener("click", (event)=>{
    linksDiv.classList.add('showLinks')

})
closeMenu.addEventListener("click", (event)=>{
    linksDiv.classList.remove("showLinks")
})
