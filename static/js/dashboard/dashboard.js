// // accordion variables
// const accordionBtns = document.querySelectorAll('.model-info');
// console.log(accordionBtns);
// const accordions = document.querySelectorAll('.model-action-list');

// accordionBtns.forEach((btn, index) => {
//   btn.addEventListener('click', () => {
//     console.log("Button Clicked");

//     const isActive = btn.nextElementSibling.classList.contains('active');

//     accordions.forEach((accordion, i) => {
//       if (index !== i) {
//         accordion.classList.remove('active');
//         accordionBtns[i].classList.remove('active');
//       }
//     });

//     btn.nextElementSibling.classList.toggle('active');
//     btn.classList.toggle('active');
//   });
// });


document.addEventListener("DOMContentLoaded", function() {
    const dropdownButtons = document.querySelectorAll(".model-info");
    // console.log(dropdownButtons);
    dropdownButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            console.log(button);
            const dropdownContent = this.nextElementSibling;
            console.log(dropdownContent.classList);
            dropdownContent.classList.toggle("active");
            console.log(dropdownContent.classList);
            closeOtherDropdowns(dropdownContent);
        });
    });

    window.addEventListener("click", function(event) {
        if (!event.target.matches(".dropbtn")) {
            dropdownButtons.forEach(button => {
                const dropdownContent = button.nextElementSibling;
                if (dropdownContent.classList.contains("active")) {
                    dropdownContent.classList.remove("active");
                }
            });
        }
    });

    function closeOtherDropdowns(currentDropdown) {
        dropdownButtons.forEach(button => {
            const dropdownContent = button.nextElementSibling;
            if (dropdownContent !== currentDropdown) {
                dropdownContent.classList.remove("active");
            }
        });
    }
});
