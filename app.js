const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
        // else{
        //     entry.target.classList.remove('show');
        // }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el))

const observer2 = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.backgroundSize = '100% 100%';
      } else {
        entry.target.style.backgroundSize = '0% 100%';
     }
    });
  });

const fadeText = document.querySelectorAll('.fadeText');
fadeText.forEach(el => {
  observer2.observe(el);
});


const hamburger = document.querySelector(".hamburger");
const nav = document.querySelector(".mainNav");

hamburger.addEventListener("click", () => {
  nav.classList.toggle("active");
});
// observer2.observe(fadeText);