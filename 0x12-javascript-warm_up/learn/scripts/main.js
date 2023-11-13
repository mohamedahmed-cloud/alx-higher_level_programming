const helloWorld = document.querySelector("h1")
const changeH1 = document.querySelector("button")

function getName () {

    const newUser = prompt("Enter Your Name: ")
    if (!newUser) 
        return getName()


        localStorage.setItem("name", `Hi ${newUser} Welcome ` )
    helloWorld.textContent = localStorage.getItem("name");

}

if (!localStorage.getItem("name"))
{
    getName();
}
changeH1.addEventListener("click", () =>{
    getName()
})

helloWorld.textContent = localStorage.getItem("name");
let image = document.querySelector("img");
console.log(image);
image.addEventListener("click", () => {
    if (image.getAttribute("src") === "images/one.jpeg")
    {
        image.setAttribute("src", "images/two.jfif");
    }
    else {
        image.setAttribute("src", "images/one.jpeg");
    }
})


